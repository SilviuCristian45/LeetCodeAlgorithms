from collections import defaultdict
import heapq

class User():
    tweets = []
    followed = []

class Twitter:
    usersRepo = {}

    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.usersRepo:
            self.usersRepo[userId] = User()
        if tweetId not in self.usersRepo[userId].tweets:
            self.usersRepo[userId].tweets.append(tweetId)

    def getNewsFeed(self, userId: int) -> list[int]:
        userPosts = self.usersRepo[userId].tweets
        for usersFollowed in self.usersRepo[userId].followed:
            userPosts += self.usersRepo[usersFollowed].tweets
        #get 10 most recent posts
        postsidNeg = [-postId for postId in userPosts]
        heapq.heapify(postsidNeg)
        result = []
        k = 10
        while k > 0 and len(postsidNeg) > 0:
            top = heapq.heappop(postsidNeg)
            result.append(abs(top))
            k -= 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.usersRepo[followerId]:
            self.usersRepo[followerId] = User()
        self.usersRepo[followerId].followed.append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersRepo[followerId].followed.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
obj.getNewsFeed(1)
obj.follow(1,2)
obj.postTweet(2, 5)
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))

# obj.unfollow(followerId,followeeId)