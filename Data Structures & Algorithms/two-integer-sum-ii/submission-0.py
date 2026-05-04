class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        i=0
        while i<len(numbers):
            j=(target-numbers[i])
            if j in numbers:
                output.append(i+1)
                output.append(numbers.index(j)+1)
                break
            i+=1
        return output