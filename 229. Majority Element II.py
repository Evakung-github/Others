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
