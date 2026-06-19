class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}
        
        for i, num in enumerate(nums):
            if num in dictionary and i - dictionary[num] <= k:
                return True
            dictionary[num] = i
        
        return False
        
        