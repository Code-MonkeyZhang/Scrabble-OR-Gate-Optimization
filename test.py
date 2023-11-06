import math

import numpy as np


def word_to_binary_matrix(word):
    # Convert word to binary representation of each letter's ASCII value
    binary_word = ['{:07b}'.format(ord(letter)) for letter in word]

    # Convert each binary string to a list of integers and then to a NumPy array
    matrix = np.array([[int(bit) for bit in binary_str] for binary_str in binary_word])

    return matrix


def count_gate(word):
    matrix = word_to_binary_matrix(word)  # convert it to matrix
    OR_gate_count = 0  # 初始化 OR 门计数器
    for i in range(matrix.shape[1]):  # matrix.shape[1] 是矩阵的列数
        col = matrix[:, i]  # 使用 NumPy 的切片语法来获取所有列的第i个元素, 以此来返回所有列的元素
        ones_count = np.sum(col);  # count # of 1s in the list

        if ones_count not in (0, 1, matrix.shape[0]):
            OR_gate_count += math.ceil(ones_count / 2);

    return OR_gate_count


word = "KOWTOW"
matrix = word_to_binary_matrix(word)

# 打印整个矩阵
print("Matrix:\n", matrix)

count = count_gate(word)

print(matrix[1, :1])
