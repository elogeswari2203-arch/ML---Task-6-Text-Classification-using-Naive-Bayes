# Task 6 – Text Classification using Naive Bayes

## Overview

This project implements a Text Classification model using the Multinomial Naive Bayes algorithm. The model analyzes customer product reviews and predicts whether the sentiment is Positive or Negative.

## Objective

To build a machine learning model capable of performing sentiment analysis on textual customer reviews using Natural Language Processing (NLP) techniques.

## Dataset

A custom Product Reviews dataset was used containing:

* Review (Text Input)
* Sentiment (Positive / Negative)

Example:

| Review                   | Sentiment |
| ------------------------ | --------- |
| Excellent battery life   | Positive  |
| Waste of money           | Negative  |
| Very good camera quality | Positive  |

## Technologies Used

* Python
* Pandas
* Scikit-learn
* CountVectorizer
* Multinomial Naive Bayes

## Project Workflow

1. Load the dataset
2. Separate input and target variables
3. Convert text into numerical vectors using CountVectorizer
4. Split data into training and testing datasets
5. Train the Multinomial Naive Bayes classifier
6. Predict sentiments for testing data
7. Evaluate model performance using:

   * Accuracy
   * Precision
   * Recall
   * F1-Score
8. Predict sentiment for user-entered reviews

## Features

* Automatic sentiment prediction
* Text preprocessing using Bag of Words
* Performance evaluation using classification metrics
* Interactive user review testing

## Sample Predictions

Input:
Excellent camera quality

Output:
Positive

Input:
Waste of money

Output:
Negative

## Learning Outcomes

* Understanding Text Classification
* Natural Language Processing Basics
* Feature Extraction using CountVectorizer
* Naive Bayes Classification
* Model Evaluation Techniques
* Sentiment Analysis Applications

## Conclusion

This project demonstrates how Machine Learning and Natural Language Processing can be combined to classify customer reviews based on sentiment. It provides a simple yet effective implementation of text classification using the Naive Bayes algorithm.
