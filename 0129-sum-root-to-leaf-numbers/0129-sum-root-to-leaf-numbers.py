class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, num):
            if root is None: return 0 
            num = num * 10 + root.val
            if root.left is None and root.right is None:
                return num
            return dfs(root.left, num) + dfs(root.right, num)
            
        return dfs(root, 0)