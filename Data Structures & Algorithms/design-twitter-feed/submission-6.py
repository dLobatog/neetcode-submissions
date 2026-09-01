class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets[userId]
        tweets.append((self.timestamp, tweetId))
        while len(tweets) > 10:
            tweets.pop(0)
            
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for followee_id in self.following[userId] | {userId}:
            tweets = self.tweets[followee_id]

            if not tweets:
                continue

            index = len(tweets) - 1
            timestamp, tweet_id = tweets[index]    
            
            heapq.heappush(feed, (-timestamp, tweet_id, followee_id, index-1))
        
        result = []
        while feed and len(result) < 10:
            _, tweet_id, followee_id, index = heapq.heappop(feed)
            result.append(tweet_id)

            if index >= 0:
                timestamp, next_tweet_id = self.tweets[followee_id][index]

                heapq.heappush(
                    feed,
                    (-timestamp, next_tweet_id, followee_id, index - 1),
                )

        return result
          

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
