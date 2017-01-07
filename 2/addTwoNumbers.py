# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sum = l1.val + l2.val
        if sum >= 10:
            sum -= 10
            add = True
        else:
            add = False

        result = ListNode(sum)
        head = result
        l1 = l1.next
        l2 = l2.next

        while True:
            if not l1 or not l2:
                break

            sum = l1.val + l2.val
            if add:
                sum += 1
                add = False
            if sum >= 10:
                add = True
                sum -= 10

            result.next = ListNode(sum)
            result = result.next
            l1 = l1.next
            l2 = l2.next

        if l2:
            while l2:
                if add:
                    sum = l2.val + 1
                    add = False
                else:
                    sum = l2.val
                
                result.next = ListNode(sum)
                result = result.next
                l2 = l2.next
        
        elif l1:
            while l1:
                if add:
                    sum = l1.val + 1
                    add = False

                else:
                    sum = l1.val
                
                result.next = ListNode(sum)
                result = result.next
                l1 = l1.next
        return head
            