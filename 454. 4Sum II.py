class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
'''
Naive approach.
O(N^4) Time complexity. ---> Time Limit Exceeded.
It is noticed that k + l is repeatedly calculated, so we need to think up a wat to avoid this.
'''
        # total = 0
        # for i in A:
        #     for j in B:
        #         for k in C:
        #             for l in D:
        #                 if i + j + k + l == 0:
        #                     total +=1
        # return total
'''
The way to avoid calculating repeatedly C and D is to calculate them first then compare to A,B.
A+B+C+D=0 <=> A+B=-(C+D)
so I create a dictionary to store the values of A+B. Rmb that there might be duplicate values and we need to store the number of it.
At first, I created another dictionary to store the values of C+D, then for every item in setone, check if -item is in settow.
This method works, but the result was only faster around 37% of submissions.
Then I noticed that there is no need to create the second dictionary. All we need to check is that whether the sum is in the setone.
Then the result is faster than 71% of submission.
'''
        total = 0
        setone=dict()
        for i in A:
            for j in B:
                if i+j not in setone:
                    setone[i+j] = 1
                else:
                    setone[i+j] += 1
                
        
        #settwo=dict()
        for i in C:
            for j in D:
                if -(i+j) in setone:
                    total += setone[-(i+j)]
                
#                 if i+j not in settwo:
#                     settwo[i+j] = 1
#                 else:
#                     settwo[i+j] += 1
        
#         for i in setone:
#             if -i in settwo:
#                 total+=setone[i]*settwo[-i]
        return total
