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

part1 = 0
for r, c in char_map['X']:
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        for i, char in enumerate('XMAS'):
            if (r + dr*i, c + dc*i) not in char_map[char]:
                break
        else:
            part1 += 1

upleft = lambda r, c: (r - 1, c - 1)
upright = lambda r, c: (r - 1, c + 1)
downleft = lambda r, c: (r + 1, c - 1)
downright = lambda r, c: (r + 1, c + 1)

part2 = 0
print(char_map)
for r, c in char_map["A"]:
    if upleft(r, c) in char_map["M"]:
        if downleft(r, c) in char_map["M"] and upright(r, c)


print(f'Part 1: {part1}')
