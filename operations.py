a=[[1,2,3],[4,5,6]]
b=[[5,6],[7,8]]
c=[[1,2,3],[4,5,6],[7,8,9]]
d=[[0,6],[7,8]]
e=[[1,2,3,4],[5,6,7,8],[10,10,11,12],[14,14,15,16]]
f=[[1, 2, 3, 1, 0, 0], [4, 5, 6, 0, 1, 0], [7, 8, 9, 0, 0, 1]]


# transpose of a matrix
def transpose(matrix): return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


# return row
def row(matrix,row_number): return matrix[row_number]


# return column
def col(matrix,col_number): return [matrix[i][col_number] for i in range(len(matrix))]


# identity matrix
def identity(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


# matrix multiplication
def m_multiply(a, b):
    if len(a[0]) != len(b):
        return False
    else:
        return [
            [sum(row(a,i)[_]*col(b,j)[_] for _ in range(len(a[0]))) for j in range(len(b[0]))] for i in range(len(a))
            ]


# matrix exponentiation
def m_power(matrix, n):
    if n >= 0:
        if len(matrix) != len(matrix[0]):
            return False
        if n == 0:
            return identity(len(matrix))
        else:
            return m_multiply(matrix, m_power(matrix, n-1))
    else:
        if len(matrix) != len(matrix[0]):
            return False
        if n == 0:
            return identity(len(matrix))
        else:
            return m_multiply(matrix, m_power(inverse(matrix), n+1))


# elementary operations
def swap(matrix, row_1, row_2):
    temp = matrix[row_2]
    matrix[row_2] = matrix[row_1]
    matrix[row_1] = temp
    return 0


def add_multiple(matrix, row_1, factor, row_2):
    matrix[row_2] = [matrix[row_1][i]*factor+matrix[row_2][i] for i in range(len(matrix[row_1]))]
    return 0


def multiply_const(matrix, row_1, factor):
    matrix[row_1] = [i*factor for i in matrix[row_1]]
    return 0


# reduction
def ref(matrix):
    for row_number in range(len(matrix)):
        temp_pivot_row = 0
        while temp_pivot_row < len(matrix[0]) and matrix[row_number][temp_pivot_row] == 0:
            temp_pivot_row += 1
        if temp_pivot_row == len(matrix[0]):
            row_number += 1
        else:
            swap(matrix, row_number, temp_pivot_row)
            for lower_row_nums in range(row_number+1, len(matrix)): # iterate columns below
                add_multiple(matrix,row_number,-matrix[lower_row_nums][row_number]/matrix[row_number][row_number],lower_row_nums)
            multiply_const(matrix, row_number, 1/matrix[row_number][row_number])
    return matrix


def rref(matrix):
    for row_number in range(min(len(matrix),len(matrix[0]))):
        temp_pivot_row = 0
        while temp_pivot_row < len(matrix[0]) and matrix[row_number][temp_pivot_row] == 0:
            temp_pivot_row += 1
        if temp_pivot_row == len(matrix[0]):
            row_number += 1
        else:
            swap(matrix, row_number, temp_pivot_row)
            if matrix[row_number][row_number] != 0:
                multiply_const(matrix, row_number, 1/matrix[row_number][row_number])

            for lower_row_nums in range(0, row_number): # iterate columns above
                if matrix[row_number][row_number] != 0:
                    add_multiple(matrix,row_number, -matrix[lower_row_nums][row_number],lower_row_nums)

            for lower_row_nums in range(row_number+1, len(matrix)): # iterate columns below
                if matrix[row_number][row_number] != 0:
                    add_multiple(matrix,row_number, -matrix[lower_row_nums][row_number],lower_row_nums)
        #print(matrix)
    return matrix

# determinant
def det(matrix):
    if len(matrix)!=len(matrix[0]):
        return False
    det_scale = 1
    deter = 1
    for row_number in range(len(matrix)):
        temp_pivot_row = 0
        while temp_pivot_row < len(matrix[0]) and matrix[row_number][temp_pivot_row] == 0:
            temp_pivot_row += 1
        if temp_pivot_row == len(matrix[0]):
            row_number += 1
        else:
            if row_number != temp_pivot_row:
                swap(matrix, row_number, temp_pivot_row)
                det_scale *= -1
            if matrix[row_number][row_number] != 0:
                multiply_const(matrix, row_number, 1/matrix[row_number][row_number])
                det_scale *= 1/matrix[row_number][row_number]

            for lower_row_nums in range(0, row_number): # iterate columns above
                if matrix[row_number][row_number] != 0:
                    add_multiple(matrix,row_number, -matrix[lower_row_nums][row_number],lower_row_nums)
    for a in range(len(matrix)):
        deter *= matrix[a][a]
    deter *= det_scale
    return deter

def inverse(matrix):
    temp_matrix = [matrix[i]+identity(len(matrix))[i] for i in range(len(matrix))]
    rref(temp_matrix)
    temp_matrix = [temp_matrix[i][len(temp_matrix):][:len(temp_matrix)] for i in range(len(temp_matrix))] #this line of code needs to be fixed for elegance sigh
    return temp_matrix
#print(a)
#print(col(a,1))


invertible_square_matrix_a=[[1,3,5,1,0,0],[7,11,13,0,1,0],[17,19,23,0,0,1]]
invertible_square_matrix_b=[[1,-3,5],[2,-1,8],[4,2,9]]
rectangular_matrix_4_3_f=[[-8,-6,5],[2,3,6],[-10,8,4],[8,4,-5]]

#print(inverse(invertible_square_matrix_a))
#add_multiple(a,0,2,1)
#multiply_const(a,0,5)
#print(m_power(b,4))
