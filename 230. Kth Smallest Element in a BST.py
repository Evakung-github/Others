# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
First solution is more intuitive. I create a helper function that traverses the tree in inorder way.
Count variable indicates the samll order we are at now, once all the left subtree is done traversal, then increment it by 1 then do the right subtree.
However, the function can't be stopped once we find the count equal to k. It seems the algorithm still provides good efficiency, but I still implement it in another way.

Second solution is implemented without helper function.
One loop is not enough for this question as we want to track all the left subtrees first then right subtrees.
So two variables, cur and stack, are created to track the left subtrees of current node and record root node, so right subtree is traversed later.
'''


class Solution:
    def __init__(self):
        self.ans = 0
        self.count = 0
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            
            cur = cur.right
#         count = 0
        
#         def helper(root):
            
#             if not root:
#                 return
#             if root.left:
#                 helper(root.left)
            
#             self.count += 1
#             if self.count == k:
#                 self.ans = root.val
#             elif self.count>k:
#                 return
            
#             if root.right:
#                 helper(root.right)
            
#             return
        
#         helper(root)
#         return self.ans
