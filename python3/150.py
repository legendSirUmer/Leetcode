#150. Evaluate Reverse Polish Notation
# Medium
# Topics
# premium lock icon
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.



from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for i in tokens:

            if(i == "/"):
                num = (stack[-2] // stack[-1] )
                stack.pop()
                stack.pop()
                if num > 0 and num < -1:
                    stack.append(num)
                else:
                    stack.append(0)

            elif (i == "*"):
                num = (stack[-2] * stack[-1] )
                stack.pop()
                stack.pop()
                stack.append(num)

            elif(i == "+"):
                num = (stack[-2] + stack[-1] )
                stack.pop()
                stack.pop()
                stack.append(num)

            elif(i == "-"):
                num = (stack[-2] - stack[-1] )
                stack.pop()
                stack.pop()
                stack.append(num)

            else:
                stack.append(int(i))

        return stack[-1]



sol = Solution()
#sol.evalRPN(["4","13","5","/","+"])
print(sol.evalRPN(["4","-2","/","2","-3","-","-"]))