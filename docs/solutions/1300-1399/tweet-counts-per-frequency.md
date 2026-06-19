# [1348. 推文计数](https://leetcode.cn/problems/tweet-counts-per-frequency/)

- 标签：设计、哈希表、二分查找、有序集合、排序
- 难度：中等

## 题目链接

- [1348. 推文计数 - 力扣](https://leetcode.cn/problems/tweet-counts-per-frequency/)

## 题目大意

**描述**：实现一个 `TweetCounts` 类，支持记录推文发布和按时间段统计推文数量。

- `TweetCounts()` 初始化对象。
- `recordTweet(String tweetName, int time)` 记录名为 $tweetName$ 的推文在时间 $time$（秒）发布。
- `getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)` 返回一个数组，表示从 $startTime$ 到 $endTime$（闭区间）内，按 $freq$（分钟、小时或天）划分的每个时间间隔内 $tweetName$ 的推文数量。

**说明**：
- $freq$ 为 `"minute"`（每分钟）、`"hour"`（每小时）或 `"day"`（每天）。
- 时间间隔的定义：
  - 分钟：$60$ 秒。第 $i$ 个区间为 $[startTime + i \times delta, startTime + (i+1) \times delta)$
  - 小时：$3600$ 秒
  - 天：$86400$ 秒
- 最后一个区间的右端点为 $endTime$（闭区间）。
- 最多调用 $recordTweet$ 和 $getTweetCountsPerFrequency$ 共 $10^4$ 次。

**示例**：

- 示例 1：

```python
输入：
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

输出：
[null,null,null,null,[2],[2,1],null,[4]]

解释：
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // "tweet3" 发布推文的时间分别是 0, 10 和 60 。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。 
tweetCounts.recordTweet("tweet3", 120);                            // "tweet3" 发布推文的时间分别是 0, 10, 60 和 120 。
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。统计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。
```


## 解题思路

### 思路 1：哈希表 + 二分查找

#### 1. 核心思想

对每个推文名称，维护一个有序时间列表。每次 $recordTweet$ 时插入一条记录。每次查询时，根据 $freq$ 确定 $delta$，然后对每个区间统计落在区间内的时间点数量。

统计可以用二分查找（`bisect_left` / `bisect_right`）快速计算每个区间内的元素个数。

#### 2. 具体步骤

**初始化**：
- 哈希表 $tweets$：$key$ 为推文名称，$value$ 为有序列表（Python 中用普通列表，$add$ 时使用 `bisect.insort` 或最后统一排序）。

**$recordTweet(tweetName, time)$**：
- 将 $time$ 加入 $tweets[tweetName]$ 的有序列表中。为了效率，可以先将所有时间点加入，不做排序，查询时再排序（或者用 `bisect.insort` 保持有序）。

**$getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)$**：
- 根据 $freq$ 确定 $delta$：
  - `"minute"` → $delta = 60$
  - `"hour"` → $delta = 3600$
  - `"day"` → $delta = 86400$
- 计算区间数量：$size = (endTime - startTime) // delta + 1$
- 获取 $tweetName$ 的时间列表 $times$（先排序）。
- 对第 $i$ 个区间 $[startTime + i \times delta, \min(startTime + (i+1) \times delta, endTime + 1)]$：
  - $left = bisect\_left(times, startTime + i \times delta)$
  - $right = bisect\_right(times, startTime + (i+1) \times delta - 1)$ 或 $bisect\_left(times, startTime + (i+1) \times delta)$
  - 区间内数量 = $right - left$

#### 3. 优化说明

由于最多 $10^4$ 次操作，每次查询时对当前名称的列表排序（或插入时保持有序）都是可行的。但注意如果多次查询之间没有新插入，重复排序浪费性能，因此可以维护一个 $dirty$ 标志，只在有插入时重新排序。

#### 4. 举例说明

操作序列：`recordTweet("tweet1", 0), recordTweet("tweet1", 60), recordTweet("tweet1", 10), getTweetCountsPerFrequency("minute", "tweet1", 0, 59)`

$delta = 60$，区间 $[0, 59]$。

$times = [0, 10, 60]$，在 $[0,59]$ 内的有 $0$ 和 $10$，共 $2$ 条。

结果：$[2]$。

再执行 `getTweetCountsPerFrequency("minute", "tweet1", 0, 120)`：

区间 $[0,59]$ 内 $0,10$ → $2$ 条
区间 $[60,119]$ 内 $60$ → $1$ 条
区间 $[120,120]$ 内无 → $0$ 条

结果：$[2, 1, 0]$。

### 思路 1：代码

```python
from collections import defaultdict
import bisect

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)  # tweetName -> list of times

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                    startTime: int, endTime: int) -> List[int]:
        # 确定 delta
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:  # "day"
            delta = 86400

        # 获取该推文的时间列表并排序
        times = sorted(self.tweets[tweetName])

        # 计算区间数
        size = (endTime - startTime) // delta + 1
        ans = [0] * size

        for i in range(size):
            left_bound = startTime + i * delta
            right_bound = min(startTime + (i + 1) * delta, endTime + 1)
            left = bisect.bisect_left(times, left_bound)
            right = bisect.bisect_left(times, right_bound)
            ans[i] = right - left

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - $recordTweet$：$O(1)$（仅追加，不排序）
  - $getTweetCountsPerFrequency$：$O(n \log n + k \log n)$，其中 $n$ 是该推文的记录数，$k$ 是区间数。
- **空间复杂度**：$O(n)$，存储所有推文记录。

---

### 思路 2：惰性排序优化

可以通过维护 $dirty$ 标志来避免重复排序：

```python
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.sorted = defaultdict(bool)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        self.sorted[tweetName] = False

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                    startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            delta = 60
        elif freq == "hour":
            delta = 3600
        else:
            delta = 86400

        # 惰性排序
        if not self.sorted[tweetName]:
            self.tweets[tweetName].sort()
            self.sorted[tweetName] = True

        times = self.tweets[tweetName]
        size = (endTime - startTime) // delta + 1
        ans = [0] * size

        for i in range(size):
            left = bisect.bisect_left(times, startTime + i * delta)
            right = bisect.bisect_left(times, min(startTime + (i + 1) * delta, endTime + 1))
            ans[i] = right - left

        return ans
```

惰性排序在多次 $recordTweet$ 之间只排序一次，效率更高。
