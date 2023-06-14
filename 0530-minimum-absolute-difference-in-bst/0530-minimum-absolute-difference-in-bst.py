# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        temp1 = None
        mini_d = float('inf')
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                #print(root.val, end=' ')
                if temp1 is not None:
                    mini_d = min(abs(root.val - temp1), mini_d)
                temp1 = root.val
                root = root.right
        return mini_d        