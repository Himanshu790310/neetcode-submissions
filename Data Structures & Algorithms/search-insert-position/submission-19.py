class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        mid = len(nums)//2
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            elif nums[0] < target:
                return 1
            else:
                return 0
        if target > nums[-1]:
            return high+1
        elif target == nums[-1]:
            return high
        while low <= high:
            if nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid 
            else:
                return mid
            mid = (low+high)//2
            if high - low == 1:
                if nums[high] > target and nums[low] < target:
                    return low +1
                elif nums[high] > target and nums[low] > target:
                    return low
        