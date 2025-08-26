from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        search = nums2[0]

        l=0
        r=len(nums1)
        m=l+r/2

        new_list = nums1 + nums2
        new_list.sort()
        median = 0.0
        l = len(new_list)
        if(l % 2 == 0):
            median = (new_list[int(l/2)] + new_list[int(l/2) -1])/ 2
        else:
            median = new_list[int(l/2)]
        return median


        
sol = Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))
        