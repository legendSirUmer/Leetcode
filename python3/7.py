class Solution:
    def reverse(self, x: int) -> int:
        if(x == 0):
            return 0

        if(x > 0):
            integer = str(x)
            reverse = integer[::-1]
            if(int(reverse) >= 2**31 ):
                return 0
            
            return int(reverse)
        elif(x < 0):
            integer = str(x)
            
            reverse = integer[::-1]
            if(-int(reverse[:-1:]) <= -2**31):
                return 0
            return -int(reverse[:-1:])


sol = Solution()
print(sol.reverse(-123456785))
print(sol.reverse(-2147483648))
