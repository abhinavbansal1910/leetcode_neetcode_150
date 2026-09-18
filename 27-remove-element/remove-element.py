class Solution:
    def removeElement(self, nums, val):

        k = 0

        # Go through every element
        for i in range(len(nums)):

            # If current element is NOT the value we want to remove
            if nums[i] != val:

                # Put it at position k
                nums[k] = nums[i]

                # Move k forward
                k += 1

        # k = number of elements that were kept
        return k