from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            for k in range(len(nums)):
                num2 = nums[k]
                if i == k:
                    continue
                if num+num2 == target:
                    index_1 = i
                    index_2 = k
                    return [index_1, index_2]

sol = Solution()
print(sol.twoSum([3,4,5,6], 7))