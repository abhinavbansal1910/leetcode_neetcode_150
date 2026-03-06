from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()  # sort the array
        
        closest_sum = nums[0] + nums[1] + nums[2]  # initial closest sum
        
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]
                
                # update closest sum
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum   # exact match
        
        return closest_sum