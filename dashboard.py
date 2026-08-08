import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Fraud Detection ML Dashboard",
    page_icon="",
    layout="wide"
)


# ---------------------------------------------------------
# Load Model
# ---------------------------------------------------------

MODEL_PATH = "fraud_model.pkl"

model = joblib.load(MODEL_PATH)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.title("Model Information")

st.sidebar.write("Model: Random Forest")
st.sidebar.write("Purpose: Fraud Detection")
st.sidebar.write("Inference: fraud_model.pkl")


# ---------------------------------------------------------
# Main Title
# ---------------------------------------------------------

st.title("Fraud Detection ML Dashboard")

st.write(
    "Upload a new transaction dataset to perform "
    "EDA, ML predictions, and fraud monitoring."
)


# ---------------------------------------------------------
# Dataset Upload
# ---------------------------------------------------------

st.header("1. Upload New Dataset")

uploaded_file = st.file_uploader(
    "Upload transaction CSV",
    type=["csv"]
)


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully.")


    # -----------------------------------------------------
    # Dataset Overview
    # -----------------------------------------------------

    st.header("2. Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))
    col4.metric("Duplicate Rows", int(df.duplicated().sum()))


    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)


    # -----------------------------------------------------
    # Data Validation
    # -----------------------------------------------------

    required_columns = [
        "amount",
        "hour",
        "num_tx_past_day"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]


    if missing_columns:

        st.error(
            f"Missing required columns: {missing_columns}"
        )

        st.stop()


    # -----------------------------------------------------
    # EDA
    # -----------------------------------------------------

    st.header("3. Exploratory Data Analysis")

    st.subheader("Statistical Summary")

    st.dataframe(
        df[required_columns].describe(),
        use_container_width=True
    )


    st.header("4. Exploratory Data Analysis")


    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Transaction Amount Distribution")

        fig, ax = plt.subplots()

        ax.hist(df["amount"], bins=20)

        ax.set_title("Amount Distribution")
        ax.set_xlabel("Transaction Amount")
        ax.set_ylabel("Frequency")

        st.pyplot(fig)


    with col2:

        st.subheader("Transactions by Hour")

        hour_counts = df["hour"].value_counts().sort_index()

        fig, ax = plt.subplots()

        ax.bar(
            hour_counts.index,
            hour_counts.values
        )

        ax.set_title("Transactions by Hour")
        ax.set_xlabel("Hour")
        ax.set_ylabel("Transaction Count")

        st.pyplot(fig)


    # -----------------------------------------------------
    # ML Prediction
    # -----------------------------------------------------

    st.header("5. Live ML Predictions")


    features = df[required_columns].copy()


    predictions = model.predict(features)


    probabilities = model.predict_proba(features)[:, 1]


    df["prediction"] = predictions

    df["fraud_probability"] = probabilities.round(4)

    df["prediction_label"] = df["prediction"].map(
        {
            0: "Legitimate",
            1: "Fraud"
        }
    )


    # -----------------------------------------------------
    # Fraud Monitoring
    # -----------------------------------------------------

    st.header("6. Fraud Monitoring")


    total_transactions = len(df)

    fraud_count = int(df["prediction"].sum())

    legitimate_count = total_transactions - fraud_count

    fraud_rate = (
        fraud_count / total_transactions * 100
        if total_transactions > 0
        else 0
    )


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Transactions",
        total_transactions
    )

    col2.metric(
        "Fraud Detected",
        fraud_count
    )

    col3.metric(
        "Legitimate",
        legitimate_count
    )

    col4.metric(
        "Fraud Rate",
        f"{fraud_rate:.2f}%"
    )


    # -----------------------------------------------------
    # Probability Distribution
    # -----------------------------------------------------

    st.subheader("Fraud Probability Distribution")


    fig, ax = plt.subplots()

    ax.hist(
        df["fraud_probability"],
        bins=10
    )

    ax.set_title("Fraud Probability")
    ax.set_xlabel("Fraud Probability")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)


    # -----------------------------------------------------
    # Prediction Results
    # -----------------------------------------------------

    st.header("7. Prediction Results")

    st.dataframe(
        df,
        use_container_width=True
    )


    # -----------------------------------------------------
    # Export Results
    # -----------------------------------------------------

    st.header("8. Export Results")


    csv_data = df.to_csv(index=False)


    st.download_button(
        label="Download Predictions CSV",
        data=csv_data,
        file_name="fraud_predictions.csv",
        mime="text/csv"
    )


    st.success(
        "Dataset analysis and ML prediction completed."
    )
