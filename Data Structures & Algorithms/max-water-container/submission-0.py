class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=[0]
        heapq.heapify(max_water)
        for i in range(len(heights)):
            left=i
            right=len(heights)-1
            while left!=right:
                water=(right-left)*(min(heights[left],heights[right]))
                heapq.heappush(max_water,water)
                if len(max_water)>1:
                    heapq.heappop(max_water)
                right-=1
        return max_water[0]