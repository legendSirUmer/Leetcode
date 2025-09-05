#NOT COmpleted




class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i1,i2,i3 = 0,0,0
        answer = True

        if(len(s3) != len(s1) + len(s2)):
             return False

        if(s1 == ''):
             if(s3 == s2):
                  return True
             
             return False
        if(s2 == ''):
             if(s3 == s1):
                  return True
             return False

        for i in range(len(s3)):
            if(i1 == len(s1)):
                 break
            if(i2 == len(s2)):
                 break
                 

            if(s3[i3] == s2[i2]):
                    i3+=1
                    i2+=1
            elif(s3[i3] == s1[i1]):
                    i3+=1
                    i1+=1
            else:
                answer = False
                return answer
        if(i3 < len(s3)-1):   
            return False
        else:
             return answer



sol = Solution()
# print(sol.isInterleave('aabcc','dbbca','aadbbcbcac'))
# print(sol.isInterleave('aabcc','dbbca',"aadbbbaccc"))
print(sol.isInterleave('aaa','bbb',"bbbbbb"))
print(sol.isInterleave('a','b',"a"))



        
