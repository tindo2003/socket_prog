class TweetCounts:

    def __init__(self):
        self.map = defaultdict(SortedList)
        self.freq_to_num = {"minute": 60, "hour": 3600, "day": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.map[tweetName].add(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        res = []
        cur_lst = self.map[tweetName]
        d = self.freq_to_num[freq]
        cur = startTime
        while cur <= endTime:
            left_idx = cur_lst.bisect_left(cur)
            right_idx = cur_lst.bisect_left(min(cur + d, endTime + 1))
            res.append(right_idx - left_idx)
            cur += d
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
