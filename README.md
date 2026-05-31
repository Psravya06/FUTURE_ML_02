# Support Ticket Classification System

## Project Overview

This project uses Machine Learning and Natural Language Processing (NLP) to automatically classify customer support tickets into different categories and assign priority levels. The system helps support teams handle customer issues more efficiently.

## Objective

To build a ticket classification model that can:

* Classify support tickets into categories
* Assign appropriate priority levels
* Improve support response efficiency
* Demonstrate NLP-based text classification

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NLTK
* VS Code

## Dataset

The dataset contains customer support tickets with:

* Ticket Description
* Category
* Priority Level

Categories include:

* Account
* Billing
* Technical
* Delivery
* General

## Methodology

1. Load and preprocess support ticket data.
2. Convert text into numerical features using TF-IDF Vectorization.
3. Train a Machine Learning classification model.
4. Predict ticket categories.
5. Assign priority levels based on predicted categories.
6. Evaluate model performance using accuracy score.

## Features

* Automatic ticket classification
* Text preprocessing
* Priority assignment
* Model evaluation
* NLP-based prediction

## Sample Output

Input Ticket:
"Payment issue while purchasing"

Predicted Category:
Billing

Priority:
High

## Project Structure

FUTURE_ML_02

* ticket_classifier.py
* support_tickets.csv
* requirements.txt
* README.md

## Future Improvements

* Larger training datasets
* Advanced NLP models
* Real-time ticket processing
* Web-based interface
* Multi-language support

## Conclusion

This project demonstrates the use of Machine Learning and Natural Language Processing to automate customer support workflows. It can help organizations prioritize and manage customer requests more effectively.
