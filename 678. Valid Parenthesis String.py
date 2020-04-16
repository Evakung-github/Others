class Solution:
    def checkValidString(self, s: str) -> bool:
'''
The first implementation is more intuitive than the second one but the idea behind them is similar.
Let's see what it only contains '(' and ')'. We increment the number by 1 if it is '(' else -1, if the number is less than 0, 
which means ')' is more than '(' and is invalid.
In this question, we have '*' and this can either +1, -1 or 0. We consider all the conditions, then once if 0 is in the list, then it is valid.
To improve the efficiency, I use set to avoid duplications.
'''
        count = [0]
        for i in s:
            j = 0
            next = set()
            while j < len(count):
                if count[j]>=0:      
                
                    if i == '(':
                        next.add(count[j] + 1)
                    elif i == ')':
                        next.add(count[j] - 1)
                    else:
                        next.add(count[j]+1)
                        next.add(count[j]-1)
                        next.add(count[j])
                
                j += 1
            count = list(next)
            if count == []:
                return False
     

        return 0 in count
'''
Solution 2
In the previous answer, it is noted that we don't need to store all the possible outcomes. 
All we care about is whether if there is at least one outcome greater than 0 and if there is 0 in the final state.
So what we need to do is to record the minimun and the maximum value of outcomes.
The minimum value takes only '(' as +1 and '), '*' as -1.
The maximum value takes both '(' and '*' as +1 and ')' as -1.
Once the maximum value less than 0, which means "count == []" in the previous solution, then it returns False.
If the minimum value == 0, meaning 0 in count in the previous solution, then it is a valid string.
'''
    
    
    
        low = 0
        high = 0
        for i in s:
            if i == '(':
                low += 1
                high += 1
            elif i == ')':
                if low>0:
                    low -=1
                high -= 1
            else:
                if low>0:
                    low-=1
                high += 1
            if high < 0:
                return False
        
        return low == 0
        
