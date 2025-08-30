#MEDIUM 


# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.




class Solution: # Done / Beats 100%
    def myAtoi(self, s: str) -> int:
        if(s == ''):
            return 0
        s = s.strip()
        ans = ''        
        i = 0
        Numbers = {'0','1','2','3','4','5','6','7','8','9'}
        while(i != len(s)):

            if(s[i] == '-' and i == 0):
                i+=1
                ans+= '-'

            elif(s[i] == '+' and i == 0):
                i+=1
                
            elif(s[i] == '0'):
                i+=1

            elif(s[i] in Numbers):
                break
            else:
                return 0
            
        if(i == len(s)):
            return 0

        while(i != len(s) and s[i] in Numbers ):
            ans += s[i]
            i+=1

        final = int(ans)
        
        INT32_MIN = -2147483648
        INT32_MAX = 2147483647


        return max(INT32_MIN, min(INT32_MAX, int(final)))

                

                
sol = Solution()
print(sol.myAtoi("words and 987"))
print(sol.myAtoi("1337c0d3"))
print(sol.myAtoi("42"))
print(sol.myAtoi("   -042"))
print(sol.myAtoi("0-1"))
print(sol.myAtoi(""))
print(sol.myAtoi("000abc"))
print(sol.myAtoi("--"))



