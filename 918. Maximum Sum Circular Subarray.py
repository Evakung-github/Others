class Solution:
    def maxSubarraySumCircular(self, A):
        max_ = -float('inf')
        temp_max = 0
        min_ = float('inf')
        temp_min = 0
        sum_ = 0
        for i in A:
            temp_max += i
            temp_min += i
            sum_ += i
            max_ = max(max_,temp_max)
            min_ = min(min_,temp_min)
            temp_max = max(0,temp_max)
            temp_min = min(0,temp_min)
        
        if sum_ == min_:
            return max_
        else:
            return max(max_,sum_-min_)
        
