"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The problem is to copy nodes so that we do not create extra copies
        
        # Interweave nodes
        current = head
        while current:
            temp = current.next
            current.next = Node(current.val, temp, current.random)
            current = temp
        
        # Correct references
        new_head = head.next if head else None
        current = head
        while current and current.next and current.next.next:
            current.next.random = current.next.random.next
            temp = current.next.next
            current.next.next = current.next.next.next
            current.next = temp
            current = current.next
            
        return new_head
        