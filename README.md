# 🌿 AI Wellness Journal

A Calm, Therapist-Inspired AI-Powered Mental Wellness Journal built using Streamlit and Hugging Face Transformers.

This application allows users to write daily reflections and receive AI-driven emotional insights, mood trends, and personal analytics.

---

## ✨ Features

-  Daily journal entry analysis
-  Emotion detection using pretrained NLP model
-  Mood trend visualization over time
-  Emotion distribution analysis
-  Persistent journal storage (CSV-based)
-  Calm & Cozy Therapist-Inspired UI
-  Fully local inference (no external API calls)

---

##  Emotion Detection Model

### Model Used:
**j-hartmann/emotion-english-distilroberta-base**

### Architecture:
- Base Model: DistilRoBERTa
- Task: Multi-class Text Classification
- Framework: Hugging Face Transformers
- Output: Emotion probabilities across 7 classes

### Emotion Labels:
- Joy
- Sadness
- Anger
- Fear
- Surprise
- Disgust
- Neutral

---

## 📊 Model Performance

According to the model documentation:

- Dataset: GoEmotions (Google)
- Accuracy: ~93% (reported on evaluation benchmark)
- Multi-class emotion classification
- Fine-tuned on emotion-labeled English datasets

This model is optimized for short to medium-length text inputs and performs well for diary-style reflections.

---

## 🏗️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Streamlit | Frontend & UI |
| Transformers | NLP Pipeline |
| PyTorch | Model Backend |
| Plotly | Interactive Charts |
| Pandas | Data Handling |

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
