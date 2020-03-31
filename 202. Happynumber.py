# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:54:32 2020

@author: eva
"""

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