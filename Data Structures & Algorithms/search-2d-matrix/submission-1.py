class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r=0 ,len(matrix)-1
        while l<=r:
            mid=(l+r)//2
            print("mid",matrix[mid][-1])
            if target<matrix[mid][-1]:
                matrix_set=set(matrix[mid])
                print("matrix_set",matrix_set)
                if target in matrix_set:
                    return True
                else:
                    print("left porition")
                    r=mid-1
            elif target>matrix[mid][-1]:
                l=mid+1
            elif target==matrix[mid][-1]:
                return True
        return False
        