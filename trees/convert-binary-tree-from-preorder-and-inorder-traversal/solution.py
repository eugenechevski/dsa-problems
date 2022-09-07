"""
https://github.com/cherokee-rose
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]

Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    * 1 <= preorder.length <= 3000
    * inorder.length == preorder.length
    * -3000 <= preorder[i], inorder[i] <= 3000
    * preorder and inorder consist of unique values.
    * Each value of inorder also appears in preorder.
    * preorder is guaranteed to be the preorder traversal of the tree.
    * inorder is guaranteed to be the inorder traversal of the tree.
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # Build the map of the indices of the inorder list
        inorder_map = {}
        for i, n in enumerate(inorder):
            inorder_map[n] = i

        # Find the root value's index in the inorder list
        root_index = inorder_map[preorder[0]]
        root = TreeNode(val=preorder[0])
        next_index = 1

        def divideAndConquer(node, start, end, mid):
            nonlocal next_index
            nonlocal inorder_map

            if not node or start == end:
                return

            if start < mid:
                node.left = TreeNode(val=preorder[next_index])
                next_index += 1
                divideAndConquer(node.left, start, mid - 1,
                                 inorder_map[node.left.val])

            if mid < end:
                node.right = TreeNode(val=preorder[next_index])
                next_index += 1
                divideAndConquer(node.right, mid + 1, end,
                                 inorder_map[node.right.val])

        divideAndConquer(root, 0, len(inorder) - 1, root_index)

        return root
