class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i=0
        j=1
        seen={s[i]:None}
        output=0
        while j<len(s):
            if s[j] in seen:
                output=max(output,len(seen))
                i+=1
                seen={s[i]:None}
                j=i+1
            else:
                seen[s[j]]=None
                j+=1
        return max(output,len(seen))