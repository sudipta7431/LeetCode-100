'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''


def searchMatrix(self, matrix, target):
    row = len(matrix)
    column = len(matrix[0])

    if len(matrix) == 0:
        return False
        
    start = 0
    end = (row * column) - 1
    while(start <= end):
        mid = (start + end) // 2
        if target == matrix[mid//column][mid%column]:
            return True
        elif target < matrix[mid//column][mid%column]:
            end = mid - 1
        else:
            start = mid + 1
    return False
