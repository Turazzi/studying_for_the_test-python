#The function returns the identity matrix

def mat_identity(n):
    mat = []
    identity = 0
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        line[identity] = 1
        identity += 1
        mat.append(line)
    return mat
n = int(input("Enter the number of lines and columns of the matrix: "))

print(mat_identity(n))