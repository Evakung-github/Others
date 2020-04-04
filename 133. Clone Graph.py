"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
# I created a hash table to track whether the node has been created or not and also map it to the created node for future use.
# This could avoid infinite loop. The node created before will be returned immediately when being called.


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        created = dict()
        
        def helper(node):
            if node in created:
                return created[node]
            else:
                root = Node(node.val)
                created[node] = root
            
            n = []
            for i in node.neighbors:
                n.append(helper(i))
            
            root.neighbors = n
            return root

            

        
        return helper(node)
         
          
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return node
    
#         visited={}
#         que=[]
#         visited[node]=Node(node.val,[])
#         que.append(node)
#         while que:
#             n=que.pop(0)
            
#             for nei in n.neighbors:
#                 if nei not in visited:
#                     visited[nei]=Node(nei.val,[])
#                     que.append(nei)
                
#                 visited[n].neighbors.append(visited[nei])
#         return visited[node]              
