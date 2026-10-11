# 1. Write a custom function `celsius_converter(f_temp)` that takes a Fahrenheit string/float, converts it to Celsius, and rounds it to two decimal places using `round()`.
# 2. Write a custom function `parse_and_clean(line)` that takes a single string line. 
# It must split the string by the `|` delimiter, strip away excess whitespace, and check for missing data. 
# If the line is structurally corrupted or the `Sensor_Status` is anything other than `ACTIVE`, the function should return `None`.

def celsius_converter(f_temp):
    try:
        f_temp = float(f_temp)
    except (ValueError, TypeError):
        return None

    c_temp = (f_temp - 32) * 5 / 9
    return round(c_temp, 2)

def parse_and_clean