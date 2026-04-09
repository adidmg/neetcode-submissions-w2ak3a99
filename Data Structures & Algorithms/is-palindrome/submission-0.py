class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_word="".join([x.lower() for x in s if x.isalnum()])
        j=len(cleaned_word)-1
        i=0
        while i<j:
            if cleaned_word[i]!=cleaned_word[j]:
                return False
            i+=1
            j-=1
        return True
        