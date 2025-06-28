from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(0,len(nums)):
        num = target - nums[i]
        copy = nums.copy()
        copy[copy.index(nums[i])] = None
       

        if(num in copy):
            answer.append(i)
            answer.append(copy.index(num))
            break
        
    return answer



li = []
for i in range(1,10001):
    li.append(i)

print(twoSum(None, li, 19999))  # Example usage, should return [0,1] since nums[0] + nums[1] = 9