class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        appended_nums = nums

        for i in range(len(nums)):
            appended_nums.append(nums[i])
        
        return appended_nums
        