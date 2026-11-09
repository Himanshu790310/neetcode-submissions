class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        mid = len(nums)//2
        while low <= high:
            if nums[mid] < target:
                low = mid +1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
            mid = (low+high)//2
        return -1
        