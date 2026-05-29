from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = []
        for num in tokens:
            if num == "+":
                total.append(total.pop() + total.pop())
            elif num == "-":
                sub_num = total[-2] - total[-1]
                total.pop()
                total.pop()
                total.append(sub_num)
            elif num == "*":
                total.append(total.pop() * total.pop())
            elif num == "/":
                div_num = total[-2] / total[-1]
                total.pop()
                total.pop()
                total.append(int(div_num))
            else:
                total.append(int(num))

        return total[0]

sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))