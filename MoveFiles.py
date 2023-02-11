import os
import shutil

SourcePath = r"H:\zizo-thesis\upper-limb-motor-functions-data-collection\KinectProject\\"
DestinationPath = r"H:\zizo-thesis\upper-limb-motor-functions-data-preprocessing-evaluation\DataCollected\\"

FilesNames = ["accelerometer.csv", "emg.csv", "gyro.csv", "KinectHandsData.csv", "orientation.csv",
              "orientationEuler.csv"]
FolderNames = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight", "Nine", "Ten", "Eleven",
               "Tweleve", "Thirtheen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
               "Twentyone", "TwentyTwo", "TwentyThree"]

# Determine which folder will be files copied in and set "DestinationPath"
for Folder in FolderNames:
    if os.path.exists(DestinationPath + Folder + '\\' + FilesNames[0]) is False:
        DestinationPath = DestinationPath + Folder + '\\'
        break

# Loop over files and move them
for File in FilesNames:
    SourceFilePath = SourcePath + File
    DestinationFilePath = DestinationPath + File
    shutil.move(SourceFilePath, DestinationFilePath)
