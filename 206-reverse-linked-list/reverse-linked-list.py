class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, previous and current.
        # Previous will eventually become the new head of the reversed list.
        previous, current = None, head

        # Traverse the list until we reach the end.
        while current:
            # Temporarily store the next node.
            temp = current.next

            # Reverse the 'next' pointer of the current node to point to previous node.
            current.next = previous

            # Move the previous pointer up to the current node.
            previous = current

            # Proceed to the next node in the original list.
            current = temp

        # After the loop, current will be None and previous will be the new head of the reversed list.
        head = previous
        return head