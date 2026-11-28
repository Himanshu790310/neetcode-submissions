class Solution:
    def hammingWeight(self, n: int) -> int:
        def binary(x):
            s = ''
            while x >= 1:
                if x == 1:
                    s += '1'
                    break
                dig = x % 2
                s += str(dig)
                x = x//2
            s = s[::-1]
            return s.count('1')
        return binary(n)