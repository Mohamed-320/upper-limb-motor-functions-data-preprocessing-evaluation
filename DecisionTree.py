# Import required libraries
import pandas as pd
from anchor import anchor_tabular
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the training data and the test data
data = pd.read_csv(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\FeaturesExtracted.csv")
# fma_scores = pd.read_csv(
#     r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\Results.csv")
# print("======= THE TRAINED DATA FOR THE Decision TREE ALGORITHM =======" + trainData)

# Pre-Processed the data
X = data.dropna(axis=1)
print("[Input] The X data includes the kinematic measures for each patient in the preprocessed dataset")
print(X)
y = data['FMAScore']  # fix Y value issue it should be the targeted value
print("[Output] The corresponding Fugl-Meyer scores for each patient in the preprocessed dataset")
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
# FIXME refactor accuracy calculations
accuracy = 1 - accuracy_score(y_test, y_pred)
print('Decision Tree Model Accuracy:', accuracy)

## For the upper extremity assessment (which assesses functions like shoulder, elbow, forearm, wrist, and hand movements), the score typically ranges from 0 to 66.

# Method to calculate the Upper Extremity Score for Fugl-Meyer Assessment
# def calculate_upper_extremity_score(dataset):
#     upper_extremity_score = dataset['UpperExtremityScore'].sum()
#     return upper_extremity_score
#
# # Assuming you have a dataset 'fma_dataset' containing FMA parameters
# upper_extremity_score = calculate_upper_extremity_score(X)
# print("Upper Extremity Score:", upper_extremity_score)

# Visualize the decision tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(classifier, feature_names=X.columns, filled=True, rounded=True)
plt.show()

# Define feature names (optional)
feature_names = ['Age', 'Income', 'Credit Score', 'Existing Debt']

# Explain individual predictions using the anchor_tabular method
explainer = anchor_tabular.AnchorTabularExplainer(
     X_train,X, classifier.predict,
    categorical_names=None  # Replace with categorical feature names if applicable
)

# Sample instance for explanation (replace with your data)
instance = [28, 45000, 700, 1800]

# Get the anchor rule for the selected instance
explanation = explainer.explain_instance(X_train, classifier.predict, threshold=0.95)

# Print the anchor rule
print("Anchor Rule for Explanation:")
print(' - '.join(explanation.names()))
print('Precision:', explanation.precision())
print('Coverage:', explanation.coverage())
