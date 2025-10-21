# [0355. 设计推特](https://leetcode.cn/problems/design-twitter/)

- 标签：设计、哈希表、链表、堆（优先队列）
- 难度：中等

## 题目链接

- [0355. 设计推特 - 力扣](https://leetcode.cn/problems/design-twitter/)

## 题目大意

**要求**：

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 $10$ 条推文。

实现 `Twitter` 类：

- `Twitter() ` 初始化简易版推特对象
- `void postTweet(int userId, int tweetId)` 根据给定的 $tweetId$ 和 $userId$ 创建一条新推文。每次调用此函数都会使用一个不同的 $tweetId$ 。
- `List<Integer> getNewsFeed(int userId)` 检索当前用户新闻推送中最近 $10$ 条推文的 ID。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
- `void follow(int followerId, int followeeId)` ID 为 $followerId$ 的用户开始关注 ID 为 $followeeId$ 的用户。
- `void unfollow(int followerId, int followeeId)` ID 为 $followerId$ 的用户不再关注 ID 为 $followeeId$ 的用户。

**说明**：

- $1 \le userId, followerId, followeeId \le 500$。
- $0 \le tweetId \le 10^{4}$。
- 所有推特的 ID 都互不相同。
- `postTweet`、`getNewsFeed`、`follow` 和 `unfollow` 方法最多调用 $3 times 10^{4}$ 次。
- 用户不能关注自己。

**示例**：

- 示例 1：

```python
输入
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
输出
[null, null, [5], null, null, [6, 5], null, [5]]

解释
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2);    // 用户 1 关注了用户 2
twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2
```

## 解题思路

### 思路 1：哈希表 + 全局时间戳

使用哈希表来存储用户信息和推文信息，结合全局时间戳来维护推文的时间顺序。

具体步骤：

1. **数据结构设计**：
   - 使用全局时间戳 $timestamp$ 来记录每条推文的发布时间。
   - 使用哈希表 $tweets$ 存储每个用户的推文列表，每个推文包含 $tweetId$ 和 $timestamp$。
   - 使用哈希表 $follows$ 存储每个用户关注的用户集合。
   - 使用哈希表 $followers$ 存储每个用户的粉丝集合。

2. **postTweet 操作**：
   - 将新推文 $[tweetId, timestamp]$ 添加到对应用户的推文列表中。
   - 递增全局时间戳 $timestamp$。

3. **getNewsFeed 操作**：
   - 获取用户自己及其关注的所有用户的推文。
   - 合并所有推文并按时间戳降序排序。
   - 返回最近的 $10$ 条推文。

4. **follow 操作**：
   - 在 $follows[followerId]$ 中添加 $followeeId$。
   - 在 $followers[followeeId]$ 中添加 $followerId$。

5. **unfollow 操作**：
   - 从 $follows[followerId]$ 中移除 $followeeId$。
   - 从 $followers[followeeId]$ 中移除 $followerId$。

### 思路 1：代码

```python
class Twitter:

    def __init__(self):
        # 全局时间戳，用于记录推文发布顺序
        self.timestamp = 0
        # 存储每个用户的推文列表，每个推文格式为 [tweetId, timestamp]
        self.tweets = defaultdict(list)
        # 存储每个用户关注的用户集合
        self.follows = defaultdict(set)
        # 存储每个用户的粉丝集合
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 将新推文添加到用户的推文列表中
        self.tweets[userId].append([tweetId, self.timestamp])
        # 递增全局时间戳
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 获取用户自己及其关注的所有用户
        all_users = {userId} | self.follows[userId]
        
        # 收集所有相关用户的推文
        all_tweets = []
        for user in all_users:
            all_tweets.extend(self.tweets[user])
        
        # 按时间戳降序排序（最新的在前）
        all_tweets.sort(key=lambda x: x[1], reverse=True)
        
        # 返回最近的 10 条推文的 tweetId
        return [tweet[0] for tweet in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # 用户不能关注自己
        if followerId == followeeId:
            return
        
        # 添加关注关系
        self.follows[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 移除关注关系
        self.follows[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `postTweet` 操作：$O(1)$，只需要添加推文到列表末尾。
  - `getNewsFeed` 操作：$O(n \log n)$，其中 $n$ 是所有相关用户的推文总数，需要排序。
  - `follow` 操作：$O(1)$，只需要在集合中添加元素。
  - `unfollow` 操作：$O(1)$，只需要从集合中移除元素。
- **空间复杂度**：$O(m + n)$，其中 $m$ 是推文总数，$n$ 是用户总数。
