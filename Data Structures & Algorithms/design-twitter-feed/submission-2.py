class User:
    def __init__(self):
        self.posts = [] #
        self.follows = set() #ids

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User()
        
        self.users[userId].posts.append((-self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User()
        collect = self.users[userId].posts.copy()

        for user in self.users[userId].follows:
            collect.extend(self.users[user].posts)

        heapq.heapify(collect)
        ans = []
        for _ in range(10):
            if not collect:
                break
            ans.append(heapq.heappop(collect)[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User()
        
        if followeeId not in self.users:
            self.users[followeeId] = User()
        
        if followerId == followeeId:
            return
        self.users[followerId].follows.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].follows:
            self.users[followerId].follows.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)