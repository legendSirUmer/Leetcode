class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(s == None or numRows <= 0):
            return ''
        if(numRows == 1):
            return s
     
        matrix = [['' for _ in range(len(s))] for _ in range(numRows)]

        if(numRows ==2 ):
            ans = s[::2] + s[1::2]
            return ans
 
        i,j,t = 0,0,0
        while(t != len(s)):


            if(i == numRows-1):
                for a in range(numRows):
                    if(t == len(s)):
                        break

                    matrix[i][j] = s[t]
                    if(i != 0 ):
                        i-=1 
                    else:
                        i+=1
                    t+=1
                    if(a != numRows-1):
                        j+=1

            else:
                matrix[i][j] = s[t]
                t+=1
                i+=1



        ans = ''
        for u in matrix:
            for b in u:
                if(b != None):
                    ans+= b
        return ans
    




sol = Solution()
print(sol.convert('PAYPALISHIRING',3))
print(sol.convert('PAYPALISHIRING',4))
print(sol.convert('A',1))
print(sol.convert('AB',1))
print(sol.convert('AB',2))

            




        
