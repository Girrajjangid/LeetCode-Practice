class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one,two,three = None, None, head
        while three:
            one,two = two, three
            three   = three.next
            two.next = one
        return two