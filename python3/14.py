from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        if strs == [""]:
            return answer
        if(len(strs) == 1):
            return strs[0]
        prefix = strs[0]

        for i in range(len(prefix)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != prefix[i]:
                    return answer
            answer += prefix[i]

    

 
    






# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"])) 
print(sol.longestCommonPrefix([""])) # Output: "fl"