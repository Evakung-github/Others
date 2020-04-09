'''
The intuition methode is to find the final text result by popping the stack once seeing "#".
However it takes O(N) time and O(N) space.

Followup:
O(N) time and O(1) space.
 
We can't decide the final result of each string if doing from left to left,
however we can if doing backwardly.
The only issue is that we can't make sure if the next char should be skipped or be kept (if it is "#").
Therefore, new variable, back, is introduced to track how many "#" we have met so far, and if we can skip the next char.
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = len(S)-1
        t = len(T) - 1
        while s >= 0 and t >=0:
            if S[s] != '#' and T[t] != '#':
                if S[s] != T[t]:
                    return False
                s -= 1
                t -= 1
            back = 0
            while s >= 0 and (S[s] == '#' or back > 0):
                if S[s] == '#':
                    back += 1
                    s -= 1
                else:
                    back -= 1
                    s -= 1
                
            back = 0
            while t >= 0 and (T[t] == '#' or back > 0):
                if T[t] == '#':
                    back += 1
                    t -= 1
                else:
                    back -= 1
                    t -= 1
        
        return s == -1 and t == -1
        
        
        
        
        
#         s= []
#         for i in S:
#             if s and i == '#':
#                 s.pop()
#             if i != "#":
#                 s.append(i)
                
#         t = []
#         for i in T:
#             if t and i == '#':
#                 t.pop()
#             if i != '#':
#                 t.append(i)
        
#         return "".join(s) == "".join(t)
        
