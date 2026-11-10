class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]
        r = ''
        flag = False
        if len(strs) == 1:
            return strs[0]
        for i,s in enumerate(x):
            try:
                for m in strs[1:]:
                    if x[i] == m[i]:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    r += x[i]
                else:
                    break
            except IndexError:
                continue
        return r
            
        