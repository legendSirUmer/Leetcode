# Runtime
# 1
# ms
# Beats
# 56.61%
# Memory
# 20.72
# MB
# Beats
# 16.45%



from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        p = 1
        ans = []
        curr = nums[0]
        ans.append(curr)
        if len(nums) > 1:
            for i in range(1,len(nums)):
                if nums[i] != curr:
                    curr = nums[i]
                    ans.append(curr)
                    p+=1
                    
        nums = ans
        return p



sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

