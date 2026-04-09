Setup and Execution Instructions

Environment Setup:
It is recommended to use a virtual environment to avoid dependency conflicts with older TensorFlow versions.
Install requirements: pip install -r requirements.txt.

Web Scraping:
Run scraper.py to extract company feedback (Advantages and Disadvantages) from Glassdoor.

The output will be saved as a DataFrame.

Model Execution:

Run main.py. This script performs text cleaning, language separation (EN/ES), and sentiment analysis using VADER and PySentimiento/TextBlob.

MLOps Tracking:

Start the MLflow server: mlflow ui.

Open http://localhost:5000 to view logged metrics, model signatures, and artifacts like N-gram distributions.