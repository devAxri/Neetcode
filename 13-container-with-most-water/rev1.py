from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        results = []
        for i in range(len(heights)):
            #print(f"left: {i}")
            start = len(heights) - 1
            while i != start:
                #print(f"right: {start}")
                #print(f"calculating: {heights[i]} - {heights[start]}")
                distance = start - i
                #print(f"distance between: {distance}")
                both = [heights[i], heights[start]]
                both.sort()
                #print(both)
                area = both[0] * distance
                results.append(area)

                start -= 1

        results.sort()
        #print(results)
        return results[-1]
                

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))