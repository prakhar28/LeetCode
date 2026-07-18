# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])

        if len(queue) < 2:
            return []
        res = []

        while len(queue) > 0:
            currentLevel = []

            for i in range(len(queue)):
                node = queue.popleft()
                currentLevel.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            res.append(currentLevel)
        return res




        