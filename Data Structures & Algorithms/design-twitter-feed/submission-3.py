class Twitter:

    def __init__(self):
        self.user_to_user = defaultdict(lambda: defaultdict(bool))
        self.user_to_post = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_to_post:
            self.user_to_post[userId] = []
            heapq.heapify(self.user_to_post[userId])
        h = self.user_to_post[userId]
        heapq.heappush(h, (self.timestamp, tweetId))
        while len(h) > 10:
            heapq.heappop(h)
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = list(self.user_to_user[userId]) + [userId]
        # combine all in a heap of size 10? 
        result = []
        heapq.heapify(result)
        for followee in follows:
            # for each user, pop last 10 
            # print(heapq.nsmallest(10, self.user_to_post[followee]))
            if followee not in self.user_to_post:
                continue
            timeline = self.user_to_post[followee]
            for post in timeline: 
                heapq.heappush(result, post)
            # add all to heap ensuring size never exceeds 10
            while len(result) > 10:
                heapq.heappop(result)
            
        sortedTimeline = []
        while len(result) > 0:
            timestamp, post_id = heapq.heappop(result)
            sortedTimeline.append(post_id)

        return sortedTimeline[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_user[followerId][followeeId] = True
    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_to_user[followerId]:
            del self.user_to_user[followerId][followeeId] 
        
