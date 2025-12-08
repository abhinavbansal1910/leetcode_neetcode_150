class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Create buckets where index = frequency
        # Size is len(nums)+1 because max frequency is len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Place numbers in their frequency buckets
        for num, frequency in count.items():
            freq[frequency].append(num)
        
        # Collect top k frequent elements
        result = []
        # Start from highest frequency, go down to 1
        for frequency in range(len(freq)-1, 0, -1):
            for num in freq[frequency]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result