class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        answer=[]
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left, right= i+1, n-1

            while left<right:
                sum_num=nums[i]+nums[left]+nums[right]
                if sum_num==0:
                    answer.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left]== nums[left-1]:
                        left+=1
                    while left<right and nums[right]== nums[right+1]:
                        right-=1
                elif sum_num>0:
                    right-=1
                else:
                    left+=1
        return answer
                    