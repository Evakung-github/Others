# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Inorder: left subtree --> root node ---> right subtree
Postorder: left subtree --> right subtree --> root node
We start to build the tree from the last element of postorder.
Once a node is located, we can find its left and right subtree by indexing on Inorder. However, the index can't be over its upper root nodes.
As in postorder, right root node is right behind the root node, so we should build the right subtrees before left subtrees.

For example,
Inorder: [9,3,15,20,7]
Postorder: [9,15,7,20,3]
3 is the root node, and the elements in inorder that are left of it are left subtrees and the opposite for the elements on the right.
then the right root node is 20, so 15 is its left subtree and 7 is its right subtree, and so on....

'''




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
