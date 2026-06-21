




#comepleted best Solution


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if(word2 == None or word2 == ''):
            return word1 
        if(word1 == None or word1 == ''):
            return word2

        ans = ''
        i,j=0
        while(i != len(word1) or j != len(word2)):
            if(i != len(word1)):
                ans+=word1[i]
                i+=1
            if(j!= len(word2)):
                ans+=word2[j]
                j+=1
        
        return ans





        