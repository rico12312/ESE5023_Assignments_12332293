import random
#build matrices
row, column = 5, 10
a = []
for i in range(row):
    b = []
    for j in range(column):
        b.append(random.randint(0,50))
    a.append(b)
    del b

row, column = 10,5
c=[]
for i in range(row):
    b=[]
    for j in range(column):
        b.append(random.randint(0,50))
    c.append(b)
    del b

#do matrix multiplication
def matrix_multip(a, b):
    if len(a[0]) != len(b):
        print("The matrix multiplication is not possible.")
        return 0

    else:
        row = len(a)
        column = len(b[0])
        result = []
        for i in range(row):
            result.append([])
            for j in range(column):
                result[i].append(0)
                for k in range(len(b)):
                    result[i][j] = result[i][j] + a[i][k] * b[k][j]
        return result

#output
print("The first matrix is:")
for row in a:
    print(row)
print(" ")
print("The second matrix is:")
for row in c:
    print(row)
print(" ")
if matrix_multip(a, c) == 0:
   pass
else:
    print("The result of matrix multiplication is:")
    for row in matrix_multip(a, c):
        print(row)
