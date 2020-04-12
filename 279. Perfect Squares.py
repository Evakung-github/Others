class Solution:
'''
Instead of calculating the number of perfect square numbers from 1 to n.
The following algorithm does it backwardly.
For example, n = 31 and the square root of it is 5.....
1 --> 30              
2 --> 27
3 --> 22  --------->  In the next step, looping though these five numbers again to find the number after minus square number til we find
4 --> 15              square number.
5 --> 6


'''
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
'''
First I used DP to solve the problem. Calculate the least number of perfect square numbers from 1 to n.
When finding the least number, we only need to find the square number less than the current number.
Therefore, the time complexity is O(n*sqrt(n)).
However, this shows no efficiency in Python.
'''
        
        
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
        
        
