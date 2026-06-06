class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to simplify edge cases
        dummy.next = head
        slow, fast = dummy, head

        # Move fast pointer so that the gap between slow and fast is n nodes apart
        for _ in range(n):
            fast = fast.next

        # Move fast to the end, maintaining the gap
        while fast:
            fast = fast.next
            slow = slow.next

        # Skip the desired node
        slow.next = slow.next.next

        # Return head of the modified list
        return dummy.next
