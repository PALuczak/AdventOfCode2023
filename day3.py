from functools import reduce
from itertools import product

schematic = []
with open("day3.txt", "r") as infile:
    for line in infile:
        row = []
        for char in line.strip():
            if char.isdigit():
                row.append(int(char))
            elif char != ".":
                row.append("X")
            else:
                row.append(".")
        schematic.append(row)

print(schematic)
height = len(schematic)
width = len(schematic[0])


def bounds_check(i, j):
    y = max(0, min(height - 1, i))
    x = max(0, min(width - 1, j))
    return y, x


result = 0

for i in range(height):
    for j in range(width):
        if schematic[i][j] == "X":
            # check for neighbouring part numbers
            for ox, oy in product([-1, 0, 1], [-1, 0, 1]):
                y, x = bounds_check(i + oy, j + ox)
                # found number
                if schematic[y][x] not in {".", "X", "o"}:
                    # "follow the line" in BOTH directions
                    part_num = []
                    part_num.append(schematic[y][x])
                    for dx in [-1, 1]:
                        xx = x + dx
                        while 0 <= xx < width and schematic[y][xx] not in {".", "X", "o"}:
                            if dx == -1:
                                part_num.insert(0, schematic[y][xx])
                            else:
                                part_num.append(schematic[y][xx])
                            schematic[y][xx] = "o"  # mark as used
                            xx = xx + dx
                    part_num = reduce(lambda a, b: a * 10 + b, part_num)
                    result += part_num
                    # print(part_num)

# TODO: FIXME
print(f"The sum of all of the part numbers in the engine schematic is {result}")
