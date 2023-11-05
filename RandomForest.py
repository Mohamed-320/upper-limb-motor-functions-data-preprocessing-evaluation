# Import necessary libraries
import csv

import numpy as np
import pandas as pd
from anchor import anchor_tabular
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Loading the dataset
data = pd.read_csv(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\FeaturesExtracted.csv")

# Assuming your dataset has columns for WMFT features (X) and motor function labels (y)
# Pre-Processed the data
X = data.dropna(axis=1)
print("[Input] The X data includes the kinematic measures for each patient in the preprocessed dataset")
print(X)
y = data['Score']  # fix Y value issue it should be the targeted value
print("[Output] The corresponding scores for each patient in the preprocessed dataset")
print(y)
# X = data.drop('motor_function_label', axis=1)
# y = data['motor_function_label']

# Create a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Perform k-fold cross-validation (replace 'k' with the desired number of folds)
k = 5
scores = cross_val_score(clf, X, y, cv=k)

# Print the cross-validation scores
for fold, score in enumerate(scores, start=1):
    print(f"Fold {fold} Accuracy: {1 - score:.2f}")

# Calculate and print the average accuracy across all folds
average_accuracy = np.mean(1 - scores)
print(f"Average Accuracy: {average_accuracy:.2f}")

# ## For the upper extremity assessment (which assesses functions like shoulder, elbow, forearm, wrist, and hand movements), the score typically ranges from 0 to 66.
#
# i = 1
# for item in y:
#     print("\n Sample", i, "Score is ", item, end=" ")
#     i = i + 1
#
# results = open(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\Results.csv",
#                'a', newline='')
# writer = csv.writer(results)
# writer.writerow(scores)
# results.close()
#
# j = 1
# for item in scores:
#     print("\n Sample Number", j)
#     j = j + 1
#     if item > 3:
#         print("Movement Fully Done")
#     elif item > 0 and item < 3:
#         print("Movement Partially Done")
#     else:
#         print("No Movement")
#
# # Convert predicted_labels to 1D array for anchor usage
# predicted_labels = np.squeeze(scores)
#
#
# # Create a function that returns True if the predicted label matches the actual label
# def predict_fn(x):
#     return scores[x]
#
#
# # Initialize the Anchor explainer
# explainer = anchor_tabular.AnchorTabularExplainer(
#     X,  # Training data
#     data.columns.tolist(),  # Feature names
#     predict_fn,  # Prediction function
#     categorical_names=None  # Categorical feature names, if applicable
# )
#
# # Choose a data point to explain (replace 'index' with the desired index)
# index = 0
# explanation = explainer.explain_instance(X.iloc[index].values)
#
# # Print the anchor rule explanation
# print('Explanation for prediction:')
# print('Anchor Rule for Explanation: %s' % (' AND '.join(explanation.names())))
# print('Precision: %.2f' % explanation.precision())
# print('Coverage: %.2f' % explanation.coverage())
