class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i]=1
            else:
                freq_dict[i]+=1
        freq_heap=[(freq_dict[i],i) for i in freq_dict]
        heapq.heapify_max(freq_heap)
        output=[]
        for i in range(k):
            (val,key)=heapq.heappop_max(freq_heap)
            output.append(key)
        return output