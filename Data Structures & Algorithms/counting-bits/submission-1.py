class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]

        output=[0]*(n+1)
        exp=0
        i=1
        while i<=n:
            pow2=pow(2,exp)
            if i==pow2:
                output[i]=1
                i+=1
                exp+=1
                continue
            if i<pow2:
                output[i]=1+output[i-pow(2,exp-1)]
                i+=1
        return output
                

