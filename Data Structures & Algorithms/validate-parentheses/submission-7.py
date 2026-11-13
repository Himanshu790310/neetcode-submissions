from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open = '({['
        close = ')}]'
        d = {')':'(', '}':'{',']':'[','(':')', '{':'}','[':']'}
        flag = True
        if len(s) %2 ==1:
            return False
        if s[0] in close:
            return False
        for i in s:
            if i in open and d[i] not in s:
                return False
        for i in s:
            if i in open:
                stack.append(i)
            if i in close:
                try:
                    x = stack.pop()
                except:
                    return False
                if x != d[i]:
                    flag = False
                    break
        if len(stack) != 0:
            return False
        return flag 
        