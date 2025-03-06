import re
from math import prod

def read_data(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data

def get_products(text):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    result = re.findall(pattern, text)
    flag = True
    total = 0
    for entry in result:
        match entry:
            case "do()": flag = True
            case "don't()": flag = False
            case _:
                x, y = map(int, entry[4:-1].split(','))
                if flag:
                    total += x * y
    return total

text = read_data("data3.txt")
print(get_products(text))
