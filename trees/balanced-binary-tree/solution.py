"""
https://github.com/cherokee-rose
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    * a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

Example 3:
    Input: root = []
    Output: true

Constraints:
    * The number of nodes in the tree is in the range [0, 5000].
    * -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root) -> bool:
        res = True

        def dfs(node, depth):
            nonlocal res
            if not node:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            if abs(left - right) > 1:
                res = False

            return max(left, right)

        dfs(root, 0)

        return res
