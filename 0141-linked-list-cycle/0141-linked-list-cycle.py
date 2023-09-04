# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        itr = head
        while itr:
            if not d.get(itr,0):
                d[itr] = d.get(itr,1)
                itr = itr.next
            else:
                return True                        
        return False