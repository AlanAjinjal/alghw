# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reversedhead = None                                     # По умолчанию перевернутый ListNode пуст
        current = head                                          # Выбранный элемент  - head

        while current:                                          # Для каждого элемента в ListNode
            reversedhead = ListNode(current.val, reversedhead)  # Записывыаем в переменную reversed head значение выбранного элемент, указывая следующим, предыдущее значение переменной
            current = current.next                              # Переходим к следующей переменной

        while head:                                             # Для каждого элемента в ListNode
            if reversedhead.val != head.val:                    # Сравниваем его с соответствующим в перевернутой ListNode
                return False                                    # В случае несоответсвия возвращаем False
            reversedhead = reversedhead.next                    # Переходим к следующему элементу в reversedhead
            head = head.next                                    # Переходим к следующему элементу в head

        return True                                             # В случае завершения цикла и соответсвии всех элементов возвращаем True