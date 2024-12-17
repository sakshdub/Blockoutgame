class Solution(object):
    def mergeAlternately(self, word1, word2):

        result=[]
        len1,len2=len(word1),len(word2)
        min_len=min(len1,len2)
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        if len1>len2:
            result.append(word1[min_len:])
        else:
            result.append(word2[min_len:])
        return ''.join(result)


word1="abc"
word2="pqrst"
sol=Solution()
j=sol.mergeAlternately(word1,word2)
print(j)