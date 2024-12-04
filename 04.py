"""
    December 04, 2024

"""
import numpy as np
"""
    Part 01
"""
def check_xmas(array1,i,j):
    xmas_count = 0
    # straight cases
    if i > 2:
        if array1[i-1][j] == "M" and array1[i-2][j] == "A" and array1[i-3][j] == "S":
            xmas_count += 1
    if j > 2:
        if array1[i][j-1] == "M" and array1[i][j-2] == "A" and array1[i][j-3] == "S":
            xmas_count += 1
    if i < array1.shape[0] - 3:
        if array1[i+1][j] == "M" and array1[i+2][j] == "A" and array1[i+3][j] == "S":
            xmas_count += 1
    if j < array1.shape[1] - 3:
        if array1[i][j+1] == "M" and array1[i][j+2] == "A" and array1[i][j+3] == "S":
            xmas_count += 1
# diagonal cases
    if i > 2 and j > 2:
        if array1[i-1][j-1] == "M" and array1[i-2][j-2] == "A" and array1[i-3][j-3] == "S":
            xmas_count += 1
    if i < array1.shape[0] - 3 and j < array1.shape[1] - 3:
        if array1[i+1][j+1] == "M" and array1[i+2][j+2] == "A" and array1[i+3][j+3] == "S":
            xmas_count += 1
    if i > 2 and j < array1.shape[1] - 3:
        if array1[i-1][j+1] == "M" and array1[i-2][j+2] == "A" and array1[i-3][j+3] == "S":
            xmas_count += 1
    if i < array1.shape[0] - 3 and j > 2:
        if array1[i+1][j-1] == "M" and array1[i+2][j-2] == "A" and array1[i+3][j-3] == "S":
            xmas_count += 1

    return xmas_count

def find_xmas(array1):
    xmas_count = 0
    for i in range(array1.shape[0]):
        for j in range(array1.shape[1]):
            if array1[i][j] == "X":
                xmas_count += check_xmas(array1, i, j)

    return xmas_count

"""
    Part 02
"""

def check_cross_mas(array1,i,j):
    cross_mas_count = 0
    # only diagonal cases this time
    # exactly 4 cases
    # the find_cross_mas function won't check the borders so there should be no out of bounds error
    if array1[i-1][j-1] == "M" and array1[i+1][j+1] == "S" and array1[i-1][j+1] == "M" and array1[i+1][j-1] == "S":
        cross_mas_count += 1
    if array1[i-1][j-1] == "M" and array1[i+1][j+1] == "S" and array1[i-1][j+1] == "S" and array1[i+1][j-1] == "M":
        cross_mas_count += 1
    if array1[i-1][j-1] == "S" and array1[i+1][j+1] == "M" and array1[i-1][j+1] == "M" and array1[i+1][j-1] == "S":
        cross_mas_count += 1
    if array1[i-1][j-1] == "S" and array1[i+1][j+1] == "M" and array1[i-1][j+1] == "S" and array1[i+1][j-1] == "M":
        cross_mas_count += 1

    return cross_mas_count


def find_cross_mas(array1):
    cross_mas_count = 0
    for i in range(1,array1.shape[0]-1):
        for j in range(1,array1.shape[1]-1):
            if array1[i][j] == "A":
                cross_mas_count += check_cross_mas(array1, i, j)

    return cross_mas_count

"""
    Using the Functions
"""

if __name__ == '__main__':
    # Getting the String
    file = open('inputs/04.txt', 'r')
    input_str = file.read()
    file.close()

    # Make it an array
    input_list = input_str.strip().split("\n")
    for k in range(len(input_list)):
        input_list[k] = list(input_list[k])
    input_array = np.array(input_list)

    # Call the functions
    print(f"THe number of XMAS is: {find_xmas(input_array)}")
    print(f"The number of \"X-MAS\" is: {find_cross_mas(input_array)}")