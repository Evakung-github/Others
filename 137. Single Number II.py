'''
solution 1: count the total number of 1 at ith position. Since other numbers appear three times, 
so the remainder after dividing total count by 3 is that single number.
As the maximum size of integer is 2^32-1, so set the outer loop to be 32.
Need to be aware of negative integer.
However, the solution is slow. so I implemented another solution.
'''
class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ans = 0
#         s = 0
        
#         for n in nums:
#             if n < 0: s+=1
        
#         for i in range(32):
#             c = 0
#             for n in nums:
#                 c += (1&(abs(n)>>i))
#             ans = ans | ((c%3) << i)
#             # ans += ((c%3) << i)
        
#         return ans if s % 3== 0 else -ans

'''
we want a new operation(@) that can make n@n@n = 0.
Two sets, ones and twos, are created.

we first put n in ones, which is operated by (ones ^ n).
When n appears the second time, it is taken out from ones and put in twos.
At the third time, n can't be put in ones as it is now in twos and n is taken out from twos.
Finally, what remains in ones is the answer.

'''


    def singleNumber(self, nums: List[int]) -> int:
        ones,twos = 0,0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        
        return ones
