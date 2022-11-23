# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Сложность: O(n)

class Solution:
    def rob(self, nums):
        a = b = c = d = 0                                                       # Создаем переменные по умолчанию равные нулю
        for i in range(len(nums)-1):                                            # Для каждого значения до предпоследнего
            a, c, b, d = b, d, max(b, a + nums[i]), max(d, c + nums[i+1])       # Перезаписываем переменные заменяя их значения соответствующими значениями далее по списку.
        return max(b, d, nums[0])                                               # Возвращаем максимальное значение и трех последних.                         