from collections import deque
class Solution:
    def removeDuplicates(self, nums):
        d = 0
        queue = deque()
        for i in nums:
            queue.append(i)
        c = 0
        while queue:
            x = queue.popleft()
            if x in nums[c+1-d:]:
                nums.pop(c-d)
                d += 1
            c += 1
        return len(nums)