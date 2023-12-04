import re

replacements = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
pattern = re.compile(
    r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
)

result = 0
with open("day1.txt", "r") as infile:
    for line in infile:
        digits = []

        for match in re.findall(pattern, line):
            if match in replacements:
                digits.append(replacements[match])
            else:
                digits.append(int(match))

        print(line, digits)

        calibration_value = 10 * digits[0] + digits[-1]
        calibration_value = int(calibration_value)
        result += calibration_value

print(f"The sum of all of the calibration values is {result}")
