

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a  = s.strip()
        b = a.split(" ")
        # print(b)
        return len(b[-1])
        





sol = Solution()
sol.lengthOfLastWord("      Hello World")