


from typing import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        answers=  []

        for i in strs:
            answers.append(Counter(i))

        for i in answers:
            if(i )



