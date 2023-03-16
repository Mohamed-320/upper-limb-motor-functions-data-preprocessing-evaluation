import csv

from matplotlib import pyplot as plt
from numpy import genfromtxt, quantile, where
from sklearn.svm import OneClassSVM

TrainData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted.csv",
    skip_header=1, delimiter=',')
TestData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\TestData\FirstTrialFeaturesTestData.csv",
    skip_header=1, delimiter=',')
print(TrainData)

################ Create a one-class SVM model and train it on the dataset ################

# 'rbf' kernel is being used, which stands for radial basis function. This kernel is commonly used in SVMs for non-linear classification problems.
# 'scale' means that the gamma parameter is set to 1 / (n_features * X.var()), where X is the training data.
# nu: The upper bound on the fraction of training errors and the lower bound on the fraction of support vectors.
svm = OneClassSVM(kernel='rbf', degree=3, gamma='scale', nu=0.2)
print(svm, "\n")
svm.fit(TrainData)

prediction = svm.predict(TestData)
scores = svm.score_samples(TestData)

# Create a dataset with only one class of data points
x = [1, 2, 3, 4]
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] "Base Array Values"
plt.scatter(x, scores)
plt.show()

i = 1
for item in scores:
    print("\n Sample", i, "Score is ", item, end=" ")
    i = i + 1

f = open(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\Results.csv",'a', newline='')
writer = csv.writer(f)
# writer.writerow(header)
writer.writerow(scores)
f.close()

j = 1
for item in scores:
    print("\n Sample Number", j)
    j = j + 1
    if item > 3:
        print("Movement Fully Done")
    elif item > 0 and item < 3:
        print("Movement Partially Done")
    else:
        print("No Movement Happened")

print("\nThe prediction scores are:\n", prediction)


j = 0
print("\nOutlier samples are:")
for item in prediction:
    j = j + 1
    if (item == -1):
        print(j, end=", ")

threshold = quantile(scores, 0.03)
print("\n Threshold is: \n ", threshold)

anom_index = where(prediction == -1)
values = x[anom_index]

for item in anom_index:
    print("\n Outlier count: \n", item)

plt.scatter(x[:, 0], x[:, 1])
plt.scatter(values[:, 0], values[:, 1], color='r')
plt.show()
