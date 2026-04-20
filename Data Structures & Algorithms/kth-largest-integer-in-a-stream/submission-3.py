class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return val

        i=0
        j=len(self.nums)-1
        print("i",i)
        print("j",j)
        while i<=j:
            if val>=self.nums[-1]:
                print('if 1 here',j)
                self.nums.append(val)
                break
            elif val<self.nums[i]:
                print('elif 1 here')
                self.nums.insert(0,val)
                break
            elif val>self.nums[i] and val<self.nums[i+1]:
                print('elif 2 here')
                self.nums.insert(i+1,val)
                break
            elif val==self.nums[i+1]:
                print('elif 3 here')
                self.nums.insert(i+1,val)
                break
            i+=1
        print(self.nums)
        if self.k>len(self.nums):
            return self.nums[-1]
        return self.nums[-self.k]
            

