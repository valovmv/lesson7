class Matrix:
    def __init__(self, lt_of_lts):
        len_of_matrix = len(lt_of_lts[0])
        for lt in lt_of_lts:
            if not len(lt) == len_of_matrix:
                raise ValueError("Ошибка ввода данных.")
        self._data = lt_of_lts

    def __str__(self):
        result = f'\n(\t' + f'\t)\n(\t'.join(f', '.join(str(x) for x in line) for line in self._data) + f'\t);'
        return result

    def __add__(self, other):
        len_of_matrix = len(self._data[0])
        hig_of_matrix = len(self._data)
        if not (len_of_matrix == len(other._data[0]) and hig_of_matrix == len(other._data)):
            raise ValueError("Необходимо ввести матрицы одного размера.")
        result = [[self._data[y][x] + other._data[y][x] for x in range(len_of_matrix)]
                  for y in range(hig_of_matrix)]
        return Matrix(result)

matrix = Matrix([[], [], []])
# matrix1 = Matrix([[2, 6], [3, 5], [4, 8]]) для проверки вывода ошибки
matrix1 = Matrix([[2, 6, 7], [3, 5, 9], [4, 8, 1]])
matrix2 = Matrix([[9, -5, 3], [-4, 7, -3], [-2, 5, -1]])
matrix3 = matrix1 + matrix2

print(matrix)
print(matrix1)
print(matrix2)
print(matrix3)
