class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1 

        return (max(dic, key=lambda k: dic[k]))
        