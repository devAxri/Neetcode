from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find all anagrams
        dict_ana = {}
        for i in range(len(strs)):
            chars = list(strs[i])
            chars.sort()
            chars_tg = "".join(chars)
            if chars_tg in dict_ana:
                for x in dict_ana:
                    if x == chars_tg:
                        dict_ana[x] = dict_ana[x]+";"+strs[i]
                    
            else:
                dict_ana[chars_tg] = strs[i]
        
        big_list = []
        for ls in dict_ana:
            split_ls = dict_ana[ls].split(";")
            small_list = []
            for word in split_ls:
                small_list.append(word)

            big_list.append(small_list)

        return big_list

sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))