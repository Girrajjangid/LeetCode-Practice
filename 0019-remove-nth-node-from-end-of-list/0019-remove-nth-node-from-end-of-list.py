# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        stack = []
        count = 0
        while dummy.next:
            count+=1
            stack.append(dummy)
            dummy = dummy.next
        dummy = head
        if count==n:
            return head.next
        while count-n-1 > 0:
            count-=1
            dummy = dummy.next
        dummy.next = dummy.next.next
        return head        