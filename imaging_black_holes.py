
input = ["00", "01", "00", "11", "00", "11", "11", "00", "11", "00", "10", "00"]
matrix = []
dimension = [2, 3]


#num = input()
#dimension = num.split(" ")

partial_image = 4

for i in range(int(dimension[1])):
    a = []
    matrix.append(a)

count = 0
for i in range(int(partial_image)):
    x = 0
    for i in range(int(dimension[1])):
        matrix[x].append(input[count])
        x += 1
        count += 1


for row in range(int(dimension[1])):
    for column in range(int(partial_image)):
        print(matrix[row][column], end="")
    print()




