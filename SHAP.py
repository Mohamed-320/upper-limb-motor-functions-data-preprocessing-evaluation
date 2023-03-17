# Import required libraries
import numpy as np
import shap
from sklearn.datasets import make_blobs
from sklearn.svm import OneClassSVM

# TrainData = genfromtxt(
#     r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted.csv",
#     skip_header=1, delimiter=',')
# TestData = genfromtxt(
#     r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\TestData\FirstTrialFeaturesTestData.csv",
#     skip_header=1, delimiter=',')

# Generate some random data for demonstration purposes
X, y = make_blobs(n_samples=100, centers=2, random_state=42)

# Train a One-Class SVM model on the data
svm = OneClassSVM(kernel='linear', nu=0.05)
svm.fit(X)


# Define a function to calculate SHAP values for the One-Class SVM model
def svm_shap_values(X, svm):
    explainer = shap.Explainer(svm.decision_function, X)
    shap_values = explainer(X)
    return shap_values


# Generate some test data for explanation purposes
test_data = np.random.rand(10, 2)

# Calculate SHAP values for the test data
shap_values = svm_shap_values(test_data, svm)

# Print the SHAP values for the first data point
print(shap_values[0])

# Plot the summary plot of SHAP values for the test data
shap.summary_plot(shap_values, test_data)
