import csv

from numpy import genfromtxt
from sklearn.svm import OneClassSVM

TrainData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\ResampledData.csv",
    skip_header=1,
    delimiter=',')
TestData = genfromtxt(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\FeaturesExtracted_TestData.csv",
    skip_header=1, delimiter=',')
# print(TrainData)

svm = OneClassSVM(kernel='rbf', degree=3, gamma='scale', nu=0.2)
print(svm, "\n")
svm.fit(TrainData)

pred = svm.predict(TestData)
scores = svm.score_samples(TestData)

# x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#
# plt.scatter(x,scores)
# plt.show()

i = 1
for item in scores:
    print("\n Sample", i, "Score is ", item, end=" ")
    i = i + 1

f = open(r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataPreProcessing\Results.csv", 'a',
         newline='')
writer = csv.writer(f)
# writer.writerow(header)
writer.writerow(scores)
f.close()

# j = 1
# for item in scores:
#     print ("\n Sample Number",j)
#     j = j + 1
#     if item > 3:
#         print("Movement Fully Done")
#     elif item > 0 and item < 3:
#         print("Movement Partially Done")
#     else :
#         print("Movement Is Not Done")


# print("\nPredection Scores:\n",pred)
# j = 0
# print ("\nOutlined samples are:")
# for item in pred:
#     j = j + 1
#     if (item == -1):
#         print(j, end =", ")


# thresh = quantile(scores, 0.03)
# print("\n Threshold is \n ",thresh)

# anom_index = where(pred==-1)
# values = x[anom_index]

# for item in anom_index:
#     print("\n Outlined samples are samples number\n", item)

# plt.scatter(x[:,0], x[:,1])
# plt.scatter(values[:,0], values[:,1], color='r')
# plt.show()
