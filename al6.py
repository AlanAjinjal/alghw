# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = []                   # Создаем пустой массив
        while head:                 # Для каждого элемента
            if head in seen:        # Если элемент есть массиве seen
                return True         # Завершаем цикл, возвращая True
            else:                   # Иначе
                seen.append(head)   # Записыавем элемент как просмотренный
                head = head.next    # переходим к следующему элементу
        return False                # Возвращем False