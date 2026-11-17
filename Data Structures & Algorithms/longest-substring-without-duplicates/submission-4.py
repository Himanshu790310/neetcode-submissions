class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        r = ''
        l = []
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        for i in s:
            if i not in r:
                r += i
            else:
                l.append(len(r))
                r = r[r.index(i)+1:]
                r += i
        if l == []:
            return len(r)
        else:
            return max(len(r), max(l))
        return max(l)