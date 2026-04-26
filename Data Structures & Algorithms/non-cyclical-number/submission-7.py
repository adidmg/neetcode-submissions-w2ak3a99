class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            num_str=str(n)
            total=0
            for i in num_str:
                total+=pow(int(i),2)
            if total==1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n=total
        return True