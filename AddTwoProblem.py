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
        
        d = {}

        p = l1
        count = 0
        dkey = 1
        while p.next:
          d[dkey] = (10**count)*p.val
          count += 1
          dkey += 1
          p = p.next

        d[dkey] = (10**count)*p.val

        count = 0
        dkey += 1
        p = l2
        while p.next:
          d[dkey] = (10**count)*p.val
          count += 1
          dkey += 1
          p = p.next

        d[dkey] = (10**count)*p.val

        result = sum(d.values())

        result_list = [i for i in str(result)]

        # Alternate method for single digit extraction
        # import math
        # result_list = [(ret//(10**i))%10 for i in range(math.ceil(math.log(ret, 10))-1, -1, -1)]

        node = ListNode(result_list[-1])
        curr = node
        
        for i in range(len(result_list)-2, -1, -1):
            curr.next = ListNode(result_list[i])
            curr = curr.next
            
        curr.next = None
        
        return node