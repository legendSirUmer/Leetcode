# BRUTE FORCE SOLUTION NOT ACCEPTED
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ''
#         for a in range(len(s)):
#             for x in range(len(s)+1,1,-1):
#                 #print(s[:x:])
#                 #print(s[a:x:] + ' '  + ''.join(reversed(s[a:x:])) )
#                 if s[a:x:] == ''.join(reversed(s[a:x:])):
                    
#                     if len(s[a:x:]) > len(ans):
#                         ans = s[a:x:]
#                         break
                    
#         return ans








sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("a"))