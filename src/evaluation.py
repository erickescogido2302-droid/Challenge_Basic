
import matplotlib.pyplot as plt

def plot_sentiment_summary(df):
    """Genera un resumen visual rápido."""
    summary = df['sentiment'].value_counts()
    print("Resumen de Sentimientos:")
    print(summary)
    summary.plot(kind='pie', autopct='%1.1f%%')
    plt.show()