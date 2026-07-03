class Solution:
    def processStr(self, s: str, k: int) -> str:
        result = ""

        for i in s:
            if i == "#":
                result = result+result
            elif i == "*":
                result = result[:len(result)-1]
            elif i == "%":
                result = result[::-1]
            else:
                result = result + i


        if(k < len(result)):
            return result[k]
        
        return "."
    
sol = Solution()
print(sol.processStr("a#b%*",1))
print(sol.processStr("cd%#*#",3))