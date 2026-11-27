from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k,v in d.items():
            if v > 1:
                return k
        #flag = False
        '''for i,v in enumerate(nums):
            if v in nums[i+1:]:
                return v'''
        