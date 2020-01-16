# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:57:15 2020

@author: eva
"""

class Solution:
    def canCompleteCircuit(self, gas):
#         i=0
#         while i <len(gas):
#             res = 0
#             j=i
#             while res+gas[j%len(gas)]-cost[j%len(gas)]>=0:
#                 res = res+gas[j%len(gas)]-cost[j%len(gas)]

#                 j += 1
#                 if j == i:
#                     return i
#             i = j+1
#         return -1

        lack = 0
        gas_sum = 0
        ans = 0
        for i in range(len(gas)):
            gas_sum = gas_sum +gas[i]-cost[i]
            if gas_sum<0:
                lack += gas_sum
                ans = i+1
                gas_sum =0
        if gas_sum + lack >=0:
            return ans
        else:
            return -1