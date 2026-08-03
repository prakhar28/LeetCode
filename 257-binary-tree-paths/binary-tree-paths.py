# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node, currPath):
            if node is None:
                return

            path = currPath + str(node.val) if not currPath else currPath + "->" + str(node.val)
            
            if node.left is None and node.right is None:
                result.append(path)
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return result
        