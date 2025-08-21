from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_d = 0
        number = 0
        for i in nums:
            if i == 0:
                return 0
            if abs(i) < min_d or min_d == 0:
                min_d = abs(i)
                number = i
            elif abs(i) == min_d:
                number = max(number, i)
        
            
        
        return number
