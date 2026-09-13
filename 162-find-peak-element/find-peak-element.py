class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = low +(high-low)//2
            if nums[mid] <nums[mid+1]:
                #that is we are going uphill so we can choose the right part
                low = mid+1
            else:
                high = mid

        return low