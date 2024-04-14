# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode()
        init_r = r
        overflow = 0
        while True:
            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0
            r.val = l1val + l2val + overflow
            print(r.val)
            if (r.val >= 10):
                overflow = 1
                r.val = r.val % 10
            else:
                overflow = 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if (l1 is None and l2 is None and overflow != 1):
                break
            r.next = ListNode() 
            r = r.next
        return init_r
