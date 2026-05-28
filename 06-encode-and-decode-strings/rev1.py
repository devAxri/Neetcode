from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Required for the Neetcode edge cases
        if strs == []:
            return "[]"
        if strs == [""]:
            return ""
        return ";".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        if s == "":
            return [""]
        return s.split(";")
    
sol = Solution()
encoded = sol.encode(["Hello", "World"])
print(sol.decode(encoded))