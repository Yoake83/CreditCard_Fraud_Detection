# Credit Card Fraud Detection System

An end-to-end **Machine Learning–based Credit Card Fraud Detection System** that identifies fraudulent transactions in real time using anonymized financial data. The project demonstrates the complete ML lifecycle — from data preprocessing and model training to backend API development and user-friendly UI.

---

##  Project Overview

Credit card fraud is a major challenge in the financial sector due to **high class imbalance, evolving fraud patterns, and privacy constraints**. This project uses a **Random Forest classifier** trained on PCA-transformed transaction data to predict whether a transaction is **Fraudulent or Legitimate**.

The system is deployed locally with:

* **FastAPI** for backend inference
* **Streamlit** for interactive UI

---

##  Key Concepts Used

* Machine Learning (Supervised Classification)
* PCA (Principal Component Analysis)
* Handling Imbalanced Datasets
* Feature Scaling
* Model Serialization
* REST API Development
* UI Integration

---

##  Dataset

* Source: Kaggle Credit Card Fraud Dataset
* Transactions made by European cardholders
* Highly imbalanced dataset (~0.17% fraud)

###  Features

* **V1–V28**: PCA-transformed anonymized features
* **Amount**: Transaction amount
* **Class**:

  * `0` → Legitimate Transaction
  * `1` → Fraudulent Transaction

> Note: The real-world meaning of V1–V28 is intentionally hidden to protect user privacy.

---

## ⚙️ Tech Stack

**Language:** Python

**Machine Learning:**

* scikit-learn
* pandas
* numpy

**Backend:**

* FastAPI
* Uvicorn

**Frontend:**

* Streamlit

**Model Persistence:**

* joblib

---

##  Project Structure

```
CreditcardDetection/
│
├── model/
│   ├── fraud_model.pkl      # Trained ML model
│   └── scaler.pkl           # Feature scaler
│
├── app.py                   # FastAPI backend
├── ui.py                    # Streamlit UI
├── train_model.py           # Model training script
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Workflow

1. Load and preprocess dataset
2. Scale numerical features
3. Train Random Forest classifier
4. Save trained model and scaler
5. Serve predictions using FastAPI
6. Consume API via Streamlit UI

---

##  How to Run the Project

### 1️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️ Train the Model

```bash
python train_model.py
```

### 3️ Start FastAPI Backend

```bash
uvicorn app:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

### 4️ Start Streamlit UI

```bash
python -m streamlit run ui.py
```

UI will open at:

```
http://localhost:8501
```

---

##  Model Output

* **Prediction:** Fraud / Not Fraud
* **Confidence Score:** Probability of fraud

---

##  Challenges Addressed

* Severe class imbalance
* Privacy-preserving feature engineering
* Feature mismatch handling
* Model–API–UI integration

---

##  Future Improvements

* Use XGBoost / LightGBM
* Add SMOTE or advanced imbalance handling
* Model explainability (SHAP / LIME)
* Cloud deployment (Render / Hugging Face)
* Authentication & logging

---

##  Author

**Yoake**
GitHub: [https://github.com/Yoake83](https://github.com/Yoake83)


⭐ If you find this project helpful, feel free to star the repository!
