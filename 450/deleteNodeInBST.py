# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        parent, target = self.searchNode(root, key)
        if target == false:
            return root
        
        if !target.left:
            if parent.left == target:
                parent.left = target.right
            else:
                parent.right = target.right
            return target.right
        elif !target.right:
            if parent.left = target:
                parent.left = target.left
            else:
                parent.right = target.left
            return target.left
        
        node = target.right
        while node.left:
            parent = node
            node = node.left
        target.val = node.val
        if not node.right:
            parent.left = node.right
        else:
            parent.left = None

    def searchNode(self, parent, node, key):
        if not node:
            return false
        if node.val < key:
            self.searchNode(node, node.right, key)
        elif node.val > key:
            self.searchNode(node, node.left, key)
        elif node.val == key:
            return parent, node
