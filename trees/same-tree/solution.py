"""
https://github.com/cherokee-rose
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
    * The number of nodes in both trees is in the range [0, 100].
    * -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    # Breadth First Search
    def isSameTree(self, p, q) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            for i in range(len(p_queue)):
                p_node = p_queue.popleft()
                q_node = q_queue.popleft()

                if (not p_node and q_node) or (p_node and not q_node) or \
                   (p_node and q_node and p_node.val != q_node.val):
                    return False
                elif p_node and q_node:
                    p_queue.append(p_node.left)
                    p_queue.append(p_node.right)
                    q_queue.append(q_node.left)
                    q_queue.append(q_node.right)

        return len(p_queue) == len(q_queue) and len(q_queue) == 0
