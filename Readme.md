# Challenge\_Basic



Glassdoor Companies Feedback Analysis (NLP \& MLOps)



1\. Project Description

This project aims to analyze employee feedback (Pros and Cons) from Glassdoor using Natural Language Processing (NLP) techniques. The pipeline includes automated web scraping data handling, sentiment analysis for both English and Spanish, and an MLOps integration for experiment tracking.



2\. Dataset Extraction 

The analysis is based on the employee\_reviews.csv dataset



Source: Real-world company reviews from Glassdoor.

Content: 67,529 entries featuring text-based feedback and numerical ratings.

Preprocessing: The data is cleaned by removing irrelevant variables, handling missing values, and splitting the corpus by language (English and Spanish).



3\. Model Construction

The sentiment analysis follows a comparative approach:



English Corpus: Evaluated using VADER (Valence Aware Dictionary and sEntiment Reasoner) due to its efficiency with social media-style text.



Spanish Corpus: Evaluated using pysentimiento, a specialized library for Spanish NLP tasks.



Feature Engineering: Includes Lemmatization, Stop-word removal, and N-gram distribution analysis.



4\. MLOps Integration

Experiment tracking is managed via MLflow.



Metrics: Logging sentiment distribution and positive review rates.

Artifacts: Storage of model signatures, sentiment plots, and N-gram frequency charts.

Tracking: All runs are logged to a local server for future reference.



5\. Execution Guide

To run this project, follow these steps:

Prerequisites



Python 3.x

MLflow server running locally (mlflow ui)

