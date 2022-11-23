# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# Сложность => O(MN)

class Solution(object):
        def countSquares(self, matrix):
            if len(matrix) == 0 or len(matrix[0]) == 0: return 0                            # Для пустой матрицы возвращаем 0
            rows = len(matrix)                                                              # Количество строк в матрице   
            cols = len(matrix[0])                                                           # Количество столбцов в матрице
            tmp = [[0 for _ in range(cols)] for _ in range(rows)]                           # Динамический массив, в котором будут храниться размерности квадратов
            summ = 0                                                                        # Начальное количество квадратов
            for i in range(rows):                                                           # Для каждой строки 
                for j in range(cols):                                                       # Для каждого столбца
                    if matrix[i][j] == 1:                                                   # Если элемент матрицы равен 1
                        if i == 0 or j == 0:                                                # Если элеент находится в первой строке или первом столбце
                            tmp[i][j] = 1                                                   # Записываем размерность равную 1
                        else:                                                               # Иначе
                            tmp[i][j] = min(tmp[i-1][j-1], tmp[i][j-1], tmp[i-1][j]) + 1    # Размерность квадрата на еденицу больше минимального значения из трех граничащих с данной позицией 
                        summ += tmp[i][j]                                                   # Увеличиваем количество квадратов на получененное значение
            return summ                                                                     # Возвращаем результат
        