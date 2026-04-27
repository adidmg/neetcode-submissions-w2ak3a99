class Solution:
    fact_dict={0:1,1:1,2:2,3:6,4:24,5:120}

    def factorial(self,num):
        if num in self.fact_dict:
            self.fact_dict[num]
            return self.fact_dict[num]
        fact=num*self.factorial(num-1)
        self.fact_dict[num]=int(fact)
        print('factorial',fact)
        return int(fact)

    def climbStairs(self, n: int) -> int:
        count=0
        num_ones=n
        num_places=n
        num_twos=0
        even=False
        if n%2==0:
            count+=2
            even=True
        else:
            count+=1
        num_ones-=2
        num_places-=1
        num_twos+=1
        while num_ones>0:
            result=int(self.factorial(num_places)/(self.factorial(num_ones)*self.factorial(num_twos)))
            count+=result
            num_ones-=2
            num_places-=1
            num_twos+=1
        return int(count)
        




