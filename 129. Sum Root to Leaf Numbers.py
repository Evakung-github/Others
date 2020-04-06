# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0 
        # Using self.ans, then there is no need for return in helper function, which increases efficiency as it takes time to return value.
        self.ans = 0
        def helper(s,root):

            if not root.left and not root.right:
                self.ans += s*10+root.val
                return
            else:
                if root.left:
                    helper(s*10+root.val,root.left)   
                if root.right:
                    helper(s*10+root.val,root.right)
        
        helper(0,root)    
        
        return self.ans
