"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        
        cur = root
        childhead,child = None,None
        
        while cur:
            if cur.left:
                if childhead:
                    child.next = cur.left
                else:
                    childhead = cur.left
                child = cur.left
            if cur.right:
                if childhead:
                    child.next = cur.right
                else:
                    childhead = cur.right
                child = cur.right
            
            cur = cur.next
            if not cur:
                cur = childhead
                childhead,child = None,None
        
        return root
        
        
        
#         stack = [root]
#         next_ = []
#         while stack:
#             cur = stack.pop(0)
#             if cur.left:
#                 next_.append(cur.left)
#             if cur.right:
#                 next_.append(cur.right)
            
#             if stack:
#                 cur.next = stack[0]
#             else:
#                 stack = next_
#                 next_ = []
        
#         return root
