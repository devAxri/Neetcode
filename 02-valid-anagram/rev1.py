class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = list(s)
        t_chars = list(t)
        s_chars.sort()
        t_chars.sort()
        if s_chars == t_chars:
            return True
        return False

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))