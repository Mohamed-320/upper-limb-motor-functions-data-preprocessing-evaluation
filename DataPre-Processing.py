import csv
import os

import scipy.signal

import Calculations as CLC

###################################################################
########### Determine Which folder to get data from  ##############
###################################################################
# Source Folder to import Data from
MainSourceFolder = r"D:\Work\Masters\Thesis\Third trial\Data Collected\\"
MainSubfolder = "Third Collection"
DataCategory = ["Fully", "Partially", "No movement"]
SampleNumber = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Nine", "Ten", "Eleven",
                "Tweleve", "Thirtheen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
                "Twentyone", "TwentyTwo", "TwentyThree"]

# Fully = 0, partially =1, No movement =2
DataCategoryIndex = 2
SampleNumberIndex = 4

KinectDataSource = MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + SampleNumber[
    SampleNumberIndex] + '\\' + "KinectHandsData.csv"
AccelerometerDataSource = MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + \
                          SampleNumber[SampleNumberIndex] + '\\' + "accelerometer.csv"

print('Processing Data from folder:')
print(
    MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + SampleNumber[SampleNumberIndex])
###################################################################
######## Import Data from CSV to String Arrays    #################
###################################################################
# Open FIles
KinectData = csv.reader(open(KinectDataSource), delimiter=",")
AccelerometerData = csv.reader(open(AccelerometerDataSource), delimiter=",")

# Create arrays to import data into
NumberOfArrays = 23
i = 1
for i in range(NumberOfArrays + 1):
    globals()["column" + str(i)] = []

# Skip First row
next(KinectData)

# Data import
for Column in KinectData:
    column1.append(Column[0])
    column2.append(Column[1])
    column3.append(Column[2])
    column4.append(Column[3])
    column5.append(Column[4])
    column6.append(Column[5])
    column7.append(Column[6])
    column8.append(Column[7])
    column9.append(Column[8])
    column1.append(Column[9])
    column1.append(Column[10])
    column1.append(Column[11])
    column1.append(Column[12])
    column1.append(Column[13])
    column1.append(Column[14])
    column2.append(Column[15])
    column2.append(Column[16])
    column2.append(Column[17])
    column2.append(Column[18])

# Skip First row
next(AccelerometerData)

for Column in AccelerometerData:
    column1.append(Column[0])
    column1.append(Column[1])
    column1.append(Column[2])
    column1.append(Column[3])

###################################################################
#########     Convert String Arrays to Double   ###################
###################################################################

TimeStamp = CLC.ConvertStrArrayToDouble(column1)
# print(column2)
RHX = CLC.ConvertStrArrayToDouble(column2)
RHY = CLC.ConvertStrArrayToDouble(column3)
RHZ = CLC.ConvertStrArrayToDouble(column4)
RSX = CLC.ConvertStrArrayToDouble(column5)
RSY = CLC.ConvertStrArrayToDouble(column6)
RSZ = CLC.ConvertStrArrayToDouble(column7)
REX = CLC.ConvertStrArrayToDouble(column8)
REY = CLC.ConvertStrArrayToDouble(column9)
REZ = CLC.ConvertStrArrayToDouble(column1)
RWX = CLC.ConvertStrArrayToDouble(column1)
RWY = CLC.ConvertStrArrayToDouble(column1)
RWZ = CLC.ConvertStrArrayToDouble(column1)
LSX = CLC.ConvertStrArrayToDouble(column1)
LSY = CLC.ConvertStrArrayToDouble(column1)
LSZ = CLC.ConvertStrArrayToDouble(column2)
SCX = CLC.ConvertStrArrayToDouble(column2)
SCY = CLC.ConvertStrArrayToDouble(column2)
SCZ = CLC.ConvertStrArrayToDouble(column2)

AccX = CLC.ConvertStrArrayToDouble(column1)
AccY = CLC.ConvertStrArrayToDouble(column1)
AccZ = CLC.ConvertStrArrayToDouble(column1)

###################################################################
###############   Signals pre-processing   ########################
###################################################################

