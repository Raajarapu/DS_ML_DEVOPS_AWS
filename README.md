# DS_ML_DEVOPS_AWS

## End-to-End Fraud Detection Platform

This project implements an end-to-end **Data Science, Machine Learning, MLOps, DevOps, Docker, and AWS Cloud workflow**. The solution starts with dataset preparation and model development in Google Colab, moves the project artifacts to GitHub, deploys the application on AWS EC2, containerises the inference service with Docker, and provides a Streamlit interface for processing new datasets and generating fraud predictions.

## Architecture

```text
Transaction Dataset
        |
        v
Google Colab
        |
        | Data Preparation / EDA / ML
        v
Trained Model
        |
        v
GitHub Repository
        |
        | Clone
        v
AWS EC2 - Ubuntu
        |
        v
Dockerfile
        |
        | docker build
        v
Docker Image
        |
        | docker run
        v
Docker Container
        |
        +----------------------+
        |                      |
        v                      v
     FastAPI              Streamlit
      :8000                  :8501
        |                      |
        |                 New Dataset
        |                      |
        |                      v
        |                     EDA
        |                      |
        |                      v
        |                 ML Prediction
        |                      |
        |                      v
        |                 Monitoring
        |                      |
        |                      v
        |                  CSV Export
        |                      |
        +----------+-----------+
                   |
                   v
              New Browser Tab
                   |
                   v
                End User






Implementation Steps
Step 01 — Create the Transaction Dataset

Prepare a small transaction dataset containing the required transaction attributes and fraud target.

Step 02 — Import the Dataset into Google Colab

Load the transaction CSV into Google Colab using Pandas.

Step 03 — Inspect the Dataset

Check the dataset shape, columns, data types, sample records and statistical information.

Step 04 — Perform Data Quality Checks

Check for missing values, duplicates, incorrect data types and inconsistent records.

Step 05 — Perform Exploratory Data Analysis

Analyse transaction behaviour, transaction amounts, time patterns and fraud distribution.

Step 06 — Select Machine Learning Features

Use amount, hour and num_tx_past_day as the primary model features.

Step 07 — Prepare the Training Dataset

Separate the feature variables from the fraud target variable.

Step 08 — Train the Machine Learning Model

Train a Random Forest classification model to identify fraudulent transactions.

Step 09 — Evaluate the Model

Evaluate the trained model using appropriate classification metrics.

Step 10 — Generate Test Predictions

Generate fraud classifications for test transactions.

Step 11 — Generate Fraud Probabilities

Generate probability scores using the model's probability prediction capability.

Step 12 — Save the Trained Model

Serialise the trained model into fraud_model.pkl for deployment.

Step 13 — Create Model Metadata

Store supporting model information in model_metadata.json.

Step 14 — Create the FastAPI Application

Create app.py to load the trained model and expose machine learning inference through an API.

Step 15 — Create the Health Endpoint

Implement GET / to verify that the FastAPI service is available.

Step 16 — Create the Prediction Endpoint

Implement POST /predict to receive transaction features and return fraud predictions.

Step 17 — Validate FastAPI Locally

Run the FastAPI service on EC2 and verify that the application starts correctly.

Step 18 — Validate Swagger Documentation

Use FastAPI's Swagger interface to test the API interactively through /docs.

Step 19 — Create the Requirements File

Create requirements.txt containing the Python dependencies required by the application.

Step 20 — Create the Dockerfile

Create a Dockerfile defining the application environment, dependencies and startup command.

Step 21 — Create the GitHub Repository

Create the DS_ML_DEVOPS_AWS repository to store the complete project.

Step 22 — Upload the Project Files

Upload the notebook, model, metadata, FastAPI application, dashboard, Dockerfile, requirements and documentation to GitHub.

Step 23 — Launch the AWS EC2 Instance

Create an Ubuntu-based EC2 instance to host the deployed application.

Step 24 — Connect to AWS EC2

Connect to the EC2 instance and verify the Linux and Docker environment.

Step 25 — Clone the GitHub Repository

Clone the project repository into the EC2 instance.

Step 26 — Install Application Dependencies

Install the required Python dependencies from requirements.txt.

Step 27 — Test FastAPI on EC2

Run the FastAPI application directly on EC2 and verify the health endpoint.

Step 28 — Test Real-Time Model Prediction

Send transaction data to /predict and verify the returned fraud classification and probability.

Step 29 — Build the Docker Image

Build the application image using:

docker build -t fraud-detection-api:1.0 .
Step 30 — Verify the Docker Image

Verify that fraud-detection-api:1.0 has been successfully created.

Step 31 — Create the Docker Container

Run the Docker image as fraud-detection-container and map the application port.

Step 32 — Verify the Docker Container

Use docker ps and container logs to confirm that the application is running successfully.

Step 33 — Test the Containerised FastAPI Service

Test the FastAPI health and prediction endpoints through the running Docker container.

Step 34 — Configure the AWS Security Group

Allow the required inbound ports for external application access:

TCP 8000 → FastAPI
TCP 8501 → Streamlit
Step 35 — Access FastAPI Through the Browser

Open the FastAPI Swagger interface from a browser using the EC2 public IP.

Step 36 — Create the Streamlit Dashboard

Create dashboard.py to provide a browser-based interface for the machine learning application.

Step 37 — Implement Dataset Upload and EDA

Allow the end user to upload a new CSV dataset and perform dataset inspection and exploratory analysis.

Step 38 — Implement Batch Predictions

Process the uploaded dataset through the trained model and generate fraud predictions and probability scores.

Step 39 — Implement Monitoring and Export

Display fraud statistics and prediction results and provide an option to export the processed dataset as CSV.

Step 40 — Perform End-to-End Validation

Open the Streamlit dashboard in a new browser tab, upload a new dataset, perform EDA, generate predictions, review fraud statistics and export the final results.
