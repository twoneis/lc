# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        for i in range(0, len(lists)):
            if lists[i] is None:
                lists[i] = float('inf'), i, None
            else:
                lists[i] = lists[i].val, i, lists[i]
        r = None
        c = None
        last = float('inf'), len(lists), None
        heapify(lists)
        while True:
            if last > lists[0]:
                min = heapreplace(lists, last)
            else:
                min = last
            if min[2] is None:
                return r
            if min[2].next is None:
                last = float('inf'), min[1], None
            else:
                last = min[2].next.val, min[1], min[2].next
            n = min[2]
            if r is None:
                r = n
                c = r
                continue
            c.next = n
            c = c.next
