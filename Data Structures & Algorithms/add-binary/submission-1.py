class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        def nums(x):
            s = 0
            while len(x) > 0:
                s += 2**(len(x)-1) * int(x[0])
                x = x[1:]
            return s
        def bin(n):
            s = ''
            while n >= 1:
                if n % 2 == 0:
                    s += '0'
                elif n % 2 == 1:
                    s += '1'
                n = n // 2
            s = s[::-1]
            return s
        return bin(nums(a)+nums(b))
        