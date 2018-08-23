def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) != len(m2):
        print("Error: Matrix shapes invalid for mult")
        return None
    res_m = [[sum([m1[i][k]*m2[k][j] for k in range(len(m2))]) for j in range(len(m2[0]))] for i in range(len(m1))]
    return res_m
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) == len(m2):
        add_mat = [[i+j for i,j in zip(m1[i],m2[i])] for i in range(len(m1))]
        return add_mat
    print("Error: Matrix shapes invalid for addition")
    return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows_mat , cols_mat = input().split(",")
    read_mat = [input().split(" ") for i in range(int(rows_mat))]
    mat = [[int(j) for j in i] for i in read_mat]
    if int(rows_mat) != len(mat):
        print("Error: Invalid input for the matrix")
        return None
    return mat
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix_1 = read_matrix()
    matrix_2 = read_matrix()
    if matrix_1 != None and matrix_2 != None:
        print(add_matrix(matrix_1, matrix_2))
        print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
