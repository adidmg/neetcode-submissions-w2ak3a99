class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r=0 ,len(matrix)-1
        while l<=r:
            mid=(l+r)//2
            if target<matrix[mid][-1]:
                matrix_set=set(matrix[mid])
                if target in matrix_set:
                    return True
                else:
                    r=mid-1
            elif target>matrix[mid][-1]:
                l=mid+1
            elif target==matrix[mid][-1]:
                return True
        return False
        