# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.

# Сложность: O(n)

class Solution(object):
    def getMaximumGenerated(self, n):
        if n == 0: return 0                                 # Для нулевого n возвращаем ответ равный 0
        nums =[0] * (n + 1)                                 # Генерируем массив из 0 длиной n + 1
        nums[1] = 1                                         # Задаем n[1] значение равное 1
        for i in range(2, n + 1):                           # Для позиций от 2 до n + 1
            if i % 2 == 0:                                  # Если номер позиции четный
                nums[i] = nums[i // 2]                      # Записываем на данной позиции значение с позиции [i // 2]
            else:                                           # Иначе
                nums[i] = nums[i // 2] + nums[i // 2 + 1]   # Записываем на данной позиции сумму знаечний с позиций [i // 2] и [i // 2 + 1]
        return max(nums)                                    # Возвращаемся максимальное значение в списке.