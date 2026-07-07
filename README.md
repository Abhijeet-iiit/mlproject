Marks Prediction - End-to-End Machine Learning Project

This repository contains an end-to-end Machine Learning pipeline designed to predict student performance/marks based on various demographic and academic factors. The project is structured following industry standard production practices, featuring modular code, logging, exception handling, and a web interface for real time predictions.

🚀 Features
Exploratory Data Analysis (EDA): Detailed notebook analysis outlining data distributions, correlation checks, and problem statements.
Modular Architecture:Clean separation of concerns with dedicated pipelines for data ingestion, transformation, and model training.
Advanced ML Modeling:Hyperparameter tuning using robust algorithms including **CatBoost**, among other regressors.
Flask Web Application:A user-friendly front-end interface built to take user inputs and output real-time predictions.

---

📁 Project Structure

├── artifacts/               # Saved datasets (train, test, raw) and trained model pickles
├── catboost_info/           # CatBoost training logs and metadata
├── notebook/                # Jupyter notebooks for EDA and model experimentation
├── src/                     # Core source code components
│   ├── components/          # Data Ingestion, Data Transformation, Model Trainer
│   ├── pipeline/            # Training and Prediction pipelines
│   ├── exception.py         # Custom exception handling
│   └── logger.py            # Custom logging setup
├── templates/               # HTML templates for the Flask web application
├── app.py                   # Flask entry point
├── requirements.txt         # Project dependencies
└── setup.py                 # Package management setup
