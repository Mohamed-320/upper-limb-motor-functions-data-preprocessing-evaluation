import csv
import os
import Calculations as CLC
import matplotlib.pyplot as plt
import scipy.signal

###################################################################
########### Determine Which folder to get data from  ##############
###################################################################
#Source Folder to import Data from
MainSourceFolder = r"D:\Work\Masters\Thesis\Third trial\Data Collected\\"
MainSubfolder   = "Third Collection"
DataCategory = ["Fully", "Partially", "No movement"]
SampleNumber = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Nine", "Ten", "Eleven", "Tweleve", "Thirtheen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Twentyone", "TwentyTwo", "TwentyThree"]

#Fully = 0, partially =1, No movement =2
DataCategoryIndex = 0
SampleNumberIndex = 0

KinectDataSource        = MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + SampleNumber[SampleNumberIndex] + '\\' + "KinectHandsData.csv"
AccelerometerDataSource = MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + SampleNumber[SampleNumberIndex] + '\\' + "accelerometer.csv"


###################################################################
######## Import Data from CSV to String Arrays    #################
###################################################################
# Open FIles
KinectData = csv.reader(open(KinectDataSource),  delimiter=",")
AccelerometerData = csv.reader(open(AccelerometerDataSource),  delimiter=",")

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
    column10.append(Column[9])
    column11.append(Column[10])
    column12.append(Column[11])
    column13.append(Column[12])
    column18.append(Column[13])
    column19.append(Column[14])
    column20.append(Column[15])
    column21.append(Column[16])
    column22.append(Column[17])
    column23.append(Column[18])

# Skip First row
next(AccelerometerData)

for Column in AccelerometerData:
    column14.append(Column[0])
    column15.append(Column[1])
    column16.append(Column[2])
    column17.append(Column[3])

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
REZ = CLC.ConvertStrArrayToDouble(column10)
RWX = CLC.ConvertStrArrayToDouble(column11)
RWY = CLC.ConvertStrArrayToDouble(column12)
RWZ = CLC.ConvertStrArrayToDouble(column13)
LSX = CLC.ConvertStrArrayToDouble(column18)
LSY = CLC.ConvertStrArrayToDouble(column19)
LSZ = CLC.ConvertStrArrayToDouble(column20)
SCX = CLC.ConvertStrArrayToDouble(column21)
SCY = CLC.ConvertStrArrayToDouble(column22)
SCZ = CLC.ConvertStrArrayToDouble(column23)

AccX = CLC.ConvertStrArrayToDouble(column15)
AccY = CLC.ConvertStrArrayToDouble(column16)
AccZ = CLC.ConvertStrArrayToDouble(column17)

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

RHX = scipy.signal.medfilt(RHX, 3)
RHY = scipy.signal.medfilt(RHY, 3)
RHZ = scipy.signal.medfilt(RHZ, 3)
RSX = scipy.signal.medfilt(RSX, 3)
RSY = scipy.signal.medfilt(RSY, 3)
RSZ = scipy.signal.medfilt(RSZ, 3)
REX = scipy.signal.medfilt(REX, 3)
REY = scipy.signal.medfilt(REY, 3)
REZ = scipy.signal.medfilt(REZ, 3)
RWX = scipy.signal.medfilt(RWX, 3)
RWY = scipy.signal.medfilt(RWY, 3)
RWZ = scipy.signal.medfilt(RWZ, 3)
LSX = scipy.signal.medfilt(LSX, 3)
LSY = scipy.signal.medfilt(LSY, 3)
LSZ = scipy.signal.medfilt(LSZ, 3)
SCX = scipy.signal.medfilt(SCX, 3)
SCY = scipy.signal.medfilt(SCY, 3)
SCZ = scipy.signal.medfilt(SCZ, 3)

AccX = scipy.signal.medfilt(AccX, 3)
AccY = scipy.signal.medfilt(AccY, 3)
AccZ = scipy.signal.medfilt(AccZ, 3)

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


###################################################################
##############   Writing Features To CSV File   ###################
###################################################################

headerROM = ['ROMRHX', 'ROMRHY', 'ROMRHZ', 'ROMREX', 'ROMREY', 'ROMREZ', 'ROMRWX', 'ROMRWY', 'ROMRWZ']
valuesROM = [ROMRHX, ROMRHY, ROMRHZ, ROMREX, ROMREY, ROMREZ, ROMRWX, ROMRWY, ROMRWZ]

headerCompensation = ['RSX', 'RSY', 'RSZ', 'LSX', 'LSY', 'LSZ', 'SCX', 'SCY', 'SCZ']
valuesCompensation = [RSX, RSY, RSZ, LSX, LSY, LSZ, SCX, SCY, SCZ]

headerSmoothness = ['MaxAccX', 'OscAccX', 'MaxAccY', 'OscAccY', 'MaxAccZ', 'OscAccZ']
valuesSmoothness = [MaxAccX, OscAccX, MaxAccY, OscAccY, MaxAccZ, OscAccZ]

headerTime = ['TimeOfMovement']
valuesTime = [TimeOfMovement]



# check if file already exists
IsROMFound = os.path.isfile(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\RangeOfMotion.csv")

# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\RangeOfMotion.csv", 'a', newline='')
writer = csv.writer(f)
# if file was just created, Add header
if not IsROMFound:
    writer.writerow(headerROM)

writer.writerow(valuesROM)
f.close()


IsCompensationFound = os.path.isfile(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Compensation.csv")

# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Compensation.csv", 'a', newline='')
writer = csv.writer(f)
# if file was just created, Add header
if not IsCompensationFound:
    writer.writerow(headerCompensation)

writer.writerow(valuesCompensation)
f.close()


IsSmoothnessFound = os.path.isfile(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Smoothness.csv")

# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\Smoothness.csv", 'a', newline='')
writer = csv.writer(f)
# if file was just created, Add header
if not IsSmoothnessFound:
    writer.writerow(headerSmoothness)

writer.writerow(valuesSmoothness)
f.close()


IsTimeFound = os.path.isfile(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\TimeOfMovement.csv")

# write to CSV file
f = open(r"D:\Work\Masters\Thesis\Third trial\DataPreProcessing\TimeOfMovement.csv", 'a', newline='')
writer = csv.writer(f)
# if file was just created, Add header
if not IsTimeFound:
    writer.writerow(headerTime)

writer.writerow(valuesTime)
f.close()

###################################################################
###################################################################
###################################################################
