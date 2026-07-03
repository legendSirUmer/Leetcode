# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         pi =0
#         si = 0
#         answer = True

#         while (pi != len(p) and si != len(s)):

            

#             if(p[pi] != '*'):
#                 if(p[pi] != s[si] and p[pi] != '.'):
#                     answer = False
#                     break
#                     si +=1
#                     pi +=1
#                 else:

#                     si +=1
#                     pi +=1
            
#             else:
#                 if (p[pi-1] == '.'):
#                     si +=1
#                 else:
#                     while(p[pi-1] == s[si] ):
#                         si +=1
#                         if(si == len(s)):
#                             break
                    
#                     pi+=1
            
#             if(pi == len(p) and si != len(s) ):
#                 answer = False 
        
#         return  answer




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        ans = False
        count = 0
        while i < len(p) and count < len(s):

            if(i < len(p) -1 and p[i+1] == '*'):
                if(p[i] == '.'):
                    if(i < len(p) -2):
                        while( count < len(s)-1 and s[count] != p[i+2]):
                            count+=1
                        if(s[count] == p[i+2]):
                            ans = self.isMatch(s[count::],p[i+2])
                    else:
                        ans = True
           



                while(count < len(s) and s[count] == p[i]):
                    count +=1
                
                if(i < len(p)-2 and p[i] == p[i+2]):
                    i+=1
                i+=2

            elif(p[i] == '.'):
                count+=1
                i+=1
            elif(p[i] == s[count]):
                count+=1
                i+=1
            else:
                i+=1


        if(count == len(s) and i == len(p) ):
            ans = True
        
        return ans



sol = Solution()

#print(sol.isMatch("aab","c*a*b"))
#print(sol.isMatch("ab",".*c"))
print(sol.isMatch('aaa',"ab*a*c*a"))