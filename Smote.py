import numpy
from imblearn.over_sampling import SMOTE
from numpy import genfromtxt, savetxt
from sklearn.datasets import make_classification

# Configuration Defines
number_of_samples_to_be_generated = 100

# Import Data To be resampled
train_data = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted_TrainData.csv",
    skip_header=1, delimiter=',')
X, y = make_classification(n_samples=number_of_samples_to_be_generated, n_features=25, n_redundant=0,
                           n_clusters_per_class=1,
                           weights=[1], flip_y=0, random_state=1, shuffle=False, scale=0)

# Concatenate Train data and randomly generated data
concatenated_data = numpy.concatenate([train_data, X])

# Count Train Data Samples
number_of_train_data_samples = 0
for item in train_data:
    number_of_train_data_samples = number_of_train_data_samples + 1
print('\nNumber of items in TrainData is:', number_of_train_data_samples)

# Create Data Labels
number_of_zeroes = number_of_samples_to_be_generated - number_of_train_data_samples
data_labels = [1] * number_of_train_data_samples + [0] * number_of_samples_to_be_generated

# Smoting The Data
sm = SMOTE()
X_resampled, y_resampled = sm.fit_resample(concatenated_data, data_labels)

# Delete the other class created to smote
delete_counter = 0
for delete_counter in range(number_of_samples_to_be_generated):
    X_resampled = numpy.delete(X_resampled, number_of_train_data_samples, 0)
    delete_counter = delete_counter + 1

# Count Train Data Samples
i = 0
for item in X_resampled:
    i = i + 1
print('\nNumber of items in Resampled Data is:', i)

# print(y)
savetxt(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\Resampled.csv",
        X_resampled, delimiter=",")
savetxt(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\Concatenated.csv",
        concatenated_data, delimiter=",")
