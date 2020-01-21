# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:27:05 2020

@author: eva
"""

#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
        
#         mid = (len(nums)-1) // 2
#         ans = TreeNode(nums[mid])
#         ans.left = self.sortedArrayToBST(nums[:mid])
#         ans.right = self.sortedArrayToBST(nums[mid+1:])
        
#         return ans
    
    
    
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        def helper(nums,start,end):
            if start>end:
                return None
            
            mid=(start+end)//2
            node=TreeNode(nums[mid])
            node.left=helper(nums,start,mid-1)
            node.right=helper(nums,mid+1,end)
            return node
        return helper(nums,0,len(nums)-1)