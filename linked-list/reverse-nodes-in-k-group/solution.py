"""
https://github.com/eugenechevski
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    * The number of nodes in the list is n.
    * 1 <= k <= n <= 5000
    * 0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        """
        Reverse the pointers between every k nodes. Make the last node from the previous slot 
        point to the first node in the current slot.
        """

        # Get the new head
        i = 0
        new_head = head
        while new_head.next and i < k - 1:
            new_head = new_head.next
            i += 1

        current_slot = head
        prev_last = None

        while current_slot:
            # Iterate until the kth node
            i = 0
            current = current_slot
            while current.next and i < k - 1:
                current = current.next
                i += 1

            # Connect the previous slot
            if prev_last and i == k - 1:  # The current slot can be reversed
                prev_last.next = current  # Point to the last
            elif prev_last:  # The left-out nodes cannot be reversed
                prev_last.next = current_slot  # Point to the first

            # The first node of the slot will be the last node
            # after reverse
            prev_last = current_slot

            # Reverse the links between the nodes in the current slot
            next_slot = current.next
            if i == k - 1:
                i = 0
                prev = None
                current = current_slot
                while i < k:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                    i += 1

            current_slot = next_slot

        return new_head
