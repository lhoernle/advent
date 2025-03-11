from collections import defaultdict

def read_data(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data

lines = read_data('test4.txt')

char_map = defaultdict(set)
for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].add((r, c))

for r, c in char_map['X']:
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        print(dr, dc)
