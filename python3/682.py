from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Stack = []
        Ptr= -1

        for i in operations:                            

            if i == "C":
                if Stack is not None:
                    Stack.pop()
                    Ptr -=1

            elif i == "D":
                Stack.append(Stack[Ptr] *2)
                Ptr +=1

            elif i == "+":
                if(len(Stack) >1 ):
                    Stack.append(Stack[Ptr] + Stack[Ptr-1])
                    Ptr +=1
            else:
                Stack.append(int(i))
                Ptr +=1


        return sum(Stack)



sol = Solution()
sol.calPoints(["5","-2","4","C","D","9","+","+"])