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
        
