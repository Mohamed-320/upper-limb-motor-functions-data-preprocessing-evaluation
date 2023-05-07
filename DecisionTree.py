# Import required libraries

import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load the training data and the test data
data = pd.read_csv(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted.csv")
fmaScores = pd.read_csv(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\Results.csv")
# print("=======THE TRAINED DATA FOR THE Decision TREE ALGORITHM=======" + trainData)

# Preprocess the data
X = data.dropna(axis=1)
print("the X data includes the kinematic measures for each patient in the preprocessed dataset")
print(X)
y = data['FMAScore']  # fix  Y value issue it should be the targeted value
print("The corresponding Fugl-Meyer scores for each patient in the preprocessed dataset")
print(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
print(y_pred)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Visualize the decision tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.show()
