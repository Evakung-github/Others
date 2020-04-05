# Time complexity:O(n!) factorial time


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []                
        for i in range(len(nums)):
            temp = [nums[i]]
            l = self.permute(nums[:i]+nums[i+1:])
            ans.extend(temp+i for i in l)
        
        return ans 

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if nums == None or len(nums) in[0,1]:
#             return [nums]

#         ans = []
#         for i in nums:
#             k = nums.copy()
#             k.remove(i)
#             for j in self.permute(k):
#                 #temp = [i]
#                 # temp.extend(j)
#                 ans.append([i]+j)
#         return ans

#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # if not nums:
#         #     return nums
#         # if len(nums) == 1:
#         #     return [nums]
#         ans = []
        
#         def helper(cur,nums):
#             if nums:
#                 for i in range(len(nums)):
#                     helper(cur+[nums[i]],nums[:i]+nums[i+1:])
#             else:
#                 ans.append(cur)
#                 return
#         helper([],nums)
        
#         return ans

