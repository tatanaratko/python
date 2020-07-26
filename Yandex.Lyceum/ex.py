numbers = [1, 10, 1, 6, 4, 10, 4, 2, 2, 1, 10, 1]
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1
print(counts)