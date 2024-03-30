import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

imdb_df = pd.read_csv('imdb_dataset.csv')

imdb_df = imdb_df.sample(n=100, random_state=42) 

imdb_df['review'] = imdb_df['review'].str.lower()

X = imdb_df['review']
y = imdb_df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
