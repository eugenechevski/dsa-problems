"""
https://github.com/eugenechevski
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    
Example 2:
    Input: list1 = [], list2 = []
    Output: []
    
Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
 
Constraints:
    * The number of nodes in both lists is in the range [0, 50].
    * -100 <= Node.val <= 100
    * Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None

        if list1 != None and list2 == None:
            return list1

        if list1 == None and list2 != None:
            return list2

        head = None
        if list1.val <= list2.val:
            head = list1
        else:
            head = list2

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                while list1.next != None and list1.next.val <= list2.val:
                    list1 = list1.next

                temp = list1.next
                list1.next = list2
                list1 = temp
            elif list2.val < list1.val:
                while list2.next != None and list2.next.val <= list1.val:
                    list2 = list2.next

                temp = list2.next
                list2.next = list1
                list2 = temp

        return head
