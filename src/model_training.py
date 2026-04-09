<<<<<<< HEAD

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

vader = SentimentIntensityAnalyzer()

def get_sentiment(text, lang):
    """Clasifica el sentimiento según el idioma."""
    try:
        if lang == 'en':
            score = vader.polarity_scores(text)['compound']
            return 'POS' if score >= 0.05 else ('NEG' if score <= -0.05 else 'NEU')
        else:
            # Análisis para español u otros usando TextBlob
            analysis = TextBlob(text)
            return 'POS' if analysis.sentiment.polarity > 0 else 'NEG'
    except:
=======

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

vader = SentimentIntensityAnalyzer()

def get_sentiment(text, lang):
    """Clasifica el sentimiento según el idioma."""
    try:
        if lang == 'en':
            score = vader.polarity_scores(text)['compound']
            return 'POS' if score >= 0.05 else ('NEG' if score <= -0.05 else 'NEU')
        else:
            # Análisis para español u otros usando TextBlob
            analysis = TextBlob(text)
            return 'POS' if analysis.sentiment.polarity > 0 else 'NEG'
    except:
>>>>>>> 89fcacdae579e33c8dc594844f2fa18a1eb14b75
        return 'NEU'