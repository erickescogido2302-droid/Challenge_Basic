import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow
import os
from collections import Counter
from nltk.util import ngrams
from wordcloud import WordCloud

def generate_ngram_plot(text_series, n, title, filename):
    """Genera una gráfica de barras con los N-gramas más comunes."""
    clean_series = text_series.fillna('').astype(str)
    words = " ".join(clean_series).split()
    
    if not words:
        print(f"Advertencia: No hay palabras para generar {title}")
        return
        
    n_grams = ngrams(words, n)
    counts = Counter(n_grams)
    most_common = counts.most_common(10)
    
    if not most_common:
        return

    labels, values = zip(*[(", ".join(k), v) for k, v in most_common])
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(values), y=list(labels), palette='viridis', hue=list(labels), legend=False)
    plt.title(title)
    plt.xlabel('Frecuencia')
    plt.savefig(filename)
    plt.close()

def create_wordcloud(text_series, title, filename):
    """Genera una nube de palabras."""
    text = " ".join(text_series.fillna('').astype(str))
    if not text.strip():
        return
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.savefig(filename)
    plt.close()

def run_evaluation():
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("Glassdoor_Sentiment_Analysis")
    
    # Crear carpeta plots si no existe
    if not os.path.exists('plots'):
        os.makedirs('plots')
        print("Carpeta 'plots' creada.")

    with mlflow.start_run(run_name="Evaluation_Visuals"):
        if not os.path.exists('data/results_en.csv'):
            print("Error: No se encontró results_en.csv en la carpeta data.")
            return
            
        df = pd.read_csv('data/results_en.csv')
        
        # Limpieza de datos
        df['cleaned_pros'] = df['cleaned_pros'].fillna('').astype(str)
        df['cleaned_cons'] = df['cleaned_cons'].fillna('').astype(str)
        
        print("Generando gráficas de N-gramas...")
        generate_ngram_plot(df['cleaned_pros'], 2, 'Top 10 Bi-gramas en Pros (EN)', 'plots/bigrams_pros_en.png')
        generate_ngram_plot(df['cleaned_cons'], 2, 'Top 10 Bi-gramas en Cons (EN)', 'plots/bigrams_cons_en.png')
        
        print("Generando Nubes de Palabras...")
        create_wordcloud(df['cleaned_pros'], 'Nube de Palabras - Pros', 'plots/wordcloud_pros.png')
        create_wordcloud(df['cleaned_cons'], 'Nube de Palabras - Cons', 'plots/wordcloud_cons.png')
        
        print("Generando Distribución de Sentimientos...")
        if 'sentiment_label' in df.columns:
            plt.figure(figsize=(8, 6))
            sns.countplot(data=df, x='sentiment_label', palette='magma', hue='sentiment_label', legend=False)
            plt.title('Distribución de Sentimientos (VADER)')
            plt.savefig('plots/sentiment_distribution.png')
            plt.close()
        
        # Log de artefactos a MLflow
        mlflow.log_artifacts("plots", artifact_path="visuals")
        print("Evaluación completada exitosamente. Revisa MLflow.")

if __name__ == "__main__":
    try:
        run_evaluation()
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")