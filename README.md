# 🌿 AI Wellness Journal

A Calm, Therapist-Inspired AI-Powered Mental Wellness Journal built using Streamlit and Hugging Face Transformers.

This application allows users to write daily reflections and receive AI-driven emotional insights, mood trends, and personal analytics.


<img width="1919" height="921" alt="Screenshot 2026-03-06 004640" src="https://github.com/user-attachments/assets/324c0c52-f829-4e57-94d1-1c8f9aa149a6" />


<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/da570a8b-f5e7-4545-8b91-1b20c60591a0" />

<img width="1919" height="913" alt="image" src="https://github.com/user-attachments/assets/727ac29d-596e-49e1-b8ac-526a65247508" />

## 🌿 Live Demo

🔗 https://emotiondetectordiary-tehciqzmkc7ns4k8ra4fw7.streamlit.app/


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

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Emotion_Detector_Diary.git
cd Emotion_Detector_Diary
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit
pandas
plotly
transformers
torch
```

---


## 📊 How Emotion Detection Works

1. User writes diary entry
2. Text is passed to Hugging Face pipeline
3. Model returns probability scores
4. Highest probability emotion is selected
5. Entry + emotion stored in CSV
6. Visual analytics generated dynamically

---

## 🔐 Data Storage

- Entries stored locally in `mood_history.csv`
- No external database
- No personal data tracking
- Fully client-side journaling experience

---

## 🚀 Deployment

Deployed using **Streamlit Community Cloud**

- Python version controlled via `runtime.txt`
- Automatic dependency resolution via `requirements.txt`
- Connected to GitHub repository

---

## 👩‍💻 Author

Fatima Zaki  
AI & Cybersecurity Enthusiast  
BTech AIML  

---

## ⭐ Why This Project Matters

Mental wellness tracking powered by AI enables:

- Emotional awareness
- Pattern recognition
- Self-reflection
- Early stress detection
- Personal growth tracking

This project demonstrates applied NLP in a real-world mental wellness use case.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💙 Acknowledgements

- Hugging Face
- Streamlit
- PyTorch
- Plotly

---

> “Reflect. Analyze. Grow.”
