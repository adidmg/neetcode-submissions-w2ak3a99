class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums=set(nums)
        sum_set=sum(set_nums)
        sum_nums=int((len(nums)*(len(nums)+1))/2)
        if 0 not in set_nums:
            return 0
        return sum_nums-sum_set
        