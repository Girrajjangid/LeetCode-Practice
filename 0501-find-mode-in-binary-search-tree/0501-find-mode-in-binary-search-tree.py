class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import Counter
        d = {}
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if d.get(root.val, None) is None:
                    d[root.val] = 1
                else:
                    d[root.val] += 1
                root = root.right
        res = []
        last = None
        for idx, val in sorted(Counter(d).items(), key= lambda x: -x[1]):
            #print(idx, val)
            if res:
                if last == val:
                    res.append(idx)
                    last = val
                else:
                    return res
            else:
                res.append(idx)
                last = val
        return res