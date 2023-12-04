from functools import reduce


colours = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

result_a = 0
result_b = 0
with open("day2.txt", "r") as infile:
    for line in infile:
        name, game = line.split(":")

        id = int(name.replace("Game", "").strip())

        isValid = True
        cube_counts = {
            "red": [],
            "green": [],
            "blue": [],
        }

        subsets = game.strip().split(";")
        for subset in subsets:
            observations = subset.strip().split(",")
            for observation in observations:
                count, colour = observation.strip().split(" ")
                count = int(count)
                if count > colours[colour]:
                    isValid = False

                cube_counts[colour].append(count)

        if isValid:
            result_a += id

        power = reduce(
            lambda a, b: a * b,
            [max(val) for val in cube_counts.values()],
        )
        result_b += power

print(f"The sum of the IDs of possible games is {result_a}")
print(f"The sum of the power of game sets is {result_b}")
