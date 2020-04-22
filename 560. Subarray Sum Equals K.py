'''
The intuitive solution is iterating all the possible combinations(subarrays).
Time complexity: O(n**2) which causes TLE.

The improved algorithm is O(N).
Starting from left, generate the accumulative sum and store it in a dictionary (hash map).
The idea is presented below.

sum(i,j) = sum(0,j) = sum(0,i-1)
The dictionary is initiated with a zero
Suppose array [-1,1,-1,1,1] ,k = 0.
The accumulation array is [-1,0,-1,0,1].
-1 --> store it.
0  --> (k-0) in the dictionary, ans += 1 and store it, so there are 2 zeros now.
-1 --> (k-(-1)) not in dictionary, store it, two -1 now.
0  --> (k-0) in the dictionary, ans += 2 and store it, so there are 3 zeros now.
(two zeors in the dictionary means that there are two start points to the current position with the total sum equal to k)
....
and so on.


Then the answer is derived.
'''


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
