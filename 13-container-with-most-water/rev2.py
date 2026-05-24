from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        results = []
        for i in range(len(heights)):
            start = len(heights) - 1
            while i != start:
                distance = start - i
                area = min(heights[i], heights[start]) * distance
                results.append(area)

                start -= 1

        results.sort()
        return results[-1]
                

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))