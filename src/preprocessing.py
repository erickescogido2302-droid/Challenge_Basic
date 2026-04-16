import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import os

# Descarga de recursos necesarios para NLTK
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('punkt_tab')

def load_and_initial_clean(file_path):
    """Carga el dataset y realiza limpieza básica inicial."""
    df = pd.read_csv(file_path)
    # Eliminar variables irrelevantes [cite: 17, 45]
    cols_to_drop = ['Unnamed: 0', 'link']
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
    
    # Manejo de nulos en columnas de texto [cite: 11, 42]
    text_cols = ['summary', 'pros', 'cons', 'advice-to-mgmt']
    for col in text_cols:
        df[col] = df[col].fillna('')
    
    return df

def detect_language_heuristic(text):
    """Heurística para separar inglés y español basada en stop words[cite: 88]."""
    if not text or len(text.strip()) < 5:
        return 'unknown'
    
    words = set(text.lower().split())
    es_stops = {'el', 'la', 'de', 'que', 'en', 'y', 'a', 'los', 'del', 'se', 'por', 'con'}
    en_stops = {'the', 'and', 'to', 'of', 'in', 'is', 'it', 'that', 'with', 'for', 'on'}
    
    es_count = len(words.intersection(es_stops))
    en_count = len(words.intersection(en_stops))
    
    if es_count > en_count:
        return 'es'
    return 'en'

def preprocess_text(text, language='english'):
    """Limpieza, stop words y lematización[cite: 90, 91, 92]."""
    # Limpieza de caracteres especiales y números
    text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', text).lower()
    
    # Tokenización
    tokens = nltk.word_tokenize(text)
    
    # Stop words
    stop_words = set(stopwords.words(language))
    tokens = [w for w in tokens if w not in stop_words]
    
    # Lematización
    lemmatizer = WordNetLemmatizer()
    # Nota: NLTK Lemmatizer es principalmente para inglés. 
    # Para un español robusto se recomendaría Spacy, pero usamos NLTK por simplicidad.
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    
    return " ".join(tokens)

def run_preprocessing_pipeline(input_path):
    print(f"--- Iniciando Preprocesamiento de {input_path} ---")
    
    # 1. Carga [cite: 119]
    df = load_and_initial_clean(input_path)
    
    # 2. Identificación de idioma [cite: 88]
    df['language'] = df['pros'].apply(detect_language_heuristic)
    
    # 3. Separación de DataFrames [cite: 89]
    df_en = df[df['language'] == 'en'].copy()
    df_es = df[df['language'] == 'es'].copy()
    
    print(f"Registros en Inglés: {len(df_en)}")
    print(f"Registros en Español: {len(df_es)}")
    
    # 4. Procesamiento de texto (Pros y Cons) [cite: 90, 91, 92]
    for col in ['pros', 'cons']:
        print(f"Procesando columna: {col}...")
        df_en[f'cleaned_{col}'] = df_en[col].apply(lambda x: preprocess_text(x, 'english'))
        df_es[f'cleaned_{col}'] = df_es[col].apply(lambda x: preprocess_text(x, 'spanish'))
    
    # 5. Guardar resultados para la siguiente etapa [cite: 12]
    os.makedirs('data', exist_ok=True)
    df_en.to_csv('data/processed_en.csv', index=False)
    df_es.to_csv('data/processed_es.csv', index=False)
    
    print("--- Preprocesamiento completado. Archivos guardados en data/ ---")

if __name__ == "__main__":
    # Cambia esto para que busque dentro de la carpeta data
    run_preprocessing_pipeline('data/employee_reviews.csv')