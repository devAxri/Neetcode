from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #height_reversed = height.copy()
        #height_reversed.reverse()

        result = []
        
        for i in range(len(height)):
            if i == 0:
                max_left = 0
            else:
                max_left = max(height[0:i])
            max_right = max(height[i:])

            calculation = min(max_left, max_right) - int(height[i])
            if calculation > 0:
                result.append(calculation)
    
            # min(L, R) - h[i]
            # result.append(int(min(max_left, max_right)) - int(height[i]))

        return sum(result)

sol = Solution()
print(sol.trap([0,2,0,3,1,0,1,3,2,1]))