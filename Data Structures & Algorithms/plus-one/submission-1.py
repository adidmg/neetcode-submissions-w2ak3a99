class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=True
        i=-1
        digit_len=-(len(digits))
        while carry:
            if digits[i]==9:
                digits[i]=0
                if i==digit_len:
                    carry=False
                    digits.insert(0,1)
                i-=1
            else:
                digits[i]+=1
                carry=False
        return digits