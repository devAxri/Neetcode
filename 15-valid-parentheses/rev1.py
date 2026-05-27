class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        seen = []

        for char in s:
            if char in opening:
                seen.append(char)
            else: # we can assume its a closing one
                if len(seen) == 0:
                    return False
                if seen[-1] != parentheses[char]:
                    return False

                seen.pop()

        #print(seen)
        return seen == []
        
sol = Solution()
print(sol.isValid("([{}])"))