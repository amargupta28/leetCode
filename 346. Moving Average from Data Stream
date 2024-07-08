class MovingAverage:

    def __init__(self, size: int):
        self.avg=size
        self.arr=[]
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        if len(self.arr) > self.avg:
            self.arr.pop(0)
        s=0
        for i in self.arr:
            s+=i
        return (s/(len(self.arr)))
        
       

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
