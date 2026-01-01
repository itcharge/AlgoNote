# [0528. 按权重随机选择](https://leetcode.cn/problems/random-pick-with-weight/)

- 标签：数组、数学、二分查找、前缀和、随机化
- 难度：中等

## 题目链接

- [0528. 按权重随机选择 - 力扣](https://leetcode.cn/problems/random-pick-with-weight/)

## 题目大意

**描述**：

给定一个下标从 $0$ 开始的正整数数组 $w$，其中 $w[i]$ 代表第 $i$ 个下标的权重。

**要求**：

实现一个函数 `pickIndex`，它可以「随机地」从范围 $[0, w.length - 1]$ 内（含 $0$ 和 $w.length - 1$）选出并返回一个下标。选取下标 $i$ 的 概率 为 $w[i] / sum(w)$ 。

- 例如，对于 $w = [1, 3]$，挑选下标 $0$ 的概率为 $1 / (1 + 3) = 0.25$ （即，25%），而选取下标 $1$ 的概率为 $3 / (1 + 3) = 0.75$（即，75%）。

**说明**：

- $1 \le w.length \le 10^{4}$。
- $1 \le w[i] \le 10^{5}$。
- $pickIndex$ 将被调用不超过 $10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。
```

- 示例 2：

```python
输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：
[null,1,1,1,1,0]
解释：
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。

由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。
```

## 解题思路

### 思路 1：前缀和 + 二分查找

这道题要求按权重随机选择下标，权重越大被选中的概率越大。

核心思路：

1. 计算前缀和数组 $prefix\_sum$，其中 $prefix\_sum[i]$ 表示前 $i+1$ 个权重的总和。
2. 总权重为 $prefix\_sum[-1]$。
3. `pickIndex` 操作：
   - 在 $[1, prefix\_sum[-1]]$ 范围内随机生成一个数 $target$。
   - 使用二分查找在前缀和数组中找到第一个大于等于 $target$ 的位置，该位置即为选中的下标。
4. 原理：前缀和将权重映射到连续区间，权重越大对应的区间越长，被随机数命中的概率越大。

例如：$w = [1, 3]$，前缀和为 $[1, 4]$

- 下标 $0$ 对应区间 $[1, 1]$，长度为 $1$，概率为 $1/4$
- 下标 $1$ 对应区间 $[2, 4]$，长度为 $3$，概率为 $3/4$

### 思路 1：代码

```python
import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        # 计算前缀和
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)

    def pickIndex(self) -> int:
        # 在 [1, total] 范围内随机生成一个数
        target = random.randint(1, self.prefix_sum[-1])
        
        # 二分查找第一个大于等于 target 的位置
        # bisect_left 返回插入位置，即第一个 >= target 的位置
        return bisect.bisect_left(self.prefix_sum, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(n)$，其中 $n$ 为权重数组长度，需要计算前缀和。
  - `pickIndex`：$O(\log n)$，二分查找的时间复杂度。
- **空间复杂度**：$O(n)$，存储前缀和数组。
