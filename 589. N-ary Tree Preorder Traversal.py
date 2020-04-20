"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self, root: 'Node') -> List[int]:
        # if not root:
        #     return
        # self.ans.append(root.val)
        # for c in root.children:
        #     self.preorder(c)
        # return self.ans
        if not root:
            return
  
        ans = [root.val]
        stack = [root]
     
        while stack:
            if stack[-1].children == []:
                stack.pop()
            else:
                r = stack[-1].children.pop(0)
                stack.append(r)
                ans.append(r.val)
        
        return ans
