"""
https://github.com/eugenechevski
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: [] 

Constraints:
    * k == lists.length
    * 0 <= k <= 10^4
    * 0 <= lists[i].length <= 500
    * -10^4 <= lists[i][j] <= 10^4
    * lists[i] is sorted in ascending order.
    * The sum of lists[i].length will not exceed 10^4.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    Divide and Conquer: split the list into halves and merge all sub-parts
    Time Complexity: O(N log k)
    Space Complexity: O(1)

    My solution uses recursion which is inherently slower due to return statements.
    It can be optimized with an iterative approach.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        return self.splitAndMerge(0, len(lists) - 1, lists)

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1:
            head.next = list1
        elif list2:
            head.next = list2

        return dummy.next

    def splitAndMerge(self, start: int, end: int, lists: Lis[Optional[ListNode]]) -> ListNode:
        if start == end:
            return lists[start]

        if start + 1 == end:
            return self.mergeTwoLists(lists[start], lists[end])

        half = start + (end - start) // 2

        return self.mergeTwoLists(self.splitAndMerge(start, half - 1, lists), self.splitAndMerge(half, end, lists))
