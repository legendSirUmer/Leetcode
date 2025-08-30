from typing import List
class Solution:




    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        med = 0.0

        def Median(new_list : List[int]) -> float:
            median = 0.0
            l = len(new_list)
            if(l % 2 == 0):
                median = (new_list[int(l/2)] + new_list[int(l/2) -1])/ 2
            else:
                median = new_list[int(l/2)]
            return median

        if(nums1 == None):
            med = Median(nums2)
            
        elif(nums2 == None):
            med = Median(nums1)
        else:
            new_list = nums1 + nums2
            new_list.sort()
            med = Median(new_list)

        return med


        

        


        


        
sol = Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))
        