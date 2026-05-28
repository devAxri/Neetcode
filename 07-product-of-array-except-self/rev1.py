from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_array = []

        for i in range(len(nums)):
            where_at = 0
            num = 1
            
            for m in range(len(nums)):
                if i != where_at:
                    num = num*nums[m]
                    
                where_at+=1
                
            return_array.append(num)

        return return_array

sol = Solution()
print(sol.productExceptSelf([1,2,4,6]))