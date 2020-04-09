# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        
        s = 0
        h = ListNode(0)
        h.next = head
        memo = {0:head}
        while head:
            s+=head.val
            memo[s] = head.next
            head = head.next
        
        
        s = 0
        head = h
        while head:
            s += head.val
            head.next = memo[s]
            head = head.next
        
        
        
        return h.next
        
        
        
        
#         node_list = []
#         while head:
#             node_list.append(head.val)
#             head = head.next
        
#         acc = [0]
#         ans = cur = ListNode(0)
#         i = 0
#         start = 0
#         while i <len(node_list):          
#             if acc[-1]+node_list[i] == 0:
#                 start = i+1
#             acc.append(acc[-1]+node_list[i])  
#             i += 1
#         if start>=len(node_list):
#             return
#         cur.next = ListNode(node_list[start])
#         prev,cur =cur, cur.next

#         i = start+1
#         while i < len(node_list):
#             start = i
#             j = i
#             while j < len(node_list):
#                 acc[j+1] -= acc[i]
#                 if acc[j+1] == 0:
#                     start = j
#                 j+=1
#             if start == i and node_list[i] != 0:
#                 cur.next = ListNode(node_list[i])
#                 cur = cur.next
#             i = start + 1
        
#         return ans.next
        
        
        
        
        
#         acc = [0]
#         i = 0
#         while i <len(node_list):
#             if acc[-1]+node_list[i] == 0:
#                 node_list = node_list[i+1:]
#                 acc = [0]
#                 i = 0
#             else:
#                 acc.append(acc[-1]+node_list[i])
#                 i += 1
        
#         i,j = 1,0
        
#         while i < len(node_list):
#             j = i
#             while j<len(node_list):
#                 acc[j+1] -= acc[i]
#                 if acc[j+1] ==0:
#                     node_list = node_list[:i]+node_list[j+1:]
#                     acc = acc[:i+1]+acc[j+2:]
                    
#                     i -= 1
#                     break
#                 j+=1
#             i += 1

        
#         h = t = ListNode(0)
#         for i in node_list:
#             t.next = ListNode(i)
#             t = t.next
        
#         return h.next
