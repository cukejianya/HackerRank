input_list = input().split()
M = int(input_list[0])
N = int(input_list[1])
R = int(input_list[2])

matrix = []
for i in range(M):
    matrix.append(input().split())

def rotate_matrix(matrix, matrix_length, row_length):
    new_matrix = []
    smallest = min(matrix_length, row_length)
    for circle in range(smallest/2):
        new_matrix.append([])
        if not circle == 0:
            del matrix[0]
            del matrix[len(matrix)-1]
            for row in matrix:
                del row[row_length-1]
                del row[0]
            matrix_length = len(matrix)
            if matrix:
                row_length = len(matrix[0])
            else:
                continue

        for i, original_row in enumerate(matrix):
            if i == 0 or i == matrix_length-1:
                row = [x for x in original_row]
                if i == 0:
                    new_matrix[0]+= row
                else:
                    index = matrix_length - 2
                    index = len(new_matrix[0]) - index
                    for x in row[::-1]:
                        new_matrix[0].insert(index, x)
                        index += 1
            else:
                for j, elm in enumerate(original_row):
                    length = len(original_row) - 1
                    length = row_length+length//2
                    if j == 0:
                        new_matrix[0].insert(length, elm)
                    if j == len(original_row) - 1:
                        length += 1
                        new_matrix[0].insert(length, elm)

    return new_matrix
print rotate_matrix(matrix, M, N)
for row in rotate_matrix(matrix, M, N):
    print row
