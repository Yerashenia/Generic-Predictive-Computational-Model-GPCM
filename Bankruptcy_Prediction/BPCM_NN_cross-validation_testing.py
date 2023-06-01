import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Training_Data_2021_113.csv')
df.fillna(0, inplace=True)
print(df.shape)

#split data into inputs and targets
X = df.drop(columns = ['Class'])
y = df['Class']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y)

# Define the MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(20,), activation='logistic', solver='adam', max_iter=1500)

# Perform 10-fold cross validation
scores = cross_val_score(mlp, X_train, y_train, cv=10)

# Output the mean cross validation score
print("10-Fold Cross Validation Score: ", np.mean(scores))

# Fit the model on the training data
mlp.fit(X_train,y_train)

# Make predictions on the training set and output metrics
predict_train = mlp.predict(X_train)
print(confusion_matrix(y_train,predict_train))
print(classification_report(y_train,predict_train))