import numpy as np

import csv
import math
import math

def read_matrix(path: str):
    matrix = []
    with open(path, 'r') as fp:
        for i in fp.readlines():
            row = i.split()
            row = list(map(int, row))
            matrix.append(row)
    #print(matrix)
    return matrix



if __name__ == "__main__":
    matrix1 = np.squeeze(read_matrix("C:\\Users\\Senya\\Desktop\\PPlab1\\data1.txt"))
    matrix2 = np.squeeze(read_matrix("C:\\Users\\Senya\\Desktop\\PPlab1\\data2.txt"))
    matrixres = np.dot(matrix1, matrix2)
    #print("Matrix mul by Py:\n ",matrixres)
    matrixcres = np.array(read_matrix("C:\\Users\\Senya\\Desktop\\PPlab1\\result.txt"))
    #print("Matrix mul by C:\n ",matrixcres)
    print(np.array_equal(matrixres, matrixcres))
