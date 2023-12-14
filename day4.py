from collections import defaultdict


def parse_numbers(numbers):
    numbers = filter(lambda a: a != "", numbers.strip().split(" "))
    numbers = set(map(lambda a: int(a), numbers))
    return numbers


accumulated_points = 0

card_counter = defaultdict(int)
with open("day4.txt", "r") as infile:
    for line in infile:
        name, numbers = line.strip().split(": ")
        winning, chosen = numbers.strip().split(" | ")

        winning = parse_numbers(winning)
        chosen = parse_numbers(chosen)

        matching = winning & chosen
        num_matches = len(matching)

        points = (num_matches > 0) * 2 ** (num_matches - 1)
        points = int(points)
        accumulated_points += points

        idx = name.replace("Card", "").strip()
        idx = int(idx)
        card_counter[idx] += 1

        for i in range(1, num_matches + 1):
            card_counter[idx + i] += card_counter[idx]

print(f"The cards are worh {accumulated_points} points in total")
total_cards = sum(v for k, v in card_counter.items())
print(f"There are {total_cards} cards in total")
