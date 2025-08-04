# from collections import Counter
# class Solution:
#     def isValid(self, s: str) -> bool:
#         a = Counter(s)
#         # print(a)
        
#         if(a['('] == a[')'] and a['['] == a[']'] and a['{'] == a['}']):
#             return True
#         else:
#             return False




class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2:
                if (stack[-1] == ')' and stack[-2] == '(') or \
                   (stack[-1] == ']' and stack[-2] == '[') or \
                   (stack[-1] == '}' and stack[-2] == '{'):
                    stack.pop()
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
