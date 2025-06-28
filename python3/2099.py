import collections
from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        copy = nums.copy()
        for i in range(0,len(copy)-k):
            copy.remove(min(copy))
   
        return copy
            




print(Solution().maxSubsequence([3,1,-2,34,5,6],3))  