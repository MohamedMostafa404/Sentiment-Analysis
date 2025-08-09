import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    layout="centered",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    model_path = "./" 
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

sentiment_pipeline = load_model()

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1; font-weight: bold;'>
        Twitter Sentiment Analysis
    </h1>
    <hr>
    """,
    unsafe_allow_html=True
)

user_text = st.text_area(
    "Enter your text here:",
    height=100,
    placeholder="Type your tweet or any text..."
)

if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            result = sentiment_pipeline(user_text)[0]
            label = result['label']
            score = result['score']

        emojis = {
            "positive": "😊",
            "negative": "😠",
            "neutral": "😐",
            "irrelevant": "🤷‍♂️"
        }

        colors = {
            "positive": "#d4edda",
            "negative": "#f8d7da",
            "neutral": "#d1ecf1",
            "irrelevant": "#fff3cd"
        }
        text_colors = {
            "positive": "#155724",
            "negative": "#721c24",
            "neutral": "#0c5460",
            "irrelevant": "#856404"
        }

        label_lower = label.lower()
        emoji = emojis.get(label_lower, "❓")
        bg_color = colors.get(label_lower, "#eeeeee")
        txt_color = text_colors.get(label_lower, "#000000")

        st.markdown(
            f"""
            <div style="
                background-color: {bg_color};
                color: {txt_color};
                padding: 20px;
                border-radius: 10px;
                font-size: 22px;
                font-weight: 600;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                {emoji} <b>{label}</b> <br>
                Confidence Score: {score:.2%}
            </div>
            """,
            unsafe_allow_html=True
        )
