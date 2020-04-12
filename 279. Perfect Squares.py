class Solution:
    def numSquares(self, n: int) -> int:
        
        sqrt = 1
        while sqrt*sqrt<=n:
            sqrt+=1
            
        cur = set()
        cur.add(n)
        count = 0
        while cur:
            temp = set()
            count += 1
            for i in cur:
                for j in range(sqrt):
                    if i == j*j:
                        return count
                    if i>j*j:
                        temp.add(i-j*j)
                    else:
                        break
            cur = temp
        return count
                
        
        
#         memo = {1:1}
#         square = 1
        
#         cur = 2
        
#         while cur <=n:
#             m = float('inf')
#             if cur == (square+1) * (square+1):
#                 m = 1
#                 square += 1
#             else:
#                 for i in range(1,square+1):
#                     if m > 1 + memo[cur-i*i]:
#                         m = 1 + memo[cur-i*i]


            
#             memo[cur] = m
#             cur += 1
       
#         return memo[n]
        
        
