'''
The problem is solved by quick sort.
As it is unnecessary to find the first, the second, the third ...... largest, we need to eliminate excessive sort.
Therefore, an index is picked up randomly and it is the point we used to separate the list, which is also called pivot.
After one while loop, the numbers in left part are no less than the pivot.
The worst time complexity is O(n^2) if it is the increasing or decreasing list. (The position of the pivot doesn't change and we have to iterate through the whole list)
The best time complexity is O(n) if the medium is picked in every iteration.
'''

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
