string = '0123456789'

matrix = [[number for number in string] for _ in range(10)]

for row in matrix:
    print(row)