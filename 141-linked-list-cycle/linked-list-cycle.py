class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize the two pointers
        slow, fast = head, head

        # Traverse the list with the two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move the slow pointer one step
            fast = fast.next.next  # Move the fast pointer two steps

            # If there's a cycle, the two pointers will meet
            if slow == fast:
                return True

        # If the fast pointer reaches the end, there's no cycle
        return False