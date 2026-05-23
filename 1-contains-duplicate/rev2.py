from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_seen = []
        for num in nums:
            if num in list_seen:
                return True
            list_seen.append(num)
        return False

sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))