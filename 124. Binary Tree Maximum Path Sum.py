'''
   8
  / \
 4   5

In this subtree, at node which value is 8, its maximum sum value is 8+4+5=17. However, this value could not be further added by its parent node.
Thus, the maximum value that can be transitted to the parent node should also be computed. For this example, the value is 8+5=13.
The variable global_max and local_max are created for the purpose.
(we can also use self.max to solve the problem)
'''



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
            
