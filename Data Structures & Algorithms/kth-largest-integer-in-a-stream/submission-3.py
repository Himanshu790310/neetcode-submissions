import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heapify_max(self.nums)
        heapq.heappush(self.nums,val)
        return heapq.nlargest(self.k, self.nums, key = None)[self.k-1]
