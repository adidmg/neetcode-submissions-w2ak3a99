class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dict={1:[],2:[]}
        if len(nums)==1:
            return nums[0]
        for i in nums:
            if i in freq_dict[1]:
                freq_dict[2].append(i)
                freq_dict[1].remove(i)
            else:
                freq_dict[1].append(i)
        return freq_dict[1][0]
        