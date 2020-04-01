#First try. Works but slow.
class Solution:
    def calculate(self, s: str) -> int:
        s+='+'
        if len(s) == 0:
            return 0
        stack = ['+']
        cur = ''
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i+=1
                continue
            if s[i] not in ['+','-','*','/']:
                cur += s[i]
            else:
                if stack[-1] in ['+','-']:
                    stack.append(int(cur))
                else:
                    p = stack.pop()
                    pre = stack.pop()
                    if p == '*':
                        stack.append(pre*int(cur))
                    else:
                        stack.append(pre//int(cur))
                stack.append(s[i])
                cur = ''
            i+=1

        print(stack)
        sum = 0
        i = 0
        while i < len(stack)-1:
            if stack[i] == '+':
                sum += stack[i+1]
            else:
                sum -= stack[i+1]
            i+=2
        
        return sum

# It is noticed that I only need to track the current sign and I don't need to store every sign before it.
# Also, I could transfer '-' to plus negative interger.
# The faster implementation is as follow.

class Solution:
    def calculate(self, s: str) -> int:
        s+='+'
        if len(s) == 0:
            return 0
        stack = []
        cur = 0
        sign = '+'
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i+=1
                continue
            if s[i] not in ['+','-','*','/']:
                cur = cur*10 + int(s[i])
            else:
                if sign == '+':
                    stack.append(cur)
                elif sign == '-':
                    stack.append(-cur)
                else:
                    pre = stack.pop()
                    if sign == '*':
                        stack.append(pre*cur)
                    else:
                        stack.append(int(pre/cur))
                
                sign = s[i]
                cur = 0
            i+=1

        # print(stack)
        
        return sum(stack)
    
    
    
    
    
    
    
    
