class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            prod1=math.prod(nums[:i])
            prod2=math.prod(nums[i+1:])
            output.append(int(prod1*prod2))
        return output