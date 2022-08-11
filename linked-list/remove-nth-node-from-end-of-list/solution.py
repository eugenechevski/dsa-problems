"""
https://github.com/cherokee-rose
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    
Example 2:
    Input: head = [1], n = 1
    Output: []
    
Example 3:
    Input: head = [1,2], n = 1
    Output: [1]
 
Constraints:
    * The number of nodes in the list is sz.
    * 1 <= sz <= 30
    * 0 <= Node.val <= 100
    * 1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> 1 -> 2 -> 3 -> 4 -> 5 -> 1 -> 2 -> 3 -> 4 -> 5
        # set pointer at nth node
        # set pointer at head
        # update pointers until the node ahead is null
        # keep track of the previous node
        ahead = head
        current = head
        prev = None

        # Move the frontrunner to the nth node
        i = 0
        while i < n:
            ahead = ahead.next
            i += 1

        # Tug alone both nodes
        while ahead:
            ahead = ahead.next
            prev = current
            current = current.next

        if prev:
            prev.next = current.next
        else:
            head = head.next

        return head
