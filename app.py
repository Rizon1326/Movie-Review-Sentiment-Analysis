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

# Set the NLTK data directory to a custom path
nltk_data_path = os.path.join(os.getcwd(), '/home/rizon/Desktop/Movie_Reviewer/nltk_data/tokenizers/punkt')
nltk.data.path.append(nltk_data_path)

# Download necessary NLTK resources if they are not already available
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Load the saved model and vectorizer
with open('svc_model.pkl', 'rb') as f:
    svc = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vect = pickle.load(f)

# Set style for plots
sns.set(style="whitegrid")

# Define stop words
stop_words = set(stopwords.words('english'))

st.set_page_config(page_title="Movie Review Sentiment Analysis", page_icon="🎬", layout="wide")

# Function to preprocess text
def data_processing(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation and numbers
    text_tokens = word_tokenize(text)  # Requires the 'punkt' tokenizer
    filtered_text = [w for w in text_tokens if w not in stop_words]
    return ' '.join(filtered_text)

# Function to predict sentiment
def predict_sentiment(input_text, model, vectorizer):
    input_text_processed = data_processing(input_text)
    input_text_vectorized = vectorizer.transform([input_text_processed])
    prediction = model.predict(input_text_vectorized)[0]
    sentiment_labels = {1: "Positive", 2: "Negative"}
    return sentiment_labels.get(prediction, "Unknown")

# Function to analyze polarity using TextBlob and display a plot
def analyze_polarity(input_text):
    polarity = TextBlob(input_text).sentiment.polarity
    if polarity > 0:
        color = "green"
    elif polarity < 0:
        color = "red"
    else:
        color = "gray"

    # Create a polarity plot
    fig, ax = plt.subplots(figsize=(4, 1.5))  # Adjusted size for a more compact plot
    sns.barplot(x=["Polarity"], y=[polarity], palette=[color], ax=ax)
    ax.set_ylim(-1, 1)
    ax.set_title(f"Polarity Score: {polarity:.2f}", fontsize=12)
    ax.set_xlabel('')
    ax.set_ylabel('')
    plt.tight_layout()  # Ensures the plot fits well without extra padding
    st.pyplot(fig)
    return polarity

# Streamlit app structure
st.title("🎬 Sentiment Analysis for IMDB Dataset of 50K Movie Reviews")

# Input from user
input_sentence = st.text_input("Enter a sentence to analyze sentiment:")

if input_sentence:
    # Predict sentiment
    predicted_sentiment = predict_sentiment(input_sentence, svc, vect)
    # Satisfactory icon for Positive sentiment
    if predicted_sentiment == "Positive":
        st.markdown("<h3 style='text-align: center;'>The sentiment of the given sentence is: Positive 😊</h3>",
                    unsafe_allow_html=True)
    elif predicted_sentiment == "Negative":
        st.markdown("<h3 style='text-align: center;'>The sentiment of the given sentence is: Negative 😞</h3>",
                    unsafe_allow_html=True)

    # Analyze and plot polarity
    polarity_score = analyze_polarity(input_sentence)
    st.write(f"Polarity of the given sentence: **{polarity_score:.2f}**")
