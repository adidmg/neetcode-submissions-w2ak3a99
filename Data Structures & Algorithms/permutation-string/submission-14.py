class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ord=[0]*26
        s2_ord=[0]*26

        len_s1=len(s1)
        len_s2=len(s2)

        if len_s1>len_s2:
            return False

        for i in range(len_s1):
            s1_ord[ord(s1[i])-97]+=1
            s2_ord[ord(s2[i])-97]+=1

        if s1_ord==s2_ord:
            return True
        
        for i in range(len_s1,len_s2):
            s2_ord[ord(s2[i])-97]+=1
            s2_ord[ord(s2[i-len_s1])-97]-=1

            if s1_ord==s2_ord:
                return True

        return False
            