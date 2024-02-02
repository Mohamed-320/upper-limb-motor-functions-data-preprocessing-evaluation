# Import required libraries
import csv

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the training data and the test data
data = pd.read_csv(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\FeaturesExtracted.csv")
# print("======= THE TRAINED DATA FOR THE Decision TREE ALGORITHM =======" + trainData)

# Pre-Processed the data
X = data.dropna(axis=1)
print("[Input] The X data includes the kinematic measures for each patient in the preprocessed dataset")
print(X)
y = data['Score']  # fix Y value issue it should be the targeted value
print("[Output] The corresponding scores for each patient in the preprocessed dataset")
print(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the decision tree model
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)
print('Test Set:', y_pred)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Decision Tree Model Accuracy: ', accuracy)

## For the upper extremity assessment (which assesses functions like shoulder, elbow, forearm, wrist, and hand movements), the score typically ranges from 0 to 66.
i = 1
for item in y_pred:
    print("\n Sample", i, "Score is ", item, end=" ")
    i = i + 1

results = open(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\Results.csv",
               'a',
               newline='')
writer = csv.writer(results)
writer.writerow(y_pred)
results.close()

j = 1
for item in y_pred:
    print("\n Sample Number", j)
    j = j + 1
    def score(item):
        match item:
            case 1:
                return "The patient does slightly attempt with the UE being tested!"
            case 2:
                return "The patient does attempt, but requires the assistance for minor re-adjustments or change of position!"
            case 3:
                return "The patient does attempt slowly performance or with effort!"
            case 4:
                return "The patient does attempt; movement is similar to the non-affected side but slightly slower!"
            case 5:
                return "The patient does attempt, and movement appears to be normal!"
            case default:
                return "No movement done!"


    print(score(item))

# Visualize the decision tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(classifier, feature_names=X.columns, filled=True, rounded=True)
plt.show()

# Define feature names
# Explain individual predictions using the anchor_tabular method
explainer = anchor_tabular.AnchorTabularExplainer(
    X, X_train, classifier.predict,
    categorical_names=None  # Replace with categorical feature names if applicable
)

# Get the anchor rule for the selected instance
explanation = explainer.explain_instance(X_train, classifier.predict, threshold=0.95)

# Print the anchor rule
print('Anchor Rule for Explanation: %s' % (' AND '.join(explanation.names())))
print('Precision: %.2f' % explanation.precision())
print('Coverage: %.2f' % explanation.coverage())
