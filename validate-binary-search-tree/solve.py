# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return self.treelt(root.left, root.val) and self.treegt(root.right, root.val)
        
    
    def treelt(self, root, val):
        if root is None:
            return True
        if root.val >= val:
            return False
        return self.treelt(root.left, val) and self.treelt(root.right, val)

    def treegt(self, root, val):
        if root is None:
            return True
        if root.val <= val:
            return False
        return self.treegt(root.left, val) and self.treegt(root.right, val)
