class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}       #hash map [num_val, pos]

        size = len(nums)

        for i in range(size):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[nums[i]] = i

        return []

            