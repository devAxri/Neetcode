from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_amount = {}
        for x in nums:
            if x not in dict_amount:
                dict_amount[x] = 1

            else:
                dict_amount[x] = dict_amount[x]+1

        sorted_dict = sorted(dict_amount.items(), key=lambda item: item[1])
        sorted_dict.reverse()
        
        list_sorted = []
        for _ in range(k):
            list_sorted.append(sorted_dict[_][0])
        
        return list_sorted

sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))