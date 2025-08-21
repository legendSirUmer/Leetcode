class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                if result[i + j] >= 10:
                    result[i + j + 1] += result[i + j] // 10
                    result[i + j] %= 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return ''.join(map(str, result[::-1])) if result else '0'
    










# Example usage:
sol = Solution()
print(sol.multiply("123", "456"))  # Output: "56088"