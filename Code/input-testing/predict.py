# Note: The following testing script expects the following trained model pickle files in model-training directory
#1. logistic_regression-pca-one-gram-one-day-mixed-data-model.pkl
#2. random_forest-XGBoost-pca-one-gram-one-day-mixed-data-3k-30-model.pkl
#3. random-forest-pca-one-gram-one-day-mixed-data-model.pkl
#4. svm-pca-one-gram-one-day-mixed-data-model.pkl

# The sizes of these trained models is in GBs so they could not been uploaded to git repo. These files can be instead downloaded from following drive link:
# https://drive.google.com/drive/folders/15vqLDwFREx9gX7kcnJb68MgI4W20J0iF?usp=sharing


import pandas
import os
import pandas as pd
import nltk
import pickle
import joblib
import string
import re

from nltk.corpus import stopwords, words
from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer

with open('test-input.txt', 'r') as file:
    input_doc = file.read().replace('\n', '')

input_doc = input_doc.lower()

print("input is: \n", input_doc)

input_sentences = []
for sentence in nltk.sent_tokenize(input_doc):
    if 'amazon' in sentence or 'amzn' in sentence or 'apple' in sentence or 'aapl' in sentence:
        input_sentences.append(sentence)

def extract_words(input_words):
    from nltk.corpus import words
    
    # Remove all non-ascii words
    processed_words = [w for w in input_words if w.isascii()]
    
    # Remove punctuation words
    tr_dict = str.maketrans(dict.fromkeys(string.punctuation))
    processed_words = [w.translate(tr_dict) for w in processed_words if w]
    
    # Remove links
    final_words = []
    for word in processed_words:
        if not re.match('[www]', word):
            final_words.append(word)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    processed_words = [w for w in final_words if w not in stop_words]
    
    # Stem words and return unique words
    stemmer = SnowballStemmer('english')
    seen = set()
    processed_words = [stemmer.stem(word) for word in processed_words if word]
    processed_words = [x for x in processed_words if not (x in seen or seen.add(x))]
    del seen
    
    # Keep only words from English dictionary
    english_words = set([w.lower() for w in words.words()])
    processed_words = [w for w in processed_words if w in english_words]
    
    return processed_words


token_words = []
for sentence in input_sentences:
    token_words.extend(nltk.wordpunct_tokenize(sentence))
token_words = extract_words(token_words)

preprocessed_input = [' '.join(token_words)]

with open('trained-one-gram-vectorizer.pkl', 'rb') as f:
    trained_one_gram_vectorizer = pickle.load(f)

test_tf_idf_vector = trained_one_gram_vectorizer.transform(preprocessed_input)
print("final test vector shape:",test_tf_idf_vector.shape)


#testing input document on Logistic Regression
with open('../model-training/logistic_regression-pca-one-gram-one-day-mixed-data-model.pkl', 'rb') as f:
    logistic_regression_one_gram_one_day_classifier = pickle.load(f)
    
y_pred=logistic_regression_one_gram_one_day_classifier.predict(test_tf_idf_vector)

label = y_pred[0]
if 1 == label:
    print("As per Logistic Regression model, following given news, the stock price will go up!");
elif -1 == label:
    print("As per Logistic Regression model, following given news, the stock price will go down!");



#testing input document on xgBoost
xgboost_one_gram_one_day_classifier = joblib.load('../model-training/random_forest-XGBoost-pca-one-gram-one-day-mixed-data-3k-30-model.pkl')

y_pred=xgboost_one_gram_one_day_classifier.predict(test_tf_idf_vector)

label = y_pred[0]
if 1 == label:
    print("As per XGBoost model, following given news, the stock price will go up!");
elif -1 == label:
    print("As per XGBoost model, following given news, the stock price will go down!");


#testing input document on Random Forest
with open('../model-training/random-forest-pca-one-gram-one-day-mixed-data-model.pkl', 'rb') as f:
    random_forest_one_gram_one_day_classifier = pickle.load(f)
    
y_pred=random_forest_one_gram_one_day_classifier.predict(test_tf_idf_vector)

label = y_pred[0]
if 1 == label:
    print("As per Random Forest model, following given news, the stock price will go up!");
elif -1 == label:
    print("As per Random Forest model, following given news, the stock price will go down!");


#testing input document on SVM
with open('../model-training/svm-pca-one-gram-one-day-mixed-data-model.pkl', 'rb') as f:
    svm_one_gram_one_day_classifier = pickle.load(f)
    
y_pred=svm_one_gram_one_day_classifier.predict(test_tf_idf_vector)

label = y_pred[0]
if 1 == label:
    print("As per SVM model, following given news, the stock price will go up!");
elif -1 == label:
    print("As per SVM model, following given news, the stock price will go down!");