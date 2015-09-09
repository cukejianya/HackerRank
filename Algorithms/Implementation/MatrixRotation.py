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
    for circle in range(matrix_length//2):
        print 'round:', circle
        print 'before:', matrix
        if not circle == 0:
            del matrix[0]
            del matrix[-1]
            print 'del row', matrix
            if matrix:
                matrix_length = len(matrix)
                row_length = len(matrix[0])
            if not matrix or not matrix[0]:
                continue

        left_array = []
        right_array = []
        for idx, row in enumerate(matrix):
            if not idx == 0:
                if not idx == matrix_length-1:
                    right_array.append(row.pop())
                    row.reverse()
                    left_array.append(row.pop())
                    row.reverse()
                else:
                    matrix[0] += right_array
                    matrix[0] += row[::-1]
                    matrix[0] += left_array[::-1]

            print '--matrix--'
            for row in matrix:
                 print row

        new_matrix.append(matrix[0])
        print 'new matrix:\n', new_matrix
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
    diff = 2
    print 'rotate:\n', rotate
    for idx in range(matrix_length/2):
        print '--row length...', row_length
        print '--matrix length...', matrix_length
        if not row_length == 0:
            reformat.append(rotate[idx][0:row_length])
            rotate[idx] = rotate[idx][row_length::]
        right_array = rotate[idx][0:matrix_length-2]
        rotate[idx] = rotate[idx][matrix_length-2::]
        if not row_length == 0:
            reformat.append(rotate[idx][0:row_length][::-1])
            rotate[idx] = rotate[idx][row_length::]
        left_array = rotate[idx]

        top = reformat[-2]
        bottom = reformat[-1]
        for j in range(idx)[::-1]:
            # print top
            # print bottom
            top = [rotate[j][1].pop()]+top
            bottom = bottom+[rotate[j][0].pop()]

            rotate[j][0].reverse()
            rotate[j][1].reverse()

            top = top+[rotate[j][0].pop()]
            bottom = [rotate[j][1].pop()]+bottom

            rotate[j][0].reverse()
            rotate[j][1].reverse()
            # print top
            # print bottom

        reformat[-2] = top
        reformat[-1] = bottom

        rotate[idx] = [right_array, left_array]
        row_length -= 2
        matrix_length -= 2
        # print 'rotate: \n',rotate
        # print 'reformat:\n',reformat


    return reformat[::2]+reformat[1::2][::-1]
    # print reformat



for row in reformat_matrix(rotate_matrix(transform_matrix(matrix, M, N), R), M, N):
    print " ".join(row)
