class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3

        dictionary = defaultdict(int)

        res = []

        for n in nums:
            dictionary[n] += 1

        for key in dictionary:
            if dictionary[key] > k:
                res.append(key)

        return res
            
        