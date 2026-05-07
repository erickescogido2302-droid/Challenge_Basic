# Glassdoor Sentiment Analysis: Bilingual NLP Pipeline

Este proyecto implementa un sistema automatizado para el análisis de sentimiento de reseñas de empleados extraídas de **Glassdoor**. La solución destaca por su capacidad de procesar contenido bilingüe y su integración con **MLflow** para la trazabilidad completa del ciclo de vida del aprendizaje automático.

## 📋 Descripción del Proyecto
El sistema procesa reseñas estructuradas en formato CSV, enfocándose específicamente en los comentarios de la columna "Pros" para detectar la percepción de los empleados.

### Características Principales:
* **Detección Automática de Idioma**: Utiliza la librería `langdetect` para identificar si la reseña está en inglés o español antes del análisis.
* **Enfoque Híbrido de Sentimiento**:
    * **VADER**: Optimizado para textos en inglés, ideal para capturar matices en reseñas de redes sociales o comentarios cortos.
    * **TextBlob**: Utilizado para asegurar una alta precisión en el procesamiento de textos en español.
* **Clasificación Tri-modal**: El modelo recibe el texto, lo limpia y asigna un puntaje de sentimiento como **Positivo**, **Neutral** o **Negativo**.

---

## 🏗️ Arquitectura del Sistema
El proyecto sigue un diseño modular para facilitar el mantenimiento y asegurar la portabilidad entre diferentes entornos:

* **`preprocessing.py`**: Implementa la normalización de texto, incluyendo la eliminación de ruido (caracteres especiales, espacios extra) y el formateo para tareas de NLP.
* **`model_training.py`**: Contiene la lógica bilingüe y los motores de análisis de sentimiento configurados para cada idioma.
* **`mlops_pipeline.py`**: El orquestador que integra el ciclo de vida del modelo con MLflow, garantizando que cada ejecución sea documentada.

---

## 🚀 Integración con MLOps (MLflow)
Para garantizar la reproducibilidad y el monitoreo, todas las ejecuciones se registran en un servidor local de MLflow:

* **Gestión de Experimentos**: Las ejecuciones se agrupan bajo el experimento "Glassdoor_Analysis".
* **Seguimiento de Métricas**: Se registra automáticamente el volumen de reseñas procesadas (`total_reviews`) en cada corrida.
* **Almacenamiento de Artefactos**: Generación y almacenamiento automático de reportes visuales de resultados (`reporte_sentimiento.png`) para auditoría inmediata.

---

## 🛠️ Guía de Ejecución Local

1. **Configurar el Entorno**: Asegúrate de tener instaladas las librerías necesarias: `pandas`, `mlflow`, `langdetect`, `nltk` y `textblob`.
2. **Iniciar Servidor de Seguimiento**: Abre una terminal y ejecuta el comando para visualizar el dashboard:
    ```bash
    mlflow ui
    ```
3. **Ejecutar el Pipeline**: Abre el Jupyter Notebook en la carpeta `notebooks/`, carga los módulos de la carpeta `src/` y llama a la función `run_mlops_pipeline(df)`.
4. **Visualizar Resultados**: Accede a `http://localhost:5000` para inspeccionar métricas y descargar los reportes de sentimiento generados.

---

**Autor**: Erick de Jesús Escogido Escobedo  
**Programa**: Maestría en Ciencia de los Datos (MCD) - CUCEA
