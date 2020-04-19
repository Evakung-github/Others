'''
Q81 is a followup of Q33, where Q81 allows duplicate and Q33 doesn't.

Let's discuss Q33 first.
As the question requires us to do in O(logn), it is solved using binary search.

There are two cases of mid, for each case we can split into two another cases.
1. mid is in the ascending part of start
  a. if target is in between start and mid, then we move right pointer to mid.
  b. else: move left pointer to mid
2. mid is in the descending part.
  a. if target is in between mid and end, then we move left pointer to mid.
  b. else: move right pointer to mid
(it will be easier to understand if drawing images)

However, things get a little bit complicated when duplicates are allowed.
In this case, we might not be able to recognize which part mid is in.
Hence, I think of a solution that first check whether left and right pointers point to the same value.
Then do the same thing as in Q33.

The Time complexity is at worst O(n) if all the value in the list are the same, but still O(logn) in general.
'''


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
