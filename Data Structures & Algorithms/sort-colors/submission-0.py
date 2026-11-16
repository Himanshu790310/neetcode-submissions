class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''for i in range(1,len(nums)):
            pivot = nums[0]
            j = i-1
            while j > 0 and pivot < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j =-1
            pivot = nums[j+1]
        return nums
        if len(nums) < 1:
            return nums
        else:'''
        '''def merge(a,b):
            l,i,j = [],0,0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    l.append(a[i])
                    i += 1
                else:
                    l.append(b[j])
                    j += 1 
            return l + a[i:] + b[j:]

        def mergesort(l):
            if len(l) <= 1:
                return l
            mid = len(l)//2
            return merge(mergesort(l[:mid]), mergesort(l[mid:]))
        return mergesort(nums)'''
        def partion(l,low,high):
            pivot = l[low]
            i = low 
            for j in range(low+1,high+1):
                if l[j] <= pivot:
                    i += 1
                    l[i],l[j] = l[j],l[i]
            l[low],l[i] = l[i], l[low]
            return i
        def quicksort(l, low, high):
            if low < high:
                piv_pos = partion(l,low,high)
                quicksort(l,low,piv_pos-1)
                quicksort(l,piv_pos +1, high)
            return l
        return quicksort(nums,0,len(nums)-1)
        