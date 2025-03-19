from collections import defaultdict

def read_data(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

lines = read_data('data4.txt')

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))

total = 0
for r, c in char_map['X']:
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        for i, char in enumerate('XMAS'):
            if (r + dr*i, c + dc*i) not in char_map[char]:
                break
        else:
            total += 1

print(total)
