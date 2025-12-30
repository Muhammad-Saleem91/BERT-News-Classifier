# Task 1: News Topic Classifier Using BERT

## 📌 Objective
This project fine-tunes a **BERT (Bidirectional Encoder Representations from Transformers)** model to classify news headlines into four distinct categories: World, Sports, Business, and Sci/Tech. The goal is to demonstrate **Transfer Learning** using the Hugging Face ecosystem.

## 🧠 Methodology
* **Dataset:** AG News (Benchmark text classification dataset).
* **Model:** `bert-base-uncased` (Pre-trained on English text).
* **Technique:** Fine-tuning with the `Trainer` API.
* **Metrics:** Accuracy and Weighted F1-Score.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Transformers, Datasets, PyTorch, Scikit-learn, Evaluate.
* **Hardware:** Trained on T4 GPU (Google Colab).

## 📊 Results
* **Accuracy:** ~89%
* **Loss:** consistently decreased over 3 epochs, indicating stable learning.
* **Inference:** Successfully classifies unseen headlines with high confidence.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the notebook: `Task1_News_Classifier.ipynb`