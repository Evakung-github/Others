# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:54:32 2020

@author: eva
"""

#Implementing this algorithm is not hard.
#However, what concerned me the most was why it is guaranteed to converge either to 1 or form a loop.
#Then I realized that it is due to the square of each digit being at most 81, say 100 for simplicity.
#Take a number with five digits for example, the next number after summing square of each digit is at most 500.
#Then the next number is at most 300, and the next number is at most 300 as well as there are only three digits and so on.
#So after at most 300 iterations, we will either find 1 or a loop.
#(Rough) Time complexity: At most 81*logN iterations which loop through each digits log(81*(logN)).



class Solution:
    def isHappy(self, n: int) -> bool:

        memo = set()
        while n >4:
            next = 0
            while n >0:
                next += (n%10) **2
                n = n //10

            if next in memo:
                return False
            else:
                memo.add(next)
            n = next
   
        
        return n==1
