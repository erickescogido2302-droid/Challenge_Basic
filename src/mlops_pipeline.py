
import mlflow
import matplotlib.pyplot as plt
import pandas as pd
from langdetect import detect
# Cambia las líneas 7 y 8 a esto:
from src.preprocessing import clean_text
from src.model_training import get_sentiment

def run_mlops_pipeline(df):
    """
    Coordina la integración final del proyecto con MLOps (Etapa 3).
    """
    # 1. Configuración de MLflow (Localhost)
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Glassdoor_Analysis")

    # 2. Ejecución del Experimento
    with mlflow.start_run(run_name="MCD_Final_Execution"):
        
        # --- PROCESAMIENTO (Etapa 2) ---
        print("Procesando datos y detectando idiomas...")
        # Detectar idioma (manejo básico para textos cortos)
        df['lang'] = df['Pros'].apply(lambda x: detect(x) if len(str(x)) > 3 else 'en')
        
        # Limpieza de texto
        df['clean_text'] = df['Pros'].apply(clean_text)
        
        # --- ANÁLISIS DE SENTIMIENTO ---
        print("Calculando sentimientos (VADER/TextBlob)...")
        df['sentiment'] = df.apply(lambda r: get_sentiment(r['clean_text'], r['lang']), axis=1)

        # --- REGISTRO DE MLOPS (Etapa 3) ---
        # Registro de métrica: Cantidad total de reseñas procesadas
        mlflow.log_metric("total_reviews", len(df))
        
        # Generar gráfica de distribución
        plt.figure(figsize=(8,4))
        df['sentiment'].value_counts().plot(kind='bar', color='skyblue', title="Sentiment Analysis Summary")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        
        # Guardar y registrar la gráfica como artefacto
        plot_path = "reporte_sentimiento.png"
        plt.savefig(plot_path)
        mlflow.log_artifact(plot_path)
        
        print(f"¡Éxito! Métricas y artefactos registrados en MLflow.")
        return df