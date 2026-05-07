class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output={}
        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i)-97]+=1
            count=tuple(count)
            if count not in output:
                output[count]=[word]
            else:
                output[count].append(word)
        return list(output.values())
        