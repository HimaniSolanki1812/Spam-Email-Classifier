# 📧 Spam Email Classifier

A Machine Learning project that classifies messages as **Spam** or **Ham (Not Spam)** using the **Naive Bayes** algorithm and **TF-IDF Vectorization**.

---

## 📌 Project Overview

Spam emails and messages are a common problem in digital communication. This project uses Natural Language Processing (NLP) and Machine Learning to automatically classify incoming messages as **Spam** or **Not Spam**.

---

## 🚀 Features

- Classifies SMS/Email messages as Spam or Not Spam
- Uses TF-IDF Vectorization for text feature extraction
- Trained using the Multinomial Naive Bayes algorithm
- Predicts custom messages entered by the user
- Easy to understand and beginner-friendly project

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Jupyter Notebook

---

## 📂 Project Structure

```
Spam-Email-Classifier/
│
├── dataset/
│   └── SMSSpamCollection
│
├── notebooks/
│   └── Spam_Email_Classifier.ipynb
│
├── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Dataset

Dataset Used:
**SMS Spam Collection Dataset**

The dataset contains labeled SMS messages:
- **Ham** – Normal messages
- **Spam** – Unwanted promotional or fraudulent messages

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Text Cleaning
4. TF-IDF Feature Extraction
5. Train-Test Split
6. Train Naive Bayes Model
7. Evaluate Model
8. Predict New Messages

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Spam-Email-Classifier.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Prediction

```bash
python predict.py
```

---

## 💬 Example

Input:

```
Congratulations! You have won a free iPhone.
```

Output:

```
🚨 Spam Message
```

Input:

```
Hi, are we meeting tomorrow?
```

Output:

```
✅ Not Spam
```

---

## 📈 Future Improvements

- Build a web application using Flask or Streamlit
- Improve accuracy using advanced NLP techniques
- Support multiple languages
- Add a user-friendly interface

---

## 👩‍💻 Developed By

**Himani Solanki**

Computer Engineering Student

---
