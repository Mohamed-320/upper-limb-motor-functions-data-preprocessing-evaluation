import os
import shutil

src_path = r"H:\zizo-thesis\upper-limb-motor-functions-data-collection\KinectProject\\"
destination_path = r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataCollected\\"

workbook_sheets = ["accelerometer.csv", "emg.csv", "gyro.csv", "KinectHandsData.csv", "orientation.csv",
                   "orientationEuler.csv"]
folders_order = ["first", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Nine", "Ten", "Eleven",
                 "Tweleve", "Thirtheen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
                 "Twenty",
                 "Twentyone", "TwentyTwo", "TwentyThree"]

# Determine which folder will be files copied in and set "DestinationPath"
for folder in folders_order:
    if os.path.exists(destination_path + folder + '\\' + workbook_sheets[0]) is False:
        destination_path = destination_path + folder + '\\'
        break

# Loop over files and move them
for workbook_files in workbook_sheets:
    src_file_path = src_path + workbook_files
    destination_file_path = destination_path + workbook_files
    shutil.move(src_file_path, destination_file_path)
