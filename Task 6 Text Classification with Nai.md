## **Task 6: Text Classification with Naive Bayes** 



1\. Objective



The aim of this task is to classify customer reviews into:



\* Positive Review

\* Negative Review



using the \*\*Naive Bayes Machine Learning Algorithm\*\*.



This is a \*\*Text Classification\*\* problem because the input is text and the output is a category.





2\. Real-World Applications



Text Classification is used in:



Email Filtering



\* Spam

\* Not Spam



Product Reviews



\* Positive

\* Negative



Social Media Analysis



\* Happy

\* Sad

\* Angry



Customer Feedback Analysis



\* Satisfied

\* Unsatisfied



News Categorization



\* Sports

\* Politics

\* Technology







3\. What is Naive Bayes?



Naive Bayes is a classification algorithm based on \*\*Bayes Theorem\*\*.



It predicts the class of a text by calculating probabilities.



Example:



Review:



Excellent camera quality



Words:



\* Excellent

\* Camera

\* Quality



The model checks:



Probability of Positive

Probability of Negative



If:

Positive Probability > Negative Probability



then

Prediction = Positive





4\. Dataset Used



File:

product\_reviews.csv



Columns:



| Review                   | Sentiment |

| ------------------------ | --------- |

| Excellent battery life   | Positive  |

| Waste of money           | Negative  |

| Very good camera quality | Positive  |

| Poor build quality       | Negative  |





5\. Libraries Used



***import pandas as pd***



Purpose:

Used for loading and handling datasets.



***from sklearn.model\_selection import train\_test\_split***



Purpose:

Used to split data into:



\* Training Data

\* Testing Data



***from sklearn.feature\_extraction.text import CountVectorizer***



Purpose:

Converts text into numerical form.

Computers cannot understand words.



Example:

excellent camera quality

becomes

\[1, 1, 1]



***from sklearn.naive\_bayes import MultinomialNB***



Purpose:

Creates the Naive Bayes model.



***from sklearn.metrics import accuracy\_score***



Purpose:

Calculates model accuracy.



***from sklearn.metrics import classification\_report***



Purpose:

Shows:

\* Precision

\* Recall

\* F1 Score

\* Support





6\. Loading Dataset



***df = pd.read\_csv("product\_reviews.csv")***



Meaning:

Read CSV file and store it in dataframe.



Example:



| Review       | Sentiment |

| ------------ | --------- |

| Good product | Positive  |

| Bad quality  | Negative  |





7\. Display Dataset



***print(df.head())***



Purpose:

Shows first 5 rows.



Example:

Good product     Positive

Bad quality      Negative

Excellent phone  Positive





8\. Input and Output Selection

***X = df\["Review"]***



Input Features

Contains reviews.



Example:

***Excellent battery life***



***y = df\["Sentiment"]***



Target Variable

Contains labels.



Example:

Positive

Negative





9\. Text Vectorization



Why Needed?



Computers understand numbers only.

They cannot understand:



***Excellent phone***



So we convert text into numbers.



Create Vectorizer



***vectorizer = CountVectorizer()***



Creates text converter.

Convert Text



***X\_vectorized = vectorizer.fit\_transform(X)***



Example:

Original Reviews



***excellent phone***

***good battery***



Vocabulary:



***excellent***

***phone***

***good***

***battery***



Converted:



| excellent | phone | good | battery |

| --------- | ----- | ---- | ------- |

| 1         | 1     | 0    | 0       |

| 0         | 0     | 1    | 1       |



This is called:



Bag of Words Model



10\. Splitting Dataset



***X\_train, X\_test, y\_train, y\_test = train\_test\_split(***

&#x20;   ***X\_vectorized,***

&#x20;   ***y,***

&#x20;   ***test\_size=0.2,***

&#x20;   ***random\_state=42***

***)***



Purpose:

Divide data into:



Training Data

80%

Used for learning.



Testing Data

20%

Used for evaluation.



Example:

100 Reviews



***80 -> Training***

***20 -> Testing***





11\. Create Model



***model = MultinomialNB()***



Creates Naive Bayes classifier.





12\. Train Model



***model.fit(X\_train, y\_train)***



Purpose:

Teach the model.



The model learns:

***excellent → Positive***

***amazing → Positive***

***bad → Negative***

***worst → Negative***





13\. Prediction



***y\_pred = model.predict(X\_test)***



Purpose:

Predict sentiments for testing data.



Example:

Actual:



***Positive***

***Negative***

***Positive***



Predicted:



***Positive***

***Negative***

***Positive***





14\. Accuracy Calculation



***accuracy = accuracy\_score(y\_test, y\_pred)***



Formula:

Example:

10 reviews tested



Correct predictions:

***8***





Accuracy:

***8/10 × 100***

***= 80%***





15\. Print Accuracy



***print("Accuracy:", accuracy)***



Example Output:

***Accuracy: 0.92***



Meaning:

92% accuracy





16\. Classification Report



***print(classification\_report(y\_test, y\_pred))***



Shows:

**Precision**

Out of all predicted positives,

how many were actually positive?



**Recall**

Out of all actual positives,

how many were found?



**F1 Score**

Balance between Precision and Recall.



**Support**

Number of samples.





17\. User Review Prediction



***review = input("Enter a review: ")***

Takes review from user.



Example:

***excellent camera quality***





18\. Convert User Review



***review\_vector = vectorizer.transform(\[review])***

Converts review into numerical format.





19\. Predict Sentiment



***prediction = model.predict(review\_vector)***



Example:

Input:

***excellent camera quality***



Output:

***Positive***





20\. Display Prediction



***print("Predicted Sentiment:", prediction\[0])***



Output:

***Predicted Sentiment: Positive***





21\. Workflow of Entire Project



***Load Dataset***

&#x20;     ***↓***

***Select Input and Output***

&#x20;     ***↓***

***Convert Text to Numbers***

&#x20;     ***↓***

***Split Data***

&#x20;     ***↓***

***Create Naive Bayes Model***

&#x20;     ***↓***

***Train Model***

&#x20;     ***↓***

***Predict Test Data***

&#x20;     ***↓***

***Calculate Accuracy***

&#x20;     ***↓***

***Generate Classification Report***

&#x20;     ***↓***

***Take User Review***

&#x20;     ***↓***

***Predict Sentiment***







