# You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.
# A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1.
# The first day of the period is exempted from this rule.
# Return the number of smooth descent periods.

# Сложность: O(n)


class Solution(object):
    def getDescentPeriods(self, prices):
        d = [1] * len(prices)                   # Генерируем массив того же рамера что и prices, заполненный единицами
        for i in range(1, len(prices)):         # Для каждого элемента со второго
            if prices[i] == prices[i - 1] - 1:  # Если разность элемента с предыдущим равна единице
                d[i] += d[i - 1]                # Записываем его в новый массив
        return sum(d)                           # Возвращаем сумму елемента нового массива