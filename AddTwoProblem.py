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
        
        n = m = ''
        
        x = l1
        while x.next:
            n += str(x.val)
            x = x.next
        n += str(x.val)
        
        x = l2
        while x.next:
            m += str(x.val)
            x = x.next
        m += str(x.val)
        
        result = str(int(m[::-1]) + int(n[::-1]))

        node = ListNode(int(result[-1]))
        curr = node
        
        for i in range(len(result)-2, -1, -1):
            curr.next = ListNode(int(result[i]))
            curr = curr.next
            
        curr.next = None
        
        return node