"""
https://github.com/cherokee-rose
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
    
Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]

Constraints:
    * The number of nodes in the list is in the range [1, 5 * 104].
    * 1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # The idea is to split the given list into two portions
        # Then, reverse the second portion.
        # Then, merge the two portions, so each node from the left
        # portion points to the corresponding node of the right portion,
        # and the node from the right portion points to the next node of the
        # left portion.

        # Split the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second portion
        second = slow.next
        slow.next = None  # Break the link
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge two lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    def extraMemorySolution(self, head: Optional[ListNode]) -> None:
        stack = []

        while head:
            stack.append(head)
            head = head.next

        left, right = 0, len(stack) - 1
        while left + 1 < right:
            stack[left].next = stack[right]
            stack[right].next = stack[left + 1]
            left += 1
            right -= 1

        if left == right:
            stack[left].next = None
        else:
            stack[left].next = stack[right]
            stack[right].next = None
