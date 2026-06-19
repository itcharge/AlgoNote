# [1306. 跳跃游戏 III](https://leetcode.cn/problems/jump-game-iii/)

- 标签：深度优先搜索、广度优先搜索、数组
- 难度：中等

## 题目链接

- [1306. 跳跃游戏 III - 力扣](https://leetcode.cn/problems/jump-game-iii/)

## 题目大意

**描述**：给定一个非负整数数组 $arr$ 和起始下标 $start$。你从 $start$ 开始，每次可以向左或向右跳 $arr[i]$ 步（$i$ 是当前位置）。

**要求**：判断是否能到达值为 $0$ 的下标。

**说明**：
- $1 \le arr.length \le 5 \times 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3
```

- 示例 2：

```python
输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true 
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 0 -> 下标 4 -> 下标 1 -> 下标 3
```


## 解题思路

### 思路 1：BFS

#### 1. 核心思想

BFS 搜索所有可达位置。从 $start$ 开始，每次可以跳 $+arr[pos]$ 或 $-arr[pos]$，在边界内且未访问则入队。

#### 2. 代码

```python
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        q = deque([start])
        visited[start] = True
        while q:
            pos = q.popleft()
            if arr[pos] == 0:
                return True
            for nxt in (pos + arr[pos], pos - arr[pos]):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        return False
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
