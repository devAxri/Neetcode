from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        punctuations = [".", "!", "?", ",", ":", ";", "\"", "\'", " "]
        for _ in range(len(punctuations)):
            s = s.replace(punctuations[_], "")
        
        s_normal = s
        s_reversed = s[::-1]
        return s_normal == s_reversed
    
sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))