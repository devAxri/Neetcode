from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        
        nums.sort()
        
        for i in range(len(nums)):
            num1 = nums[i]
            #print(f"num1 = {num1}")
            for m in range(len(nums)):
                if m == i:
                    continue
                num2 = nums[m]
                #print(f"num1 = {num2}")
                for o in range(len(nums)):
                    if o == i or o == m:
                        continue
                    num3 = nums[o]
                    #print(f"num1 = {num3}")
                    
                    if num1 + num2 + num3 == 0:
                        to_sort = [num1, num2, num3]
                        to_sort.sort()
                        if to_sort not in return_list:
                            return_list.append(to_sort)
                    
                    #print(num1+num2+num3)

        return return_list

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))