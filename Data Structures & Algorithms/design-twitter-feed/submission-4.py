class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        h = self.tweets[userId]
        heapq.heappush(h, (self.timestamp, tweetId))
        while len(h) > 10:
            heapq.heappop(h)
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for followee_id in self.following[userId] | {userId}:
            for tweet in self.tweets[followee_id]:
                heapq.heappush(feed, tweet)

                if len(feed) > 10:
                    heapq.heappop(feed)
        
        result = []
        while feed:
            _, tweet_id = heapq.heappop(feed)
            result.append(tweet_id)

        return result[::-1]
          

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
