# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def depth(node):
            if node == None:
                return 0
            
            leftD = depth(node.left)
            rightD = depth(node.right)
            self.maxD = max(self.maxD, leftD + rightD)
            return 1 + max(leftD, rightD)
        
        depth(root)
        return self.maxD