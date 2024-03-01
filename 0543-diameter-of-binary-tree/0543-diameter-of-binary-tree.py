class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = float('-inf')
        def dfs(root):
            nonlocal max_
            if root is None: return -1
            lh = dfs(root.left)
            rh = dfs(root.right)
            max_ = max((2 + lh + rh), max_)
            return 1 + max(lh,rh)
        dfs(root)
        return max_ 