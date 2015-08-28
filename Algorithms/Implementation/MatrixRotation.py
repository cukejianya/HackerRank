input_list = input().split()
M = int(input_list[0])
N = int(input_list[1])
R = int(input_list[2])

matrix = []
for i in range(M):
    matrix.append(input().split())

def transform_matrix(matrix, matrix_length, row_length):

    new_matrix = []
    smallest = min(matrix_length, row_length)
    for circle in range(smallest/2):
        # print 'round:', circle
        # print 'before:', matrix
        if not circle == 0:
            del matrix[0]
            del matrix[-1]
            # print 'del row', matrix
            if matrix:
                for row in matrix:
                    del row[-1]
                    del row[0]
                matrix_length = len(matrix)
                row_length = len(matrix[0])
            if not matrix or not matrix[0]:
                continue

        left_array = []
        right_array = []
        for idx, row in enumerate(matrix):
            if not idx == 0:
                if not idx == matrix_length-1:
                    left_array.append(row[::-1].pop())
                    right_array.append(row.pop())
                else:
                    matrix[0] += right_array
                    matrix[0] += row[::-1]
                    matrix[0] += left_array[::-1]
        new_matrix.append(matrix[0])
        # print new_matrix
    return new_matrix

def rotate_matrix(transform, R):
    for idx, row in enumerate(transform):
        for i in range(R%len(row)):
            transform[idx].append(transform[idx][0])
            del transform[idx][0]
    return transform

def reformat_matrix(rotate, matrix_length, row_length):
    smallest = min(matrix_length, row_length)
    reformat = []
    for idx in range(smallest/2):

        if not idx == 0:
            reformat.append([rotate[idx-1][1].pop()]+rotate[0][0:row_length]+rotate[0][::-1][matrix_length-2:row_length+2])
            print [rotate[idx-1][1].pop()]+rotate[0][0:row_length]+rotate[0][::-1][matrix_length-2:row_length+2]

        else:
            reformat.append(rotate[0][0:row_length])
            reformat.append(rotate[0][::-1][matrix_length-2:row_length+2])

        right_array = rotate[idx][row_length:row_length+matrix_length-2]
        left_array = rotate[idx][::-1][row_length:row_length+matrix_length-2][::-1]
        rotate[idx] = [right_array, left_array]

        row_length -= 2
        matrix_length -= 2

    # print reformat



reformat_matrix(rotate_matrix(transform_matrix(matrix, M, N), R), M, N)
