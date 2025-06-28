
def isPalindrome(self, x: int) -> bool:
    num = x.__str__()
    for i in range(0, len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True
        
       





print(isPalindrome(None, 12321) )