class Solution:
    def dfs(self, root, side):
        if not root: return
        if not root.left and not root.right: # It is a leave
            if side == -1: self.sum += root.val
        self.dfs(root.left, -1)
        self.dfs(root.right, 1)
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
        