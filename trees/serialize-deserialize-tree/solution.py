"""
https://github.com/cherokee-rose
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Example 2:
    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized = ""
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    serialized += (" " + str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    serialized += " null"

        print(serialized)

        return serialized.strip()
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(" ")
        root = None if nodes[0] == 'null' else TreeNode(int(nodes[0]))
        queue = deque([root])
        next_child = 1

        while next_child < len(nodes):
            for i in range(len(queue)):
                node = queue.popleft()

                if nodes[next_child] != 'null':
                    node.left = TreeNode(int(nodes[next_child]))
                    queue.append(node.left)

                next_child += 1

                if next_child == len(nodes):
                    break

                if nodes[next_child] != 'null':
                    node.right = TreeNode(int(nodes[next_child]))
                    queue.append(node.right)

                next_child += 1

                if next_child == len(nodes):
                    break

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
