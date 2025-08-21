from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t_sum = str(digits)
        t_sum = int(t_sum.replace('[', '').replace(']', '').replace(',', '').replace(' ', '')) + 1
        t_sum = str(t_sum)
        t_sum = [int(i) for i in t_sum]
        return t_sum
            





sol =  Solution()
# Example usage:sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([9, 9, 9]))   # Output: [1, 0, 0, 0]

       