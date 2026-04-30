class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict={}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i]=1
            else:
                freq_dict[i]+=1
        freq_heap=[]
        for i in freq_dict:
            heapq.heappush(freq_heap,(freq_dict[i],[i]))
            if len(freq_heap)>k:
                heapq.heappop(freq_heap)
        output=[]
        for i in range(k):
            val,key=heapq.heappop(freq_heap)
            output.append(key[0])
        return output