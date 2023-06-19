#Function that returns a matrix with dimensions N and M with all elements equal to zero

def create_matrix(n_lines, n_columns):
    matrix = []
    for i in range(n_lines):
        line = []
        for j in range(n_columns):
            line.append(0)
        matrix.append(line)
    return matrix

n_lines = int(input("Enter the number of lines: "))
n_columns = int(input("Enter the number of columns: "))

print(create_matrix(n_lines, n_columns))