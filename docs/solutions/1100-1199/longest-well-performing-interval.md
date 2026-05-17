# [1124. 表现良好的最长时间段](https://leetcode.cn/problems/longest-well-performing-interval/)

- 标签：栈、数组、哈希表、前缀和、单调栈
- 难度：中等

## 题目链接

- [1124. 表现良好的最长时间段 - 力扣](https://leetcode.cn/problems/longest-well-performing-interval/)

## 题目大意

**描述**：给定一份工作时间表 $hours$，记录员工每天的工作小时数。工作 > 8 小时算「劳累」，≤ 8 小时算「不劳累」。

**表现良好的时间段**：在这段时间内，劳累的天数**严格多于**不劳累的天数。

**要求**：返回最长的表现良好的时间段的长度。如果不存在，返回 $0$。

**说明**：

- $1 \le hours.length \le 10^4$。
- $0 \le hours[i] \le 16$。

**示例**：

```python
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]，其中劳累 2 天 > 不劳累 1 天。
```

## 解题思路

### 思路 1：前缀和 + 哈希表

这道题可以用一个巧妙的转化：把 > 8 的记为 $+1$，≤ 8 的记为 $-1$。那么问题就变成了：**找到和 > 0 的最长连续子数组**。

然后引入**前缀和**的概念。前缀和 $preSum[i]$ 表示从开头到第 $i$ 天的累计和。子数组 $[j+1...i]$ 的和 = $preSum[i] - preSum[j]$。

我们要找 $preSum[i] - preSum[j] > 0$，即 $preSum[j] < preSum[i]$，且 $i - j$ 最大。

**步骤拆解：**

1. 遍历数组，累加 $preSum$（> 8 加 1，≤ 8 减 1）。

2. 如果 $preSum > 0$，说明从开头到现在都是良好的，直接更新最大长度为 $i+1$。

3. 否则，用哈希表记下每个 $preSum$ 第一次出现的位置。然后在哈希表里找 $preSum - 1$ 第一次出现的位置，因为 $preSum - 1 < preSum$，而且它是最接近 $preSum$ 的较小值，能让长度最大。

**为什么找 $preSum - 1$？**
我们要找一个比当前 $preSum$ 小的数，使得子数组和 > 0。最接近当前 $preSum$ 的较小值就是 $preSum - 1$，这样 $i - j$ 才能尽可能大（因为我们找到的是这个值第一次出现的位置，距离当前最远）。

### 思路 1：代码

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        preSum = 0  # 当前前缀和
        pos = {}    # 记录每个前缀和第一次出现的位置
        max_len = 0  # 最大长度
        
        for i in range(n):
            # 转换：>8 → +1，≤8 → -1
            if hours[i] > 8:
                preSum += 1
            else:
                preSum -= 1
            
            if preSum > 0:
                # 从头到现在的和 > 0，整段都是良好的
                max_len = i + 1
            else:
                # 记录这个前缀和第一次出现的位置
                if preSum not in pos:
                    pos[preSum] = i
                # 找 preSum - 1 的位置，因为 preSum - 1 < preSum
                if preSum - 1 in pos:
                    max_len = max(max_len, i - pos[preSum - 1])
        
        return max_len
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。只需遍历一次数组。
- **空间复杂度**：$O(n)$。哈希表最多存 $n$ 个前缀和。
