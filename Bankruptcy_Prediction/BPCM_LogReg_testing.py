import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import LabelBinarizer

# Load the dataset
df = pd.read_csv('Training_Data_2021_113.csv')
df.fillna(0, inplace=True)

# Split data into inputs and targets
X = df.drop(columns = ['Class'])
y = df['Class']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y)

# Create a logistic regression model
logreg = LogisticRegression(max_iter=2000)

# Train the model
logreg.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg.predict(X_test)

# Calculate and print the accuracy score
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Print classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Calculate AUC-ROC
# Binarize the output
lb = LabelBinarizer()
y_test_bin = lb.fit_transform(y_test)
y_pred_bin = lb.transform(y_pred)
print("AUC-ROC: ", roc_auc_score(y_test_bin, y_pred_bin))
