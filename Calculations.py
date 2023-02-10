import math

from Config import MovementStopDetectionTime


def FindMin(Array):
    MinValue = Array[0]
    for Item in Array:
        if Item < MinValue:
            MinValue = Item
    return MinValue


def FindMax(Array):
    MaxValue = Array[0]
    for Item in Array:
        if Item > MaxValue:
            MaxValue = Item
    return MaxValue


def MaxMinusMin(Max, Min):
    max = float(Max)
    min = float(Min)
    if max > min:
        return max - min
    else:
        return min - max


def CalcROM(Array):
    max = FindMax(Array)
    min = FindMin(Array)
    if max > min:
        return max - min
    else:
        return min - max


def ConvertStrArrayToDouble(ArrayName):
    DoubleArray = []
    for item in ArrayName:
        DoubleArray.append(float(item))
    return DoubleArray


def CalculateMeanValue(Array):
    MeanValue = 0.0
    i = 0
    for item in Array:
        MeanValue += Array[i]
        i += 1
    MeanValue = MeanValue / i
    return MeanValue


def CalculateOscilliations(Array):
    difference = 0.0
    SumOfOsc = 0.0
    FirstTimeFlag = 0
    previous = 0.0
    for item in Array:
        if FirstTimeFlag == 0:
            FirstTimeFlag = 1
        else:
            difference = item - previous
            if difference < 0:
                difference = difference * -1

        SumOfOsc = (SumOfOsc + difference)
        previous = item

    return SumOfOsc


def CalculateStdDev(Array):
    StdDev = 0.0
    NumberOfItems = 0

    MeanValue = CalculateMeanValue(Array)

    for item in Array:
        StdDev = StdDev + ((item - MeanValue) ** 2)
        NumberOfItems += 1

    StdDev = StdDev / (NumberOfItems - 1)
    StdDev = math.sqrt(StdDev)

    return StdDev


def RemoveOutOfRange(Array):
    i = 0
    ArrayMean = CalculateMeanValue(Array)
    ArrayStdDev = CalculateStdDev(Array)

    MinValue = ArrayMean - (3 * ArrayStdDev)
    MaxValue = ArrayMean + (3 * ArrayStdDev)

    for item in Array:
        if item > MaxValue or item < MinValue:
            Array[i] = 0
        i += 1


def CreateNumberOfArrays(NumberOfArrays):
    i = 1
    for i in range(NumberOfArrays + 1):
        globals()["column" + str(i)] = []
    return


# return time of movement in Milli seconds
def CalculateTimeOfMovement(Array):
    StartTime = Array[0]
    for Item in Array:
        EndTime = Item

    TimeOfMovement = (EndTime - StartTime)  # Time is calculated in MicroSeconds
    TimeOfMovement = TimeOfMovement - (
            MovementStopDetectionTime * 1000000)  # Time of stoppage detection is subtracted from the time calculated
    TimeOfMovement = TimeOfMovement / 1000  # Time is convereted to MilliSeconds

    return TimeOfMovement
