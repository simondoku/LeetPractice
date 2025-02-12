def spiralMatrix(matrix):
    res = []

    while matrix:
        #add the first element in the matrix to the res
        res += matrix.pop(0)

        #loop through the rest of the rows and pop the last elements
        if matrix  and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))

    return res
matrix = [[1,2,3],[4,5,6], [7,8,9]]
print(spiralMatrix(matrix))