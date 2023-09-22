import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porterstem = PorterStemmer()

# Load the vectorizer and model
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('FAKE NEWS DETECTOR')

input_news = st.text_area("Enter the NEWS")

def stemming(content):
    stem_content = re.sub('[^a-zA-Z]', ' ', content)  # Fixed the regex pattern
    stem_content = stem_content.lower()
    stem_content = stem_content.split()
    stem_content = [porterstem.stem(word) for word in stem_content if word not in stopwords.words('english')]  # Fixed the if condition
    stem_content = ' '.join(stem_content)
    
    return stem_content

if st.button('DETECT'):
    news = stemming(input_news)
    news = [news]  # Wrap the news in a list to match the expected input format
    news = vectorizer.transform(news)  # Use transform, not fit
    prediction = model.predict(news)

    if prediction[0] == 0:
        st.header("REAL NEWS")
    else:
        st.header("FAKE NEWS")

