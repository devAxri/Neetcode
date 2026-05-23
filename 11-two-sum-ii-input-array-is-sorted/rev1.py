from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for o in range(len(numbers)):
                if i == o:
                    continue
                if numbers[i] + numbers[o] == target:
                    return [i+1, o+1]
                
sol = Solution()
print(sol.twoSum([1,2,3,4], 3))