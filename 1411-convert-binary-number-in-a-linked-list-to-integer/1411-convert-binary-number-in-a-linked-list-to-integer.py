class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = ""
        while head:
            l+=str(head.val)
            head = head.next
        return int(l ,2)
