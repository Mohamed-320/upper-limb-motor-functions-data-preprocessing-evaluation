import csv
import os

import scipy.signal
from matplotlib import pyplot as plt

import Calculations as CLC

########### Determine Which folder to get data from  ##############
# Source Folder to import Data from
main_src_folder = r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datacollected" + '\\'
main_sub_folder = "first"
data_category = ["Fully", "Partially", "No movement"]
sample_number = ["first", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Nine", "Ten", "Eleven",
                 "Tweleve", "Thirtheen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
                 "Twenty",
                 "Twentyone", "TwentyTwo", "TwentyThree"]

# Fully = 0, partially =1, No movement =2
data_category_index = 0
sample_number_index = 0

# KinectDataSource = MainSourceFolder + MainSubfolder + '\\' + DataCategory[DataCategoryIndex] + '\\' + SampleNumber[
#     SampleNumberIndex] + '\\' + "KinectHandsData.csv"
kinect_data_src = main_src_folder + main_sub_folder + '\\' + "KinectHandsData.csv"
accelerometer_data_src = main_src_folder + main_sub_folder + '\\' + "accelerometer.csv"

print('Processing Data From Folder: ' + main_src_folder + main_sub_folder + '\\')

###### Import Data from CSV to String Arrays ######

# Open Files
kinect_data = csv.reader(open(kinect_data_src), delimiter=",")
accelerometer_data = csv.reader(open(accelerometer_data_src), delimiter=",")

# Create arrays to import data into
number_of_arrays = 23
i = 1
for i in range(number_of_arrays + 1):
    globals()["column" + str(i)] = []

# Skip first row
next(kinect_data)

# Data import
for Column in kinect_data:
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

# Skip first row
next(accelerometer_data)

for Column in accelerometer_data:
    column1.append(Column[0])
    column1.append(Column[1])
    column1.append(Column[2])
    column1.append(Column[3])

#########   Convert String Arrays to Double  #########

time_stamp = CLC.convert_string_array_to_double(column1)
# print(column2)
RHX = CLC.convert_string_array_to_double(column2)
RHY = CLC.convert_string_array_to_double(column3)
RHZ = CLC.convert_string_array_to_double(column4)
RSX = CLC.convert_string_array_to_double(column5)
RSY = CLC.convert_string_array_to_double(column6)
RSZ = CLC.convert_string_array_to_double(column7)
REX = CLC.convert_string_array_to_double(column8)
REY = CLC.convert_string_array_to_double(column9)
REZ = CLC.convert_string_array_to_double(column1)
RWX = CLC.convert_string_array_to_double(column1)
RWY = CLC.convert_string_array_to_double(column1)
RWZ = CLC.convert_string_array_to_double(column1)
LSX = CLC.convert_string_array_to_double(column1)
LSY = CLC.convert_string_array_to_double(column1)
LSZ = CLC.convert_string_array_to_double(column2)
SCX = CLC.convert_string_array_to_double(column2)
SCY = CLC.convert_string_array_to_double(column2)
SCZ = CLC.convert_string_array_to_double(column2)

AccX = CLC.convert_string_array_to_double(column1)
AccY = CLC.convert_string_array_to_double(column1)
AccZ = CLC.convert_string_array_to_double(column1)

###############   Signals pre-processing   ########################

plt.title('Acceleration in Z-axis Preprocessing')
plt.xlabel('Frames')
plt.ylabel('Acceleration')
plt.plot(AccX)
plt.show()

CLC.remove_out_of_range(RHX)
CLC.remove_out_of_range(RHY)
CLC.remove_out_of_range(RHZ)
CLC.remove_out_of_range(RSX)
CLC.remove_out_of_range(RSY)
CLC.remove_out_of_range(RSZ)
CLC.remove_out_of_range(REX)
CLC.remove_out_of_range(REY)
CLC.remove_out_of_range(REZ)
CLC.remove_out_of_range(RWX)
CLC.remove_out_of_range(RWY)
CLC.remove_out_of_range(RWZ)
CLC.remove_out_of_range(LSX)
CLC.remove_out_of_range(LSY)
CLC.remove_out_of_range(LSZ)
CLC.remove_out_of_range(SCX)
CLC.remove_out_of_range(SCY)
CLC.remove_out_of_range(SCZ)

median_filter_window = 3

RHX = scipy.signal.medfilt(RHX, median_filter_window)
RHY = scipy.signal.medfilt(RHY, median_filter_window)
RHZ = scipy.signal.medfilt(RHZ, median_filter_window)
RSX = scipy.signal.medfilt(RSX, median_filter_window)
RSY = scipy.signal.medfilt(RSY, median_filter_window)
RSZ = scipy.signal.medfilt(RSZ, median_filter_window)
REX = scipy.signal.medfilt(REX, median_filter_window)
REY = scipy.signal.medfilt(REY, median_filter_window)
REZ = scipy.signal.medfilt(REZ, median_filter_window)
RWX = scipy.signal.medfilt(RWX, median_filter_window)
RWY = scipy.signal.medfilt(RWY, median_filter_window)
RWZ = scipy.signal.medfilt(RWZ, median_filter_window)
LSX = scipy.signal.medfilt(LSX, median_filter_window)
LSY = scipy.signal.medfilt(LSY, median_filter_window)
LSZ = scipy.signal.medfilt(LSZ, median_filter_window)
SCX = scipy.signal.medfilt(SCX, median_filter_window)
SCY = scipy.signal.medfilt(SCY, median_filter_window)
SCZ = scipy.signal.medfilt(SCZ, median_filter_window)

