import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline
from datetime import datetime
import os
import random

# ===============================
# PAGE CONFIG (CENTERED!)
# ===============================
st.set_page_config(
    page_title="Wellness Journal",
    page_icon="🌿",
    layout="centered"
)

DATA_FILE = "mood_history.csv"

# ===============================
# CLEAN CALM STYLING
# ===============================
st.markdown("""
<style>
body {
    background-color: #f5f3ef;
}

section[data-testid="stSidebar"] {
    background-color: #f0ebe3;
}

h1 {
    font-weight: 500;
    color: #3e3e3e;
}

textarea {
    font-size: 15px !important;
    border-radius: 10px !important;
    background-color: #fbfaf8 !important;
}

button[kind="primary"] {
    border-radius: 22px !important;
    background-color: #c7a17a !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🌿 Journal")
page = st.sidebar.radio("", ["Diary", "Insights", "My Entries"])

# ===============================
# LOAD MODEL
# ===============================
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=None
    )

emotion_model = load_model()

emotion_colors = {
    "sadness": "#7ea8be",
    "anger": "#c97b63",
    "fear": "#b8a1c9",
    "joy": "#93c9a1",
    "neutral": "#c5c5c5",
    "surprise": "#e3b778",
    "disgust": "#8fb8b8"
}

emotion_text = {
    "sadness": "You seem a little low today.",
    "joy": "There’s warmth in your words.",
    "anger": "There’s intensity here.",
    "fear": "You sound uncertain.",
    "neutral": "Your tone feels steady.",
    "surprise": "Something unexpected stirred you.",
    "disgust": "Something didn’t sit right."
}

quotes = [
    "Healing isn’t linear.",
    "You are allowed to rest.",
    "Your feelings are valid.",
    "Growth takes time.",
    "Be gentle with yourself."
]

# ===============================
# DIARY PAGE
# ===============================
if page == "Diary":

    st.title("Wellness Journal")
    st.caption("A quiet space to reflect.")

    st.markdown(f"*{random.choice(quotes)}*")

    user_input = st.text_area("Your thoughts", height=130)

    if st.button("Reflect", type="primary") and user_input.strip():

        results = emotion_model(user_input)[0]
        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

        top_emotion = sorted_results[0]["label"]
        top_score = sorted_results[0]["score"]

        st.markdown(
            f"""
            <div style="
                padding:18px;
                border-radius:12px;
                background-color:{emotion_colors.get(top_emotion)}30;">
                <b>{emotion_text.get(top_emotion)}</b><br>
                Confidence: {top_score*100:.1f}%
            </div>
            """,
            unsafe_allow_html=True
        )

        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "emotion": top_emotion,
            "confidence": round(top_score, 3),
            "text": user_input
        }

        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
        else:
            df = pd.DataFrame([entry])

        df.to_csv(DATA_FILE, index=False)

# ===============================
# INSIGHTS PAGE
# ===============================
if page == "Insights":

    st.title("Gentle Insights")

    if not os.path.exists(DATA_FILE):
        st.info("No reflections yet.")
    else:
        df = pd.read_csv(DATA_FILE)

        # smaller trend chart
        fig_trend = px.line(
            df,
            y="confidence",
            markers=True,
            height=300
        )
        fig_trend.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_trend, use_container_width=False)

        # smaller pie chart
        emotion_counts = df["emotion"].value_counts().reset_index()
        emotion_counts.columns = ["emotion", "count"]

        fig_pie = px.pie(
            emotion_counts,
            names="emotion",
            values="count",
            color="emotion",
            color_discrete_map=emotion_colors,
            height=350
        )
        fig_pie.update_layout(margin=dict(l=20, r=20, t=30, b=20))

        st.plotly_chart(fig_pie, use_container_width=False)

# ===============================
# MY ENTRIES PAGE
# ===============================
if page == "My Entries":

    st.title("Your Reflections")

    if not os.path.exists(DATA_FILE):
        st.info("No saved entries yet.")
    else:
        df = pd.read_csv(DATA_FILE)
        df = df.sort_values(by="date", ascending=False)

        for _, row in df.iterrows():
            with st.expander(f"{row['date']} — {row['emotion']}"):
                st.write(row["text"])