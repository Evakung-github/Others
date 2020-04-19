class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in set(nums):
        #     return True
        # else:
        #     return False
        
        if not nums:
            return False
        
        left,right = 0,len(nums)-1
        while left<right:
            while right>left and nums[left] == nums[right]:
                right -= 1
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[mid]>=nums[left]:
                if nums[mid] > target and target >=nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[right]>=target and target > nums[mid]:
                    left = mid+1
                else:
                    right = mid -1
            # print(left,right)
        if nums[left] == target or nums[right] == target:
            return True
        
        return False
