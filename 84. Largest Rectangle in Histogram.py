

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pos = [-1]
        height = [-float('inf')]
        
        ans = 0
        for i in range(len(heights)):
            p = pos[-1]
            while heights[i] <= height[-1]:
                ans = max(ans,height[-1]*(p-pos[-2]))
                height.pop()
                pos.pop()
            
                
            
            height.append(heights[i])
            pos.append(i)
            
        for i in range(1,len(pos)):
            p = pos[-1]
            ans = max(ans,height[i]*(p-pos[i-1]))
        
        return ans
