class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for i in nums:
            freq_dict[i]=1+freq_dict.get(i,0)
        freq_heap=[]
        for i in freq_dict.keys():
            heapq.heappush(freq_heap,(freq_dict[i],i))
            if len(freq_heap)>k:
                heapq.heappop(freq_heap)
        output=[]
        for i in range(k):
            output.append(heapq.heappop(freq_heap)[1])
        return output