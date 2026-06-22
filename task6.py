# Import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("product_reviews.csv")
print("Dataset loaded successfully")

# Display dataset
print("Dataset:")
print(df.head())

# Input and output
X = df["Review"]
y = df["Sentiment"]

# Convert text into numbers
vectorizer = CountVectorizer(stop_words='english')

X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# User review prediction
review = input("\nEnter a review: ")

review_vector = vectorizer.transform([review])

prediction = model.predict(review_vector)

print("\nPredicted Sentiment:", prediction[0])