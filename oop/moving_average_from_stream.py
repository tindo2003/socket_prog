from collections import deque 
class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.arr = deque([])
        self.cur_sum = 0 
        self.size = size

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.cur_sum += val 
        self.arr.append(val)
        if len(self.arr) > self.size:
            res = self.arr.popleft()
            self.cur_sum -= res
        return self.cur_sum / len(self.arr)