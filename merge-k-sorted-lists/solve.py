# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        r = ListNode()
        init_r = r
        second_last = r
        while True:
            min = 1001
            min_i = -1
            for i in range(0, len(lists)):
                if lists[i] is None:
                    continue
                if lists[i].val < min:
                    min = lists[i].val
                    min_i = i
            if min_i == -1:
                break
            lists[min_i] = lists[min_i].next
            r.val = min
            r.next = ListNode()
            second_last = r
            r = r.next
        if second_last.next is None:
            return None
        second_last.next = None
        return init_r
