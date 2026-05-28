from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            count = 0
            for num2 in nums:
                if num == num2:
                    count += 1
                    if count > 1:
                        return True
        else:
            return False

sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))