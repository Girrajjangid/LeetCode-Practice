# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curt = dummy
        counter = 0
        while curt.next:
            counter+=1
            curt = curt.next
        counter_ = 0
        while dummy.next:
            if counter_>counter//2: break
            counter_+=1
            dummy = dummy.next   
        return dummy