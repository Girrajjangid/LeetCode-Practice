class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        Sum = 0
        def traverse(root):
            nonlocal Sum
            if root is None: return
            traverse(root.right)
            Sum += root.val
            root.val = Sum
            traverse(root.left)
        traverse(root)
        return root