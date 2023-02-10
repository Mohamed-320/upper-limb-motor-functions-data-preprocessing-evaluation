import numpy
from imblearn.over_sampling import SMOTE
from numpy import genfromtxt, savetxt
from sklearn.datasets import make_classification

####################################################################################################
################################## configuration Defines  ##########################################
####################################################################################################
NumberOfSamplesToBeGenerated = 100

####################################################################################################
############################# Import Data To be resampled ##########################################
####################################################################################################
TrainData = genfromtxt(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted_TrainData.csv",
                       skip_header=1, delimiter=',')
X, y = make_classification(n_samples=NumberOfSamplesToBeGenerated, n_features=25, n_redundant=0, n_clusters_per_class=1,
                           weights=[1], flip_y=0, random_state=1, shuffle=False, scale=0)

# Concatenate Train data and randomly generated data
ConcatenatedData = numpy.concatenate([TrainData, X])

# Count Train Data Samples
NumberOfTrainDataSamples = 0
for item in TrainData:
    NumberOfTrainDataSamples = NumberOfTrainDataSamples + 1
print('\nNumber of items in TrainData is:', NumberOfTrainDataSamples)

# Create Data Labels
NumberOfZeros = NumberOfSamplesToBeGenerated - NumberOfTrainDataSamples
DataLabels = [1] * NumberOfTrainDataSamples + [0] * NumberOfSamplesToBeGenerated

####################################################################################################
############################ Count Percentage of 1s in the Data Labels #############################
####################################################################################################
# j = 0
# NumberOfOnes = 0
# for item in y:
#     j = j + 1
#     if item == 1:
#         NumberOfOnes = NumberOfOnes + 1
# print ('\nThe number of ones in the Whole Sample is  ' ,(NumberOfOnes/j) * 100, '%')


####################################################################################################
#################################### Smoting The Data ##############################################
####################################################################################################
sm = SMOTE()
X_resampled, y_resampled = sm.fit_resample(ConcatenatedData, DataLabels)

####################################################################################################
######################## Delete the other class created to smote ###################################
####################################################################################################
DeleteCounter = 0
for DeleteCounter in range(NumberOfSamplesToBeGenerated):
    X_resampled = numpy.delete(X_resampled, NumberOfTrainDataSamples, 0)
    DeleteCounter = DeleteCounter + 1

# Count Train Data Samples
i = 0
for item in X_resampled:
    i = i + 1
print('\nNumber of items in Resampled Data is:', i)

# print(y)
savetxt(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Resampled.csv", X_resampled, delimiter=",")
savetxt(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Concatenated.csv", ConcatenatedData, delimiter=",")
# print(y)
