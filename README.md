# 🔍 Log Classification System Using Hybrid Methods

This project presents a robust log classification system designed to effectively categorize system and application logs using a hybrid classification framework. Built with flexibility and real-world adaptability in mind, this system leverages a combination of rule-based and machine learning approaches to handle both simple and complex log patterns.

🎯 **Live Demo:** [Streamlit App](https://log-classification-systems.streamlit.app/)


## 🚀 Key Features

* 🧠 **Hybrid Classification Pipeline:** Integrates multiple techniques—Regex, Machine Learning, and LLMs—to achieve high accuracy across diverse log types.
* 🧾 **User-Friendly Interface:** Built with Streamlit for an interactive and easy-to-use experience.
* 🔄 **Dynamic Method Switching:** Selects the most suitable classification method based on log type.

---

## 🔧 Classification Techniques Used

### 1. **Regex-Based Matching**

* Ideal for logs with known, repeated patterns.
* Quickly identifies simple log types using pre-defined regular expressions.

### 2. **Sentence Transformers + Logistic Regression**

* Captures contextual information from log entries.
* Sentence embeddings are passed through a Logistic Regression model trained on labeled log data.
* Best suited for logs with moderate structure and sufficient training data.

### 3. **LLM-Based Classification**

* Employs Large Language Models (LLMs) to understand complex, less structured log entries.
* Effective in low-data scenarios where traditional ML struggles.
* Acts as a fallback when regex and logistic regression are insufficient.
* Here, it works specifically for a 'LegacyCRM' source logs.

---

## 🛠 Technologies Used

* **Streamlit** – for building the interactive web app
* **Transformers** – for generating embeddings
* **scikit-learn** – for Logistic Regression model
* **Regex** – for rule-based log matching
* **Groq API (deepseek-R1 model)** – for intelligent fallback classification

---

## 🧪 How to Use

1. **Upload** your log message(s) csv in the app.
2. The system **analyzes each log line** and selects the best classification approach.
3. Results are **displayed with category labels** and the output file can be downloaded from the app.

---

## 📦 Setup Instructions (Local)

```bash
git clone https://github.com/Naima-ai/Log-Classification-System.git
cd Log-Classification-System
pip install -r requirements.txt
streamlit run app.py
```



## 🤝 Acknowledgements

Inspired by implementations of hybrid log classification approaches by Codebasics.
---
