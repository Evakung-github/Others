'''
Tt requires O(n) space if solved using hashmap.
Therefore, another algorithm should be implemented to achieve O(1) space, which is Boyer-Moore Majority Vote algorithm.
For simplicity, say we just want to find the majority element that appears more than ⌊ n/2 ⌋ times.
Take [1,2,3,1,2,1,1] for instance,
Step1, say candidate is 1 then its vote is 1.
step2, another candidate shows up, so votes of candidate1 and candidate2 are tie. Turn vote of candidate1 into 0.
      At this stage, it is unnecessary to store candidate2 as it ties with candidate1 and if it is the majority, then it will appear later again, and we will name it as candidate if necessary.
Step3, another candidate shows up, and since votes of candidate1 is 0. So we nominate a new canditate and its vote now is 1.
Step4, 1 is not equal to 3, so we deduct candidate3's vote by 1.
Step5, since votes of candidate3 is 0. So we nominate a new canditate and its vote now is 1.
...
...
till we find the true candidate. However, this can the false candidate, so the final count should be done again.

The main idea of Boyer-Moore Majority vote algorithm is that the majority will remain after deducting with others.
The same idea applies in this problem. The only difference is that there will be at most two candidates.
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        memo = {}
        for i in nums:
            new_memo={}
            if i in memo:
                memo[i]=memo[i]+1
                continue
            else:
                if len(memo)<2:
                    memo[i] = 1
                    continue
                else:
                    for k in memo:
                        if memo[k] == 0:
                            new_memo[i] =1
                        else:
                            if memo[k]-1>0:
                                new_memo[k] = memo[k]-1
                            
            memo = new_memo
        
        for i in memo:
            memo[i]=0
        for i in nums:
            if i in memo:
                memo[i]+=1
            
        return [k for k in memo if memo[k] > len(nums)//3]
                    
        
        
        
        
        
        
#         cache = {}
#         ans = set()
#         th = len(nums)//3
#         for i in nums:
#             if i in ans:
#                 continue
#             if i not in cache:
#                 cache[i] = 1
#             else:
#                 cache[i] +=1
#             if cache[i]>th:
#                 ans.add(i)
#                 if len(ans) == 2:
#                     break
        

        
#         return ans
