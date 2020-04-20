"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
Recursion
'''
class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        self.ans.append(root.val)
        for c in root.children:
            self.preorder(c)
        return self.ans

'''
Iteration
'''
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
  
        ans = []
        stack = [root]
     
        while stack:
            r = stack.pop()
            ans.append(r.val)
            stack.extend(r.children[::-1])
        
        return ans
