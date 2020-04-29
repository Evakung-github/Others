# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return
      
        def helper(root):
            l,r = [-float('inf'),-float('inf')],[-float('inf'),-float('inf')]

            if not root.left and not root.right:
                #print ([root.val,root.val])
                return [root.val,root.val]
            if root.left:
                l = helper(root.left)
            if root.right:
                r = helper(root.right)
            local_max = root.val+max(l[0],r[0],0)
            global_max = max(l[1],r[1],max(l[0],0)+max(r[0],0)+root.val)
            #print ([local_max,global_max])
                       
            return [local_max,global_max]
        
        ans = helper(root)
        
        return max(ans)
            
