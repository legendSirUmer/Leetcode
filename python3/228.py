from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = nums[0]
        end = ''
        for i in range(len(nums)-1):
            
            if(nums[i]+1 == nums[i+1]):
                end = nums[i+1]
            
            else:
                if(end == ''):
                    ans.append(str(start))
                    start = nums[i+1]
                else:
                    ans.append(str(start)+'->' +str(end))
                    start = nums[i+1]
                    end = ''
        
        if(end == ''):
            ans.append(str(start))
        else:
            ans.append(str(start)+'->' +str(end))
            

        return ans



sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))
print(sol.summaryRanges([0,2,3,4,6,8,9]))



