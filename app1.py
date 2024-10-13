import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import pandas as pd

# Set page config
st.set_page_config(page_title="Movie Review Sentiment Analysis", page_icon="🎬", layout="wide")


# NLTK setup
@st.cache_resource
def setup_nltk():
    nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
    nltk.data.path.append(nltk_data_path)
    nltk.download('punkt', quiet=True, download_dir=nltk_data_path)
    nltk.download('stopwords', quiet=True, download_dir=nltk_data_path)


setup_nltk()


# Load model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open('svc_model.pkl', 'rb') as f:
        svc = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vect = pickle.load(f)
    return svc, vect


svc, vect = load_model_and_vectorizer()

# Set style for plots
sns.set(style="whitegrid")

# Define stop words
stop_words = set(stopwords.words('english'))


# Function to preprocess text
@st.cache_data
def data_processing(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text_tokens = word_tokenize(text)
    filtered_text = [w for w in text_tokens if w not in stop_words]
    return ' '.join(filtered_text)


# Function to predict sentiment
@st.cache_data
def predict_sentiment(input_text, model, vectorizer):
    input_text_processed = data_processing(input_text)
    input_text_vectorized = vectorizer.transform([input_text_processed])
    prediction = model.predict(input_text_vectorized)[0]
    sentiment_labels = {1: "Positive", 2: "Negative"}
    return sentiment_labels.get(prediction, "Unknown")


# Function to analyze polarity using TextBlob and display a plot
def analyze_polarity(input_text):
    polarity = TextBlob(input_text).sentiment.polarity
    subjectivity = TextBlob(input_text).sentiment.subjectivity

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Polarity plot
    sns.barplot(x=["Polarity"], y=[polarity], palette=["green" if polarity > 0 else "red"], ax=ax1)
    ax1.set_ylim(-1, 1)
    ax1.set_title("Polarity", fontsize=14)
    ax1.text(0, polarity, f"{polarity:.2f}", ha='center', va='bottom' if polarity > 0 else 'top')

    # Subjectivity plot
    sns.barplot(x=["Subjectivity"], y=[subjectivity], palette=["blue"], ax=ax2)
    ax2.set_ylim(0, 1)
    ax2.set_title("Subjectivity", fontsize=14)
    ax2.text(0, subjectivity, f"{subjectivity:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    st.pyplot(fig)

    return polarity, subjectivity


# Streamlit app structure
def main():
    st.title("🎬 Movie Review Sentiment Analysis")
    st.write("Analyze the sentiment of movie reviews using machine learning!")

    # Input from user
    input_sentence = st.text_area("Enter a movie review to analyze:", height=100)

    if st.button("Analyze Sentiment"):
        if input_sentence:
            with st.spinner("Analyzing sentiment..."):
                # Predict sentiment
                predicted_sentiment = predict_sentiment(input_sentence, svc, vect)

                # Display result
                if predicted_sentiment == "Positive":
                    st.success("The sentiment of the given review is: Positive 😊")
                elif predicted_sentiment == "Negative":
                    st.error("The sentiment of the given review is: Negative 😞")

                # Analyze and plot polarity and subjectivity
                st.subheader("Sentiment Analysis")
                polarity, subjectivity = analyze_polarity(input_sentence)

                # Display metrics
                col1, col2 = st.columns(2)
                col1.metric("Polarity", f"{polarity:.2f}")
                col2.metric("Subjectivity", f"{subjectivity:.2f}")

                # Explanation
                st.info("""
                **Polarity** ranges from -1 (very negative) to 1 (very positive).
                **Subjectivity** ranges from 0 (very objective) to 1 (very subjective).
                """)
        else:
            st.warning("Please enter a movie review to analyze.")

    # Add some example reviews
    st.subheader("Try these example reviews:")
    example_reviews = [
        "This movie was absolutely fantastic! The acting was superb and the plot kept me engaged throughout.",
        "I was really disappointed with this film. The story was confusing and the characters were poorly developed.",
        "An average movie with some good moments, but overall it didn't leave a lasting impression."
    ]
    for i, review in enumerate(example_reviews, 1):
        if st.button(f"Example {i}"):
            st.text_area("Review:", value=review, height=100, key=f"example_{i}")

    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit | Data source: IMDB Dataset")


if __name__ == "__main__":
    main()