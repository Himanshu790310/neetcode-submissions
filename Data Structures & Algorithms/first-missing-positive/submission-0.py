class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = 1
        y = max(nums)
        if y <= 0:
            return x
        for i in range(1,y+1):
            if i not in nums:
                return i 
            if i == y:
                return i +1