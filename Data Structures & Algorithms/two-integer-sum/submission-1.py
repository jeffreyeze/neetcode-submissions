class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            numb = target - nums[i]
            if numb in seen:
                return [seen[numb], i]
            seen[nums[i]] = i
        return 0