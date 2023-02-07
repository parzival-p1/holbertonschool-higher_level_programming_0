#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        squares = []
        for row in matrix:
            squares.append(list(map(lambda x: x * x, row)))
        return (squares)
