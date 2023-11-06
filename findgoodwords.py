import math

import numpy as np


def word_to_binary_matrix(word):
    # Convert word to binary representation of each letter's ASCII value
    binary_word = ['{:07b}'.format(ord(letter)) for letter in word]

    # Convert each binary string to a list of integers and then to a NumPy array
    matrix = np.array([[int(bit) for bit in binary_str] for binary_str in binary_word])
    return matrix


# 读取文件中的单词到列表中
def read_words_from_file(filename):
    with open(filename, 'r') as file:
        # 使用 list comprehension 读取每一行，并移除每行的换行符
        return [line.strip() for line in file]


def count_gate(matrix):
    OR_gate_count = 0  # 初始化 OR 门计数器
    for i in range(matrix.shape[1]):  # matrix.shape[1] 是矩阵的列数
        col = matrix[:, i]  # 使用 NumPy 的切片语法来获取所有列的第i个元素, 以此来返回所有列的元素
        ones_count = np.sum(col);  # count # of 1s in the list

        if ones_count not in (0, 1, matrix.shape[0]):
            OR_gate_count += math.ceil(ones_count / 2);

    return OR_gate_count


def main():
    filepath = "../scrabble_words.txt"
    word_list = read_words_from_file(filepath)
    space_rows = np.array([[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]])
    dash_rows = np.array([[1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1]])

    OR_gate_counts = []

    for word in word_list:
        matrix = word_to_binary_matrix(word)  # convert it to matrix
        space_word = np.concatenate((matrix, space_rows), axis=0)
        dash_word = np.concatenate((matrix, dash_rows), axis=0)
        # pick the circuit with less OR gate
        OR_gate_count = max(count_gate(space_word), count_gate(dash_word));
        OR_gate_counts.append((word, OR_gate_count))

        OR_gate_counts.sort(key=lambda x: x[1],reverse=True)

    with open('../max_results.txt', 'w') as file:
        for word, count in OR_gate_counts:
            # 写入数据，每个结果占一行
            file.write(f"{word}: {count}\n")

if __name__ == '__main__':
    main()
