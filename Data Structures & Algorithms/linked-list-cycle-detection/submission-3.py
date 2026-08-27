# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = set()
        current = head

        while current:
            value = current

            if value in h:
                return True

            h.add(value)
            current = current.next
        return False
        