class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        memo = {0:-1}
        onecount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                onecount += 1
            else:
                onecount -= 1
            
            if onecount in memo:
                if i -memo[onecount]>ans:
                    ans = i-memo[onecount]
            else:
                memo[onecount] = i
        
        return ans
