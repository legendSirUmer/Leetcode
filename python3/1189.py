from typing import Counter 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict  = Counter(text)

        arr = ['b','a','l','o','n']
        min = float('inf')
        for i in range(len(arr)):
            if(dict[arr[i]] <= min):
                if(arr[i] == 'l' or arr[i] == 'o'):
                    min = dict[arr[i]]//2
                else:
                    min = dict[arr[i]]


        return min
    



sol = Solution()
#print(sol.maxNumberOfBalloons('balon'))
print(sol.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))