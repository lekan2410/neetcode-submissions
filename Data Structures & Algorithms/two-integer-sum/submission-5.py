class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target - nums[i]

            if diff in dictionary:
                return [dictionary[diff], i]

            dictionary[n] = i






        