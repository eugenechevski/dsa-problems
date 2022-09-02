"""
https://github.com/cherokee-rose
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    * The number of nodes in the tree is in the range [1, 104].
    * -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mySolution(self, root) -> bool:
        isValid = True

        def dfs(node, left_subtree, right_subtree):
            nonlocal isValid
            if not node:
                return
            if isValid and (not node.left or (node.val > node.left.val and (not right_subtree or node.left.val  right_subtree.val))):
                dfs(node.left, node, right_subtree)
            else:
                isValid = False
            if isValid and (not node.right or (node.val < node.right.val and (not left_subtree or left_subtree.val > node.right.val))):
                dfs(node.right, left_subtree, node)
            else:
                isValid = False
        dfs(root, None, None)
        return isValid

    def isValidBST(self, root) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )
        return valid(root, float("-inf"), float("inf"))
