class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_ind={}
        for i,n in enumerate(nums):
            num_ind[n]=i
        for i,n in enumerate(nums):
            j=target-n
            if j in num_ind and num_ind[j]!=i:
                return [i, num_ind[j]]
        return[]




        
        