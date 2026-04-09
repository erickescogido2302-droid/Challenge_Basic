
import re

def clean_text(text):
    """Limpia el texto quitando números y puntuación."""
    text = str(text).lower()
    text = re.sub(r'\d+', '', text) # Quitar números
    text = re.sub(r'[^\w\s]', '', text) # Quitar puntuación
    return text.strip()