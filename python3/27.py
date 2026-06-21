from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in range(len(nums)):
            if(nums[i] == val):
                continue
            else:
                ans.append(nums[i])  
                             
        nums.clear() 
        nums.extend(ans)

        return len(ans)

        
sol = Solution()




a = [0,1,2,2,3,0,4,2]

print(sol.removeElement(a,2))
print(a)