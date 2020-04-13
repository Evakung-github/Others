'''
I only track the number of ones, increase 1 when it's one, decrease 1 otherwise.
The main idea is that when the counts of one are the same at different timestamp,
it means that there is contguous array between them.
(Draw a graph of the number of ones will be clearer.)
Therefore, I use hashmap to track the position of different count (note that only the first position is stored.)
Time complexity:O(n)

'''


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
