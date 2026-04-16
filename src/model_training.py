import pandas as pd
import mlflow
import mlflow.sklearn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pysentimiento import create_analyzer
import os

# Configuración de MLflow
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Glassdoor_Sentiment_Analysis")

def analyze_english_sentiment(df):
    """Aplica VADER con validación estricta de tipos de datos."""
    analyzer = SentimentIntensityAnalyzer()
    
    # Forzar la columna a string y manejar nulos de inmediato
    df['cleaned_pros'] = df['cleaned_pros'].fillna('').astype(str)
    
    def get_vader_score(text):
        # Doble validación: si no es string o está vacío, score neutral
        if not isinstance(text, str) or text.strip() == "":
            return 0.0
        return analyzer.polarity_scores(text)['compound']
    
    print("Analizando sentimientos en inglés con VADER...")
    df['sentiment_score'] = df['cleaned_pros'].apply(get_vader_score)
    
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'pos' if x >= 0.05 else ('neg' if x <= -0.05 else 'neu')
    )
    return df

def analyze_spanish_sentiment(df):
    """Aplica pysentimiento para el corpus en español."""
    analyzer = create_analyzer(task="sentiment", lang="es")
    
    # Manejo de nulos para español
    df['cleaned_pros'] = df['cleaned_pros'].fillna('').astype(str)
    
    def get_pysentimiento_label(text):
        if not isinstance(text, str) or text.strip() == "":
            return 'NEU'
        return analyzer.predict(text).output
    
    print("Analizando sentimientos en español con pysentimiento...")
    df['sentiment_label'] = df['cleaned_pros'].apply(get_pysentimiento_label)
    return df

def train_and_log():
    with mlflow.start_run():
        # 1. Cargar datos procesados
        try:
            df_en = pd.read_csv('data/processed_en.csv')
            df_es = pd.read_csv('data/processed_es.csv')
        except FileNotFoundError:
            print("Error: Archivos no encontrados en la carpeta data.")
            return

        # 2. Análisis de sentimientos
        df_en_results = analyze_english_sentiment(df_en)
        
        if len(df_es) > 0:
            df_es_results = analyze_spanish_sentiment(df_es)
            # Guardar resultados español
            df_es_results.to_csv("data/results_es.csv", index=False)
            mlflow.log_artifact("data/results_es.csv")
        
        # 3. Log de métricas
        pos_rate_en = (df_en_results['sentiment_label'] == 'pos').mean()
        mlflow.log_metric("positive_rate_en", pos_rate_en)
        
        # 4. Guardar resultados inglés
        df_en_results.to_csv("data/results_en.csv", index=False)
        mlflow.log_artifact("data/results_en.csv")
        
        print("Análisis completado exitosamente.")

if __name__ == "__main__":
    train_and_log()