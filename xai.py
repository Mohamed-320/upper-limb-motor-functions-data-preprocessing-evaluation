import numpy as np
import shap
from numpy import genfromtxt
from sklearn.svm import OneClassSVM

# Load Fugue Meyer dataset
TrainData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted.csv",
    skip_header=1, delimiter=',')
TestData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\TestData\FirstTrialFeaturesTestData.csv",
    skip_header=1, delimiter=',')
X = np.loadtxt("path/to/fugue_meyer.csv", delimiter=",")
y = np.ones(len(X))  # All instances are positive (anomalous)

# Train one-class SVM on normal instances
normal_X = X[y == 1]
svm = OneClassSVM().fit(normal_X)

# Compute SHAP values for test instances
explainer = shap.KernelExplainer(svm.decision_function, normal_X)
test_X = X[:10]  # Example test instances
shap_values = explainer.shap_values(test_X)

# Print SHAP values for each feature for each test instance
for i in range(len(test_X)):
    print("Instance", i + 1)
    for j in range(len(shap_values)):
        print("Feature", j + 1, "SHAP value:", shap_values[j][i])
