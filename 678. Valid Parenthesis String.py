class Solution:
    def checkValidString(self, s: str) -> bool:
        

        
 
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
        
