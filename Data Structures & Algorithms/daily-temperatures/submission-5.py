class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        max_temp=[(temperatures[0],0)]
        for i in range(1,len(temperatures)):
            if temperatures[i]>max_temp[-1][0]:
                while max_temp and temperatures[i]>max_temp[-1][0]:
                    output[max_temp[-1][-1]]=(i-max_temp[-1][-1])
                    max_temp.pop()
                max_temp.append((temperatures[i],i))
            else:
                max_temp.append((temperatures[i],i))        
        return output