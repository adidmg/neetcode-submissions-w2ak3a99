class Solution:
    def reverseBits(self, n: int) -> int:
        n_lst=[]
        while n:
            if n%2==1:
                n_lst.append("1")
            else:
                n_lst.append("0")
            n=n>>1
        n_lst.append("0"*(32-len(n_lst)))
        return int(''.join(n_lst),2)
        