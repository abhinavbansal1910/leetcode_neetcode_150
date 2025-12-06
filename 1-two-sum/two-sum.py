class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            # If complement is found in the map, return the indices
            if diff in num_map:
                return [num_map[diff], i]


            num_map[num] = i