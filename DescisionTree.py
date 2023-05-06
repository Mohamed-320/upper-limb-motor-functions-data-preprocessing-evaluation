# Import required libraries
import pandas as pd
from numpy import genfromtxt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load the data
# data = pd.read_csv('post-stroke-data.csv')
data = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted.csv",
    skip_header=1, delimiter=',')

# Preprocess the data
# Create a dataset with only one class of data points
# new_df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns, index=df.index)

X = data.drop([1, 2, 3, 4], axis=1)
y = data[1, 2, 3, 4]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Visualize the decision tree
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, filled=True, rounded=True)
plt.show()
