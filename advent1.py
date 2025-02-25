import time

def read_data(filename):
    list1 = []; list2 = []
    with open(filename, "r") as file:
        for line in file:
            datum1, datum2 = line.strip().split()
            list1.append(int(datum1))
            list2.append(int(datum2))
    return list1, list2


if __name__ == '__main__':
    filename = 'data1.txt'
    list1, list2 = read_data(filename)
    result = []
    total = 0
    start = time.time()
    for number1 in list1:
        total += list2.count(number1)*number1
    print(total)
    end = time.time()
    print(end-start)
