<<<<<<< HEAD

import re

def clean_text(text):
    """Limpia el texto quitando números y puntuación."""
    text = str(text).lower()
    text = re.sub(r'\d+', '', text) # Quitar números
    text = re.sub(r'[^\w\s]', '', text) # Quitar puntuación
=======

import re

def clean_text(text):
    """Limpia el texto quitando números y puntuación."""
    text = str(text).lower()
    text = re.sub(r'\d+', '', text) # Quitar números
    text = re.sub(r'[^\w\s]', '', text) # Quitar puntuación
>>>>>>> 89fcacdae579e33c8dc594844f2fa18a1eb14b75
    return text.strip()