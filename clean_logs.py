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

line = "2026-10-11 12:00 | 25.5 | ACTIVE"

def parse_and_clean(line):
    cleaned = []
    parsed = line.split("|")

    for x in parsed:
        rm_space = x.strip()
        if rm_space in ("ERROR", "N/A"):
            rm_space = None
        cleaned.append(rm_space)

    if len(cleaned) != 5:
        return None

    if any(x is None or x == "" for x in cleaned):
        return None

    if cleaned[4] != "ACTIVE":
        return None

    return cleaned


if __name__ == "__main__":
    import csv
    from pathlib import Path

    project_dir = Path(__file__).resolve().parent
    input_file = project_dir / "input" / "environmental_raw.txt"
    output_file = project_dir / "output" / "environmental_cleaned.csv"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    rejected_lines = []
    accepted_count = 0

    with open(input_file, "r", encoding="utf-8") as file, \
         open(output_file, "w", newline="", encoding="utf-8") as output:
        next(file, None)

        writer = csv.writer(output)
        writer.writerow([
            "Timestamp", "StationID", "Temp(C)",
            "Humidity(%)", "Sensor_Status"
        ])

        for line in file:
            cleaned_line = parse_and_clean(line)

            if cleaned_line is None:
                rejected_lines.append(line.strip())
                continue

            c_temp = celsius_converter(cleaned_line[2])

            if c_temp is None:
                rejected_lines.append(line.strip())
                continue

            cleaned_line[2] = c_temp
            writer.writerow(cleaned_line)
            accepted_count += 1

    print(f"Valid rows written: {accepted_count}")
    print(f"Corrupted or invalid lines skipped: {len(rejected_lines)}")
    print(f"Cleaned file saved to: {output_file}")
    
