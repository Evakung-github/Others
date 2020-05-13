class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            i,j = l,l
            m = (l+r)//2
            pivot = nums[m]
            nums[m],nums[r] = nums[r],nums[m]
            while j<r:
                if nums[j]>=pivot:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1                
                j+=1
            nums[i],nums[r] = nums[r],nums[i]
            if i == k-1:
                return nums[i]
            elif i >k-1:
                r = i-1
            else:
                l = i+1
