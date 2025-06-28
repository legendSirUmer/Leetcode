import collections
from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
          
        copy = nums.copy()
        
        for i in range(0,k):
            minimum = 9999999999
            for j in range(len(copy)-1):
                if(minimum > copy[j]):
                    minimum = copy[j]
                    copy.remove(copy[j])
            
        return copy
        
    
            




print(Solution().maxSubsequence([3,1,-2,34,5,6],3))  