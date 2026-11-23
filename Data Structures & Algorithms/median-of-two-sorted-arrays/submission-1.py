class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        odd = lambda x: x%2 ==1
        if odd(n):
            return float(l[n//2])
        else:
            return (l[n//2] + l[n//2-1])/2