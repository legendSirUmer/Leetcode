# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


#COMPLETED 0ms BEST SOLUTION

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0

        for i in t:
            if(j == len(s)):
                return True
            if i == s[j]:
                j+=1
            
        if(j == len(s)):
             return True 
        else:
             return False
    



sol = Solution()
print(sol.isSubsequence('abc',"ahbgdc"))