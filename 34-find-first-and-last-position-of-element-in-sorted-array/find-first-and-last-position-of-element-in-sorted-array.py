class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findfirst(nums,target)
        last = self.findlast(nums,target)
        return [first, last]

    def findfirst(self,nums,target):
        low=0
        high =len(nums)-1

        answer=-1

        while low<=high:
            mid = low + (high -low)//2

            if nums[mid] == target :
                answer = mid
                high = mid -1
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1

        return answer

    def findlast(self,nums,target):
        low=0
        high =len(nums)-1

        answer=-1

        while low<=high:
            mid = low + (high -low)//2

            if nums[mid] == target :
                answer = mid
                low = mid +1
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid+1

        return answer
