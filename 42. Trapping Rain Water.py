'''
I solved the problem by two pointers (left and right).
The total area was calculated by getting the area of two pointers and then minus the part doesn't need, 
add the part isn't covered by the previous two pointers.

Take [4,3,6,5,1] for example,

l = 0, r = 4 ---> area = 4 * 1= 4
as height[r] < height[l], r -= 1 ---> r = 3
l = 0, r = 3 ---> the area 4 includes portion of r = 3, so it should be removed, area -= 1 * 1.
Also, the area formed by l = 0 and r = 3 that hasn't covered is 3 * 2 = 6. (3 = min(height[0],height[3]) - 1 (previous height)).
so area = area + 6 = 9.

keeps doing.... til l < r-1.

Then, the answer is derived.
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        prev_h = min(height[0],height[-1])
        ans = prev_h*(len(height)-2)
        l,r = 0,len(height)-1
        
        while l <r-1:
            if height[l]>height[r]:
                r -= 1
                ans -= min(prev_h,height[r])
            else:
                l += 1
                ans -= min(prev_h,height[l])
            h = max(prev_h,min(height[r],height[l]))
            ans += (h-prev_h)*(r-l-1)
            prev_h = h
            
            
        return ans
