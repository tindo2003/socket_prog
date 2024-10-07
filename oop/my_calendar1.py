class MyCalendar:
    def __init__(self):
        self.interval_list = []
    # INTERVAL

    def book(self, start: int, end: int) -> bool:
        if not self.interval_list: 
            self.interval_list.append([start, end])
            return True
        def binary_search(tgt_start):
            l, r = 0, len(self.interval_list) - 1
            ans = 0
            while l <= r:
                mid = (l + r) // 2
                cur_start, cur_end = self.interval_list[mid][0], self.interval_list[mid][1] 
                if cur_start <= tgt_start:
                    l = mid + 1
                    ans = mid
                else:
                    r = mid - 1
            return ans 
        idx = binary_search(start)
     
        cur_start, cur_end = self.interval_list[idx][0], self.interval_list[idx][1]
        if start > cur_start and start >= cur_end:
            if idx + 1 < len(self.interval_list):
                right_start, right_end = self.interval_list[idx + 1][0], self.interval_list[idx + 1][1] 
                if right_start >= end:
                    self.interval_list.insert(idx+1, [start, end])
                    return True 
            else:
                self.interval_list.insert(idx+1, [start, end])
                return True 
        elif start < cur_start and cur_start >= end:
            if idx - 1 >= 0:
                left_start, left_end =  self.interval_list[idx - 1][0], self.interval_list[idx - 1][1]  
                if start >= left_end:
                    self.interval_list.insert(idx, [start, end])
                    return True   
            else:
                self.interval_list.insert(idx, [start, end])
                return True  
        return False 

def main():
    c = MyCalendar()
    itv_list = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    for itv in itv_list:
        c.book(itv[0], itv[1])
        print(c.interval_list) 

if __name__ == "__main__":
    main()

