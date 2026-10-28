# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        hash_table = set()

        while current:
            
            if current in hash_table:
                return True
            
            hash_table.add(current)
            current = current.next
            
            
        
        return False
        