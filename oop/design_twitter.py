from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
       self.time = 0 
       self.follower_list = defaultdict(set) # userid ->[userids that they follow]
       self.tweets = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((tweetId, self.time))


    def getNewsFeed(self, userId: int) -> List[int]:
        my_tweets =  self.tweets[userId].copy()
        my_friends = self.follower_list[userId]
        for id in my_friends:
            my_tweets.extend(self.tweets[id])
        my_tweets.sort(key=lambda x: x[1], reverse=True)

        return [tweetId for tweetId, time in my_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_list[followerId]:
            self.follower_list[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)