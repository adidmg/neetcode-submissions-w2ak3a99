class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        sorted_nums=sorted(nums)
        print(sorted_nums)
        conseq=0
        curr_conseq=1
        i=0
        j=1
        while j<len(sorted_nums):
            
            if sorted_nums[j]==sorted_nums[i]+1: 
                curr_conseq+=1
            elif sorted_nums[j]==sorted_nums[i]:
                i+=1
                j+=1
                continue
            else:
                conseq=max(conseq,curr_conseq)
                curr_conseq=1
            i+=1
            j+=1

        return max(conseq,curr_conseq)
        