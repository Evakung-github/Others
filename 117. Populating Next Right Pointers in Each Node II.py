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
'''
First solution: Using bfs.
Track every point level by level. Once the stack is empty, then we know the node is the last node of the level and its next is null 
as well as that it is time to go the next level.
However, the followup question says using constant extra space. Though we can assume the implicit stack does not count as the extra space,
it is fun/worthy to think up another solution for the problem.
'''

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

'''
Second solution: Using three pointers.
Three pointers are used to track current level and next level's leftmost node and moving node.
The current level is shifted by the next pointer, when the next is null, it means it's time to move to the next level, 
start from the leftmost node we recorded before. 
'''

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
        
        
        

