class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0                      # starting index
        high = len(nums) - 1         # last index

        while low <= high:
            mid = (low + high) // 2  # middle index

            if nums[mid] == target:
                return mid           # target found

            elif nums[mid] < target:
                low = mid + 1        # search right side

            else:
                high = mid - 1       # search left side

        return -1                    # target not found
