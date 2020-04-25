'''
At first, I thought the problem was solved by DP. However, O(n**2) was still needed no matter what, leading to time limit exceeded.
After a while, it is noticed that this can be solved by the greedy algorithm as what matters is the maximum position.

At each point, record the farest point it can get. Update the farest point while iterating the nums list.
Take [2,3,1,1,4] for example,
At index 0, max_ = 2
At index 1, 1+3 > max_ ==> max_4 (Note that it is feasible as index 0 can choose to reach index 1 and jump to 4.)
At the time max_>= total length -1, we got the answer!

Take [3,2,1,0,4] for example,
At index 0, max_ = 3
At index 1, 1+2 not bigger than max_, so it doesn't matter if we change or not.
At index 2, 2+1 not bigger than max_, so it doesn't matter if we change or not.
At index 3, the max_ is still 3 so it means the sequence terminates at this point.

Time complexity: O(n)

'''



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
