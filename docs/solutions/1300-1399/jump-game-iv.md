# [1345. 跳跃游戏 IV](https://leetcode.cn/problems/jump-game-iv/)

- 标签：广度优先搜索、数组、哈希表
- 难度：困难

## 题目链接

- [1345. 跳跃游戏 IV - 力扣](https://leetcode.cn/problems/jump-game-iv/)

## 题目大意

**描述**：给定一个整数数组 $arr$。你从下标 $0$ 开始，每次可以跳到 $i-1$、$i+1$ 或任意与 $arr[i]$ 值相同的下标。

**要求**：返回跳到最后一个下标所需的最少步数。

**说明**：
- $1 \le arr.length \le 5 \times 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。
```

- 示例 2：

```python
输入：arr = [7]
输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。
```


## 解题思路

### 思路 1：BFS + 同值分组优化

#### 1. 核心思想

BFS 找最短路径。关键优化：当第一次访问某个值对应的所有下标后，从哈希表中删除该值。否则同值的边会导致大量重复访问。

#### 2. 具体步骤

**第 1 步**：建立值到下标的映射 $val\_to\_idx$。

**第 2 步**：BFS 从 $0$ 开始，每次尝试三个方向。
- 访问完某个值对应的所有下标后，清空该列表（剪枝）。

### 思路 1：代码

```python
from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        val_to_idx = defaultdict(list)
        for i, v in enumerate(arr):
            val_to_idx[v].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return steps
                # 跳到同值下标
                for j in val_to_idx[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                val_to_idx[arr[i]].clear()  # 关键剪枝
                # 左右邻居
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)
            steps += 1
        return -1
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
