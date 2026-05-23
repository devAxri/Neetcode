from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            num1 = nums[i]
            startLeft = i + 1
            startRight = len(nums) - 1
            
            while startLeft < startRight:
                num2 = nums[startLeft]
                num3 = nums[startRight]
                
                total = num1+num2+num3
                
                if total < 0:
                    startLeft += 1
                elif total > 0:
                    startRight -= 1
                else:
                    startLeft += 1
                    startRight -= 1
                    list_n = [num1,num2,num3]
                    if list_n not in result:
                        result.append([num1,num2,num3])
        
        return result

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))