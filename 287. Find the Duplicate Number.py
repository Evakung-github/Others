class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s = nums[0]
        f = nums[s]
        
        while nums[s] != nums[f]:
            s = nums[s]
            f = nums[nums[f]]
        s= 0
        while nums[s] != nums[f]:
            s = nums[s]
            f = nums[f]
        
        return nums[s]
