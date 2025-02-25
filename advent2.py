def read_data(filename):
    data_matrix = []
    with open(filename, "r") as file:
        for line in file:
            temp = line.strip().split()
            temp = [int(i) for i in temp]
            data_matrix.append(temp)
    return data_matrix

def strict_inc(A):
    n = len(A)
    for i in range(n-1):
        if A[i+1] <= A[i]:
            return False
    return True

def strict_dec(A):
    n = len(A)
    for i in range(n-1):
        if A[i+1] >= A[i]:
            return False
    return True

def pass_condition(A):
    n = len(A)
    for i in range(n-1):
        if abs(A[i+1] - A[i]) > 3:
            return False
    return True

if __name__ == "__main__":
    filename = "data2.txt"
    data = read_data(filename)
    total = 0
    for row in data:
        if (strict_inc(row) or strict_dec(row)) and pass_condition(row):
            total += 1
    print(total)
