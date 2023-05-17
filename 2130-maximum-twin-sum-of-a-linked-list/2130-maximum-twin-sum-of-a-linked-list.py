class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head
        first, second = dummy, dummy
        while second.next.next:
            first, second = first.next, second.next.next
        second_half = first.next
        first, second, third = None, None, second_half
        while third:
            first, second, third = second, third, third.next
            second.next = first
        second_half = second
        max_sum = float('-inf')
        while second_half and head:
            max_sum = max(max_sum, second_half.val + head.val)
            head, second_half = head.next, second_half.next
        return max_sum
        