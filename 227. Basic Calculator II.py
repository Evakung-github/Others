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