AccX = scipy.signal.medfilt(AccX, median_filter_window)
AccY = scipy.signal.medfilt(AccY, median_filter_window)
AccZ = scipy.signal.medfilt(AccZ, median_filter_window)

plt.title('Acceleration in Z-axis Postprocessing')
plt.xlabel('Frames')
plt.ylabel('Acceleration')
# print(RHX)
plt.plot(AccX)
plt.show()

###################   Features Extraction   #######################

ROMRHX = CLC.calc_rom(RHX)
MeanValueRHX = CLC.calc_mean_value(RHX)

ROMRHY = CLC.calc_rom(RHY)
MeanValueRHY = CLC.calc_mean_value(RHY)

ROMRHZ = CLC.calc_rom(RHZ)
MeanValueRHZ = CLC.calc_mean_value(RHZ)

ROMRSX = CLC.calc_rom(RSX)
MeanValueRSX = CLC.calc_mean_value(RSX)

ROMRSY = CLC.calc_rom(RSY)
MeanValueRSY = CLC.calc_mean_value(RSY)

ROMRSZ = CLC.calc_rom(RSZ)
MeanValueRSZ = CLC.calc_mean_value(RSZ)

ROMREX = CLC.calc_rom(REX)
MeanValueREX = CLC.calc_mean_value(REX)

ROMREY = CLC.calc_rom(REY)
MeanValueREY = CLC.calc_mean_value(REY)

ROMREZ = CLC.calc_rom(REZ)
MeanValueREZ = CLC.calc_mean_value(REZ)

ROMRWX = CLC.calc_rom(RWX)
MeanValueRWX = CLC.calc_mean_value(RWX)

ROMRWY = CLC.calc_rom(RWY)
MeanValueRWY = CLC.calc_mean_value(RWY)

ROMRWZ = CLC.calc_rom(RWZ)
MeanValueRWZ = CLC.calc_mean_value(RWZ)

ROMLSX = CLC.calc_rom(LSX)
MeanValueLSX = CLC.calc_mean_value(LSX)

ROMLSY = CLC.calc_rom(LSY)
MeanValueLSY = CLC.calc_mean_value(LSY)

ROMLSZ = CLC.calc_rom(LSZ)
MeanValueLSZ = CLC.calc_mean_value(LSZ)

ROMSCX = CLC.calc_rom(SCX)
MeanValueSCX = CLC.calc_mean_value(SCX)

ROMSCY = CLC.calc_rom(SCY)
MeanValueSCY = CLC.calc_mean_value(SCY)

ROMSCZ = CLC.calc_rom(SCZ)
MeanValueSCZ = CLC.calc_mean_value(SCZ)

MaxAccX = CLC.find_max(AccX)
ROMAccX = CLC.calc_rom(AccX)
OscAccX = CLC.calc_oscillations(AccX)

MaxAccY = CLC.find_max(AccY)
ROMAccY = CLC.calc_rom(AccY)
OscAccY = CLC.calc_oscillations(AccY)

MaxAccZ = CLC.find_max(AccZ)
ROMAccZ = CLC.calc_rom(AccZ)
OscAccZ = CLC.calc_oscillations(AccZ)

# Calculate Time
movement_time = CLC.calc_movement_time(time_stamp)
print(movement_time)

##############   Writing Features To CSV File   ###################
kinect_header = ['ROMRHX', 'ROMRHY', 'ROMRHZ', 'ROMRSX', 'ROMRSY', 'ROMRSZ', 'ROMREX', 'ROMREY', 'ROMREZ', 'ROMRWX',
                 'ROMRWY', 'ROMRWZ', 'ROMLSX', 'ROMLSY', 'ROMLSZ', 'ROMSCX', 'ROMSCY', 'ROMSCZ', 'MovementTime']
kinect_values = [ROMRHX, ROMRHY, ROMRHZ, ROMRSX, ROMRSY, ROMRSZ, ROMREX, ROMREY, ROMREZ, ROMRWX, ROMRWY, ROMRWZ, ROMLSX,
                 ROMLSY, ROMLSZ, ROMSCX, ROMSCY, ROMSCZ, movement_time]

accelerometer_header = ['MaxAccX', 'OscAccX', 'MaxAccY', 'OscAccY', 'MaxAccZ', 'OscAccZ']
accelerometer_values = [MaxAccX, OscAccX, MaxAccY, OscAccY, MaxAccZ, OscAccZ]

motion_src = ['ScoreOfMotion']
src_of_motion = 1

# Create an empty string list to append header's and values to
header = []
values = []

# Append Headers to one empty list 'header'
for item in kinect_header:
    header.append(item)
for item in accelerometer_header:
    header.append(item)
# for item in MotionScore:
#     header.append(item)

# Append Values to one empty list 'values'
for item in kinect_values:
    values.append(item)
for item in accelerometer_values:
    values.append(item)
# values.append(ScoreOfMotion)


# Check if file already exists!
is_file_found = os.path.isfile(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\FeaturesExtracted.csv")

# Write into CSV File
f = open(
    r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\datapreprocessing\FeaturesExtracted.csv",
    'a', newline='')
writer = csv.writer(f)
print("======= Pre-Processed Data Are Ready! =======")
# If file was just created, Add header
if not is_file_found:
    writer.writerow(header)

writer.writerow(values)
f.close()
