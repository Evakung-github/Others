class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return True
        
        max_ = nums[0]
        i = 0
        while i <= max_:
            if i + nums[i]>=len(nums)-1:
                return True
            if i + nums[i]>max_:
                max_ = i+nums[i]
            
            i+=1

        
        return False
