input_list = input().split()
M = int(input_list[0])
N = int(input_list[1])
R = int(input_list[2])

matrix = []
for i in range(M):
    matrix.append(input().split())

def rotate_matrix(matrix, matrix_length, row_length):
    new_matrix = []
    for i, original_row in enumerate(matrix):
        row = [x for x in original_row]
        maxlen = matrix_length-1
        #print row
        #print matrix[i+1][row_length-1]
        if not i == maxlen:
            del row[0]
            if i < 0:
                row.insert(row_length-2, matrix[i+1][row_length-1])
            else:
                row.append(row_length-2, matrix[i+1][row_length-1])
        print matrix
        #print matrix[i-1][0]
        if not i == 0:
            del row[row_length-1]
            row = [matrix[i-1][0]]+row
        new_matrix.append(row)
    return new_matrix

print matrix
for row in rotate_matrix(matrix, M, N):
    print row
