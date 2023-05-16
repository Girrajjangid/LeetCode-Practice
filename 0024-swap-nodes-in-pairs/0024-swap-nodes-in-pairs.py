# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, dummy.next
        while curr and curr.next:
            third  = curr.next.next
            second = curr.next
             
            #reverse the pair
            second.next = curr
            curr.next   = third
            prev.next   = second
            
            # update the pair
            prev, curr = curr, third
        return dummy.next            
        
        