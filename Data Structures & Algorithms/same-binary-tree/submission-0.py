# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_p = []
        res_q = []
        def dfs_p(node):
            if not node:
                res_p.append(None)
                return None
            res_p.append(node.val)
            dfs_p(node.left)
            dfs_p(node.right)

        def dfs_q(node):
            if not node:
                res_q.append(None)
                return None
            res_q.append(node.val)
            dfs_q(node.left)
            dfs_q(node.right)

        dfs_p(p)
        dfs_q(q)
        return res_p == res_q
