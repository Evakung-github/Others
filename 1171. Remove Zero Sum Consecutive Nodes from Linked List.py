# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
At first, I tried to solve the problem by create the list, remove the zero sum subset and turn it back to link list.
I couldn't think up a good way to find the zero sum subset, so basically the first method is trying to sum up all the subset 
and then remove it.

Then actually there is easier way to find the subset we want, which is adding from the beginning of the link list, 
and when the sum matches the previous sum, it means the sum of the subset between them is zero!!! 

In addition, it is well noticed that the last one should be kept instead of the first one, 
take [1,3,2,-3,-2,5,5,-5,1] for example. If the sum series is [1,4,6,3,1,6,11,6,7,6]
when the second "1" is found, the link list is now 1 --> 5 --> 5 --> -5 --> 1.
The error occurs when the following 6s matching the previous 6, but 6 is no longer valid in the sum series.
Hence, we should kind of solving this problem backwardly.
'''



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
