class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=-1
        first=-len(digits)
        while i>=first:
            if digits[i]==9:
                digits[i]=0
                if i==first:
                    digits.insert(0,1)
                    break
                i-=1
                continue
            digits[i]+=1
            break
        return digits