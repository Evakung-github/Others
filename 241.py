# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:09:48 2020

@author: eva
"""

#solved by divide and conquer
#First, I constructed the algorithm without memorization. It worked but it took 36ms, which was faster than only 33% of submitted solution.
#After looing into code carefully, I noticed that multiple steps were repeated, leading to the inefficiency of the programming.
#Therefore, I implemented memorization by using self.memo to reduce repeated calculations, then it takes 20 ms.


class Solution:
    def __init__(self):
        self.memo = {}    
    def diffWaysToCompute(self, input: str):
        if input == '':
            return [0]
        
        if input in self.memo:
            return self.memo[input]
        
        num = ''
        i = 0
        ans = []
        while i <len(input):
            if input[i] not in ['+','-','*']:
                num += input[i]
                i += 1
                continue
            
            l = self.diffWaysToCompute(input[:i])
            r = self.diffWaysToCompute(input[i+1:])
            
            if input[i] == '+':
                ans+=[a + b for a in l for b in r]
            elif input[i] == '*':
                ans+=[a * b for a in l for b in r]
            else:
                ans+=[a - b for a in l for b in r]
                
            i+=1
        self.memo[input] = ans if len(ans)>0 else [int(num)]
        return ans if len(ans)>0 else [int(num)] 




a = Solution()
a.diffWaysToCompute('2*3-4*5')