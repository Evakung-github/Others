class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # total = 0
        # for i in A:
        #     for j in B:
        #         for k in C:
        #             for l in D:
        #                 if i + j + k + l == 0:
        #                     total +=1
        # return total
        
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
