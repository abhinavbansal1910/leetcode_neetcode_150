class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        while i <len(nums):
            while i<len(nums) and nums[i]%2==0:
                i+=2
            while j<len(nums) and nums[j]%2==1:
                j+=2
            if i < len(nums):
                nums[i],nums[j]=nums[j],nums[i]

        return nums