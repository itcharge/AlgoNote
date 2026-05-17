# [1215. 步进数](https://leetcode.cn/problems/stepping-numbers/)

- 标签：广度优先搜索、数学
- 难度：中等

## 题目链接

- [1215. 步进数 - 力扣](https://leetcode.cn/problems/stepping-numbers/)

## 题目大意

**描述**：给定两个整数 $low$ 和 $high$。如果一个整数相邻两位上的数字之差的绝对值恰好为 $1$，则称这个数为步进数。

**要求**：返回 $[low, high]$ 范围内的所有步进数，按升序排列。

**说明**：

- $0 \le low \le high \le 2 \times 10^{9}$。

**示例**：

- 示例 1：

```python
输入：low = 0, high = 21
输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
```

- 示例 2：

```python
输入：low = 10, high = 15
输出：[10,12]
```

## 解题思路

### 思路 1：BFS 枚举

#### 1. 核心思想

一个步进数可以通过"在末尾添加一位差值恰好为 $1$ 的数字"来生成。例如 $12$ 是步进数，末尾是 $2$，可以在后面加 $1$（$2-1=1$）或 $3$（$3-2=1$）得到 $121$ 或 $123$，这两个仍然是步进数。

因此可以用 BFS 从 $1$ 到 $9$ 开始生成所有步进数（$0$ 也单独处理）。每次从队列中取出一个数 $num$，取最后一位 $last = num \% 10$，尝试在后面添加 $last-1$ 和 $last+1$（如果在 $0$ 到 $9$ 之间），生成新数 $num \times 10 + d$。如果新数 $\le high$，加入队列和结果集。

#### 2. 具体步骤

**第 1 步**：如果 $low == 0$，先将 $0$ 加入结果集。

**第 2 步**：将 $1$ 到 $9$ 加入队列。

**第 3 步**：BFS 循环：
- 从队列中取出 $num$。
- 如果 $num > high$，跳过。
- 如果 $num \ge low$，加入结果集（BFS 保证了数字从小到大）。
- 取最后一位 $last = num \% 10$。
- 如果 $last > 0$，尝试加 $last-1$：$new = num \times 10 + (last-1)$，如果 $new \le high$，入队。
- 如果 $last < 9$，尝试加 $last+1$：$new = num \times 10 + (last+1)$，如果 $new \le high$，入队。

**第 4 步**：将结果集排序（BFS 的顺序不一定严格升序）并返回。

注意：也可以用 DFS 或直接迭代生成，BFS/DFS 的思路类似。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        ans = []
        if low == 0:
            ans.append(0)

        q = deque(range(1, 10))
        while q:
            num = q.popleft()
            if num > high:
                continue
            if num >= low:
                ans.append(num)
            last = num % 10
            if last > 0:
                nxt = num * 10 + (last - 1)
                if nxt <= high:
                    q.append(nxt)
            if last < 9:
                nxt = num * 10 + (last + 1)
                if nxt <= high:
                    q.append(nxt)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(K)$，其中 $K$ 是 $[0, high]$ 范围内的步进数个数。步进数的数量远小于 $high$（因为每步最多生成 $2$ 个后继，最多 $9$ 位数字，总数不超过 $2^9 \times 9 \approx 4608$ 个）。
- **空间复杂度**：$O(K)$，需要存储所有步进数。
