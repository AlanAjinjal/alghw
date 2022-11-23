# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Сложность : O(n)

class Solution(object):
    def maxProfit(self, prices):
        res = 0                                     # Начальное значение результат равно нулю
        for i in range(1, len(prices)):             # Для каждого значения начиная со второго
            if prices[i] > prices[i - 1]:           # Если знаечние больше предыдущего
                res += prices[i] - prices[i - 1]    # Прибавляем разницу значений к финальному результату
        return res                                  # Возвращаем результат
