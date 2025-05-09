# sepsis-detection-project

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This repository contains the code and resources for a Predictive Sepsis Detection project. The project aims to develop a system for automated medical diagnosis using Electronic Health Records (EHR) to predict the onset of sepsis.

## Overview
Sepsis is a life-threatening condition that arises when the body's response to infection causes injury to its tissues and organs. Early detection and intervention are critical for improving patient outcomes. This project utilizes machine learning and deep learning algorithms to analyze EHR data and predict the likelihood of sepsis onset.

## Contents
* Flask_App: Contains the Flask web application for deploying the predictive model.
* app.py: Flask application script.
* Dockerfile: Docker configuration file.
* random_forest_classifier.pkl: Pre-trained Random Forest classifier model.
* requirements.txt: List of Python dependencies.
* static: Directory for static files used in the web application.
* notebooks/Notebook_for_Predictive_Sepsis_Detection.ipynb: Jupyter Notebook containing the code for data preprocessing, model training, and evaluation.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         sepsis_detection_project and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── code/		   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes sepsis_detection_project a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

