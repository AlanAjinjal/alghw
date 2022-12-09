# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        item, count = head, 0  # По умолчанию выбираем заголовочный элемент, и количество элементов считаем равным 0
        dec = 0                # Десятичное значение по умолчанию равно 0
        
        while(item):           # Для каждого элемента
            count += 1         # Увеличием счетчик на 1
            item = item.next   # переходим к следующем элементу
        
        

        for i in range(count):              # Для каждого значения в диапазоне от 0 до count
            val = head.val                  # Получение значение элемента   
            dec +=  val * 2 ** (count-1-i)  # Высчитываем десятичное значение элемента на данной позиции и прибавляем к основному значению
            head = head.next                #Переходим к следующему значению

        return dec     # Возвращаем результат