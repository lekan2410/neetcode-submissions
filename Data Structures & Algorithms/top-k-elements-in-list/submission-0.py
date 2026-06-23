class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = defaultdict(int)

        new_list = []

        for i in range(len(nums)):
            dictionary[nums[i]] += 1

        sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        result = [num for num, freq in sorted_items[:k]]

        return result

        
        