# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
        self.count = 0
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        
        def helper(root):
            
            if not root:
                return
            if root.left:
                helper(root.left)
            
            self.count += 1
            if self.count == k:
                self.ans = root.val
            elif self.count>k:
                return
            
            if root.right:
                helper(root.right)
            
            return
        
        helper(root)
        return self.ans
