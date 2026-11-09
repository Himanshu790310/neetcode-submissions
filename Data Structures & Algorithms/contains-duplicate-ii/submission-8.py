class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        x,y,z = 0,0,0
        for i in nums:
            if i in nums[nums.index(i)+1:]:
                x = nums.index(i)
                z = i
                nums = nums[nums.index(i)+1:]
        try:
            y = nums.index(z)+1
        except:
            y = -55555555555
        if abs(x-y) <= k:
            return True
        return False