class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        d = {}
        for i in s:
            c[i] = c.get(i,0) +1
        for j in t:
            d[j] = d.get(j,0) +1
        return c == d
        