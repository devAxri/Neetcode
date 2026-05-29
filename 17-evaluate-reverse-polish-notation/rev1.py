from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = []
        operators = ["+", "-", "*", "/"]
        for num in tokens:
            if num not in operators:
                total.append(int(num))
        
            else:
                if num == "+":
                    total.append(total.pop() + total.pop())
                if num == "-":
                    sub_num = total[-2] - total[-1]
                    total.pop()
                    total.pop()
                    total.append(sub_num)
                if num == "*":
                    total.append(total.pop() * total.pop())
                if num == "/":
                    div_num = total[-2] / total[-1]
                    total.pop()
                    total.pop()
                    total.append(int(div_num))

        return total[0]

sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))