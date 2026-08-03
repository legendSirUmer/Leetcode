#solved

from typing import Counter 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict  = Counter(text)

        arr = ['b','a','l','o','n']
        ans = []
        for i in range(len(arr)):       
                if(arr[i] == 'l' or arr[i] == 'o'):
                    ans.append(dict[arr[i]]//2)
                               
                else:
                    ans.append(dict[arr[i]])


        return min(ans)
    



sol = Solution()
#print(sol.maxNumberOfBalloons('balon'))
print(sol.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))