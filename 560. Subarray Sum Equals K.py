class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        acc = 0
        # prevsum = set()
        # prevsum.add(0)
        prevsum = dict()
        prevsum[0] = 1
        for i in nums:
            acc += i
            if acc - k in prevsum:
                ans += prevsum[acc-k]
            
            if acc in prevsum:
                prevsum[acc]+=1
            else:
                prevsum[acc]=1

        return ans
        
        
        
        # i = 0
        # ans = 0
        # while i <len(nums):
        #     s = 0
        #     for j in range(i,len(nums)):
        #         s += nums[j]
        #         if s == k:
        #             ans += 1
        #     i += 1 
        return ans
