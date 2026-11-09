class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0
        for i in range(x+1):
            if i*i <= x:
                y = i
            else:
                break
        return y