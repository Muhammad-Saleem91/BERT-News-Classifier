import streamlit as st
from transformers import pipeline

# 1. Loading the model directly from the local folder

model_path = "./bert_news_model"

@st.cache_resource  # 👈 This makes it fast! Loads model only once.
def load_classifier():
    return pipeline("text-classification", model=model_path, tokenizer=model_path)

classifier = load_classifier()

# 2. Define the Label Map (0,1,2,3 -> Text)
label_map = {
    "LABEL_0": "🌍 World",
    "LABEL_1": "⚽ Sports",
    "LABEL_2": "💼 Business",
    "LABEL_3": "🚀 Sci/Tech"
}

# 3. Streamlit UI
st.title("📰 AI News Classifier")
st.write("Enter a news headline, and BERT will categorize it for you.")

# Input Box
user_input = st.text_area("News Headline:", height=100)

if st.button("Classify"):
    if user_input.strip():
        # Make Prediction
        result = classifier(user_input)[0]
        label = label_map.get(result['label'], "Unknown")
        score = result['score']
        
        # Display Result
        st.success(f"**Category:** {label}")
        st.info(f"**Confidence:** {score:.2%}")
    else:
        st.warning("Please enter some text first!")