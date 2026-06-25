class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = 0
        R = len(nums)-1

        while R>L:
            if nums[L] %2 == 1 and nums[R] %2 ==0:
                nums[L],nums[R] = nums[R],nums[L]
                L+=1
                R-=1
            elif nums[L]%2==0:
                L+=1
            else:
                R-=1
    
        return nums