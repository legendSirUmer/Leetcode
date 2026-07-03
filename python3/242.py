from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = Counter(s)
        ans2 = Counter(t)

        if(ans == ans2):
            return True
        return False