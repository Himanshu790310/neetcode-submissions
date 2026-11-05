class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        mx = 0
        x = -1
        for i in nums:
            d[i] = d.get(i,0) +1
        while k != 0:
            for key,val in d.items():
                if val > mx:
                    mx = val
                    x = key
            res.append(x)
            del d[x]
            mx = 0
            x = -1
            k -= 1
        return res
            

        