# plt.title('Acceleration in Z-axis Preprocessing')
# plt.xlabel('Frames')
# plt.ylabel('Acceleration')
# plt.plot(AccX)
# plt.show()

CLC.RemoveOutOfRange(RHX)
CLC.RemoveOutOfRange(RHY)
CLC.RemoveOutOfRange(RHZ)
CLC.RemoveOutOfRange(RSX)
CLC.RemoveOutOfRange(RSY)
CLC.RemoveOutOfRange(RSZ)
CLC.RemoveOutOfRange(REX)
CLC.RemoveOutOfRange(REY)
CLC.RemoveOutOfRange(REZ)
CLC.RemoveOutOfRange(RWX)
CLC.RemoveOutOfRange(RWY)
CLC.RemoveOutOfRange(RWZ)
CLC.RemoveOutOfRange(LSX)
CLC.RemoveOutOfRange(LSY)
CLC.RemoveOutOfRange(LSZ)
CLC.RemoveOutOfRange(SCX)
CLC.RemoveOutOfRange(SCY)
CLC.RemoveOutOfRange(SCZ)

MedianFilterWindow = 3

RHX = scipy.signal.medfilt(RHX, MedianFilterWindow)
RHY = scipy.signal.medfilt(RHY, MedianFilterWindow)
RHZ = scipy.signal.medfilt(RHZ, MedianFilterWindow)
RSX = scipy.signal.medfilt(RSX, MedianFilterWindow)
RSY = scipy.signal.medfilt(RSY, MedianFilterWindow)
RSZ = scipy.signal.medfilt(RSZ, MedianFilterWindow)
REX = scipy.signal.medfilt(REX, MedianFilterWindow)
REY = scipy.signal.medfilt(REY, MedianFilterWindow)
REZ = scipy.signal.medfilt(REZ, MedianFilterWindow)
RWX = scipy.signal.medfilt(RWX, MedianFilterWindow)
RWY = scipy.signal.medfilt(RWY, MedianFilterWindow)
RWZ = scipy.signal.medfilt(RWZ, MedianFilterWindow)
LSX = scipy.signal.medfilt(LSX, MedianFilterWindow)
LSY = scipy.signal.medfilt(LSY, MedianFilterWindow)
LSZ = scipy.signal.medfilt(LSZ, MedianFilterWindow)
SCX = scipy.signal.medfilt(SCX, MedianFilterWindow)
SCY = scipy.signal.medfilt(SCY, MedianFilterWindow)
SCZ = scipy.signal.medfilt(SCZ, MedianFilterWindow)

AccX = scipy.signal.medfilt(AccX, MedianFilterWindow)
AccY = scipy.signal.medfilt(AccY, MedianFilterWindow)
AccZ = scipy.signal.medfilt(AccZ, MedianFilterWindow)

# plt.title('Acceleration in Z-axis Postprocessing')
# plt.xlabel('Frames')
# plt.ylabel('Acceleration')
# # print(RHX)
# plt.plot(AccX)
# plt.show()


###################################################################
###################   Features Extraction   #######################
###################################################################

ROMRHX = CLC.CalcROM(RHX)
MeanValueRHX = CLC.CalculateMeanValue(RHX)

ROMRHY = CLC.CalcROM(RHY)
MeanValueRHY = CLC.CalculateMeanValue(RHY)

ROMRHZ = CLC.CalcROM(RHZ)
MeanValueRHZ = CLC.CalculateMeanValue(RHZ)

ROMRSX = CLC.CalcROM(RSX)
MeanValueRSX = CLC.CalculateMeanValue(RSX)

ROMRSY = CLC.CalcROM(RSY)
MeanValueRSY = CLC.CalculateMeanValue(RSY)

ROMRSZ = CLC.CalcROM(RSZ)
MeanValueRSZ = CLC.CalculateMeanValue(RSZ)

ROMREX = CLC.CalcROM(REX)
MeanValueREX = CLC.CalculateMeanValue(REX)

ROMREY = CLC.CalcROM(REY)
MeanValueREY = CLC.CalculateMeanValue(REY)

