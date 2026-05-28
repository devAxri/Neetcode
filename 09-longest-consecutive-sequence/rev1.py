from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return 0 if nums == []
        if len(nums) == 0:
            return 0

        nums.sort() # sort

        num_store = []
        for i in range(len(nums)):

            #print(f"num_store: {num_store}")
            #print("running for number " + str(nums[i]))
            has_hit = False

            for o in range(len(num_store)):
                last_in_list = num_store[o][-1]
                last_in_list_p_1 = last_in_list + 1
                #print(f"last in list + 1: {last_in_list_p_1}")

                if (last_in_list_p_1 == nums[i]):
                    #print(f"num_store: {num_store[o]}")
                    num_store[o].append(nums[i])
                    #print("hit")
                    has_hit = True
                    #print(f"num_store (added): {num_store[o]}")
                    break
        
            if not has_hit:
                num_store.append([nums[i]])

        # calc which is the longest
        longest = 0
        for p in range(len(num_store)):
            #print(f"len(num_store[p]) == {len(num_store[p])}")
            #print(f"longest == {longest}")
            if len(num_store[p]) > longest:
                longest = len(num_store[p])

        return longest
    
sol = Solution()
print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))