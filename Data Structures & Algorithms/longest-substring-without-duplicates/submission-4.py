class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left=0
        seen=set()
        output=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            curr=(right-left)+1
            output=max(output, curr)
            seen.add(s[right])
        return output
                