class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pi =0
        si = 0
        answer = True

        while (pi != len(p) and si != len(s)):

            

            if(p[pi] != '*'):
                if(p[pi] != s[si] and p[pi] != '.'):
                    answer = False
                    break
                    si +=1
                    pi +=1
                else:

                    si +=1
                    pi +=1
            
            else:
                if (p[pi-1] == '.'):
                    si +=1
                else:
                    while(p[pi-1] == s[si] ):
                        si +=1
                        if(si == len(s)):
                            break
                    
                    pi+=1
            
            if(pi == len(p) and si != len(s) ):
                answer = False 
            

        return  answer


sol = Solution()
print(sol.isMatch('aa','a'))
print(sol.isMatch('aa','a*'))
print(sol.isMatch('ab','.*'))
print(sol.isMatch("mississippi","mis*is*p*."))
print(sol.isMatch("aab","c*a*b"))