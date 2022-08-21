"""
https://github.com/cherokee-rose
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    * The number of nodes in the tree is in the range [0, 104].
    * -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution(object):
    def recursiveDFS(self, root):
        if not root:
            return 0

        return 1 + max(self.recursiveDFS(root.left), self.recursiveDFS(root.right))

    def iterativeDFS(self, root):
        max_depth = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                max_depth = max(max_depth, depth)

        return max_depth

    def iterativeBFS(self, root):
        if not root:
            return 0

        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level

    def maxDepth(self, root):
        return self.iterativeDFS(root)
