# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder)==0:
            return

        ino = dict(zip(inorder,range(len(inorder))))
        
        
        def helper(l,h):
            print(l,h)
            if l > h:
                return None

            node = postorder.pop()
            tree = TreeNode(node)
            index = ino[node]
            
            tree.right = helper(index+1,h)
            tree.left = helper(l,index-1)
                   
          
            return tree
