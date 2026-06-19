# [1311. 获取你好友已观看的视频](https://leetcode.cn/problems/get-watched-videos-by-your-friends/)

- 标签：广度优先搜索、图、数组、哈希表、排序
- 难度：中等

## 题目链接

- [1311. 获取你好友已观看的视频 - 力扣](https://leetcode.cn/problems/get-watched-videos-by-your-friends/)

## 题目大意

**描述**：给定好友关系图 $friends$（$friends[i]$ 是 $i$ 的好友列表），$watchedVideos$ 是每个人观看的视频列表，$id$ 是用户 ID，$level$ 是层级。

**要求**：返回第 $level$ 层好友观看过的视频（按视频出现频率升序，频率相同按字典序升序）。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_1.png)

```python
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
输出：["B","C"] 
解释：
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -> watchedVideos = ["C"] 
id 为 2 -> watchedVideos = ["B","C"] 
你朋友观看过视频的频率为：
B -> 1 
C -> 2
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_2.png)

```python
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
输出：["D"]
解释：
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
```


## 解题思路

### 思路 1：BFS 找第 level 层好友

#### 1. 核心思想

用 BFS 找到距离 $id$ 恰好为 $level$ 的所有好友。收集他们看过的全部视频，统计频率后按规则排序。

#### 2. 具体步骤

**第 1 步**：BFS 从 $id$ 开始，找到第 $level$ 层好友。

**第 2 步**：统计这些好友看过的视频频率。

**第 3 步**：排序（频率升序 → 字典序升序）。

### 思路 1：代码

```python
from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = [False] * n
        q = deque([id])
        visited[id] = True
        cur_level = 0

        while q:
            if cur_level == level:
                # 收集当前层好友看过的视频
                videos = []
                for user in q:
                    videos.extend(watchedVideos[user])
                freq = Counter(videos)
                return sorted(freq.keys(), key=lambda x: (freq[x], x))
            for _ in range(len(q)):
                u = q.popleft()
                for v in friends[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            cur_level += 1

        return []
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n + V \log V)$，$V$ 是视频数量。
- **空间复杂度**：$O(n)$。
