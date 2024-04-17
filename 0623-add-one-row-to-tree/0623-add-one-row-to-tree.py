# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,root)
        
        def dfs(root, dep):
            if root is None: return dep
            if dep==depth-2:
                root.left = TreeNode(val, left=root.left)
                root.right = TreeNode(val, right=root.right)
            return max(dfs(root.left, dep+1), dfs(root.right, dep+1))
        
        dfs(root, 0)
        return root