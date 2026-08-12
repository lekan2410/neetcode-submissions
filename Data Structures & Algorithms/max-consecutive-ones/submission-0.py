class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                max_one += 1
            else:
                max_one = 0

            res = max(res, max_one)
        
        return res

        