ROMREZ = CLC.CalcROM(REZ)
MeanValueREZ = CLC.CalculateMeanValue(REZ)

ROMRWX = CLC.CalcROM(RWX)
MeanValueRWX = CLC.CalculateMeanValue(RWX)

ROMRWY = CLC.CalcROM(RWY)
MeanValueRWY = CLC.CalculateMeanValue(RWY)

ROMRWZ = CLC.CalcROM(RWZ)
MeanValueRWZ = CLC.CalculateMeanValue(RWZ)

ROMLSX = CLC.CalcROM(LSX)
MeanValueLSX = CLC.CalculateMeanValue(LSX)

ROMLSY = CLC.CalcROM(LSY)
MeanValueLSY = CLC.CalculateMeanValue(LSY)

ROMLSZ = CLC.CalcROM(LSZ)
MeanValueLSZ = CLC.CalculateMeanValue(LSZ)

ROMSCX = CLC.CalcROM(SCX)
MeanValueSCX = CLC.CalculateMeanValue(SCX)

ROMSCY = CLC.CalcROM(SCY)
MeanValueSCY = CLC.CalculateMeanValue(SCY)

ROMSCZ = CLC.CalcROM(SCZ)
MeanValueSCZ = CLC.CalculateMeanValue(SCZ)

MaxAccX = CLC.FindMax(AccX)
ROMAccX = CLC.CalcROM(AccX)
OscAccX = CLC.CalculateOscilliations(AccX)

MaxAccY = CLC.FindMax(AccY)
ROMAccY = CLC.CalcROM(AccY)
OscAccY = CLC.CalculateOscilliations(AccY)

MaxAccZ = CLC.FindMax(AccZ)
ROMAccZ = CLC.CalcROM(AccZ)
OscAccZ = CLC.CalculateOscilliations(AccZ)

# Calculate Time
TimeOfMovement = CLC.CalculateTimeOfMovement(TimeStamp)
print(TimeOfMovement)

###################################################################
##############   Writing Features To CSV File   ###################
###################################################################
headerKinect = ['ROMRHX', 'ROMRHY', 'ROMRHZ', 'ROMRSX', 'ROMRSY', 'ROMRSZ', 'ROMREX', 'ROMREY', 'ROMREZ', 'ROMRWX',
                'ROMRWY', 'ROMRWZ', 'ROMLSX', 'ROMLSY', 'ROMLSZ', 'ROMSCX', 'ROMSCY', 'ROMSCZ', 'MovementTime']
valuesKinect = [ROMRHX, ROMRHY, ROMRHZ, ROMRSX, ROMRSY, ROMRSZ, ROMREX, ROMREY, ROMREZ, ROMRWX, ROMRWY, ROMRWZ, ROMLSX,
                ROMLSY, ROMLSZ, ROMSCX, ROMSCY, ROMSCZ, TimeOfMovement]

headerAcc = ['MaxAccX', 'OscAccX', 'MaxAccY', 'OscAccY', 'MaxAccZ', 'OscAccZ']
valuesAcc = [MaxAccX, OscAccX, MaxAccY, OscAccY, MaxAccZ, OscAccZ]

MotionScore = ['ScoreOfMotion']
ScoreOfMotion = 1

# Create an empty string list to append header's and values to
header = []
values = []

# Append Headers to one empty list 'header'
for item in headerKinect:
    header.append(item)
for item in headerAcc:
    header.append(item)
# for item in MotionScore:
#     header.append(item)

# Append Values to one empty list 'values'
for item in valuesKinect:
    values.append(item)
for item in valuesAcc:
    values.append(item)
# values.append(ScoreOfMotion)


# check if file already exists
IsFileFound = os.path.isfile(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted.csv")

# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\FeaturesExtracted.csv", 'a', newline='')
writer = csv.writer(f)
# if file was just created, Add header
if not IsFileFound:
    writer.writerow(header)

writer.writerow(values)
f.close()

###################################################################
###################################################################
###################################################################
