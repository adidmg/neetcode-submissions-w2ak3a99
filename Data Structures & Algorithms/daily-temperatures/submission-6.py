class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        max_temp=[]
        for i,t in enumerate(temperatures):
            while max_temp and t>max_temp[-1][-1]:
                index,temp=max_temp.pop()
                output[index]=i-index
            max_temp.append((i,t))        
        return output