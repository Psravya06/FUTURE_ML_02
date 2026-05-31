import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load data
data = pd.read_csv("support_tickets.csv")

# Features and labels
X = data["Ticket"]
y = data["Category"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Build model
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Example prediction
ticket = ["Payment issue while purchasing"]

prediction = model.predict(ticket)

print("Predicted Category:", prediction[0])

# Priority Logic
if prediction[0] in ["Billing", "Account"]:
    print("Priority: High")
elif prediction[0] in ["Technical", "Delivery"]:
    print("Priority: Medium")
else:
    print("Priority: Low")