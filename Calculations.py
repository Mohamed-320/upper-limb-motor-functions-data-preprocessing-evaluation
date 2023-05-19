import math

from Config import movement_stop_detection_time


def find_min(array):
    min_value = array[0]
    for item in array:
        if item < min_value:
            min_value = item
    return min_value


def find_max(array):
    max_value = array[0]
    for Item in array:
        if Item > max_value:
            max_value = Item
    return max_value


def max_min_difference(max, min):
    max = float(max)
    min = float(min)
    if max > min:
        return max - min
    else:
        return min - max


# Calculate Range of Motion (ROM)
def calc_rom(array):
    max = find_max(array)
    min = find_min(array)
    if max > min:
        return max - min
    else:
        return min - max


def convert_string_array_to_double(array_name):
    array_of_doubles = []
    for item in array_name:
        array_of_doubles.append(float(item))
    return array_of_doubles


def calc_mean_value(array):
    mean_value = 0.0
    i = 0
    for item in array:
        mean_value += array[i]
        i += 1
    mean_value = mean_value / i
    return mean_value


def calc_oscillations(array):
    difference = 0.0
    sum_of_osc = 0.0
    first_time_flag = 0
    previous = 0.0
    for item in array:
        if first_time_flag == 0:
            first_time_flag = 1
        else:
            difference = item - previous
            if difference < 0:
                difference = difference * -1

        sum_of_osc = (sum_of_osc + difference)
        previous = item
    return sum_of_osc


# Calculate standard deviation
def calc_std_dev(array):
    std_dev = 0.0
    number_of_items = 0
    mean_value = calc_mean_value(array)

    for item in array:
        std_dev = std_dev + ((item - mean_value) ** 2)
        number_of_items += 1

    std_dev = std_dev / (number_of_items - 1)
    std_dev = math.sqrt(std_dev)
    return std_dev


def remove_out_of_range(array):
    i = 0
    array_mean = calc_mean_value(array)
    array_std_dev = calc_std_dev(array)

    min_value = array_mean - (3 * array_std_dev)
    max_value = array_mean + (3 * array_std_dev)

    for item in array:
        if item > max_value or item < min_value:
            array[i] = 0
        i += 1


def create_number_of_arrays(number_of_arrays):
    i = 1
    for i in range(number_of_arrays + 1):
        globals()["column" + str(i)] = []
    return


# return time of movement in Milli seconds
def calc_movement_time(array):
    start_time = array[0]
    for item in array:
        end_time = item

    movement_time = (end_time - start_time)  # Time is calculated in MicroSeconds
    movement_time = movement_time - (
            movement_stop_detection_time * 1000000)  # Time of stoppage detection is subtracted from the time calculated
    movement_time = movement_time / 1000  # Time is converted to MilliSeconds
    return movement_time
