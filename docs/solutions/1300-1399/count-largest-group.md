# [1399. 统计最大组的数目](https://leetcode.cn/problems/count-largest-group/)

- 标签：数学、哈希表
- 难度：简单

## 题目链接

- [1399. 统计最大组的数目 - 力扣](https://leetcode.cn/problems/count-largest-group/)

## 题目大意

**描述**：给定整数 $n$。将 $1$ 到 $n$ 的每个整数按各位数字之和分组，相同数位和的数字属于同一组。

**要求**：返回所有组中，包含数字最多的那些组的数量。

**说明**：
- $1 \le n \le 10^4$。

**示例**：
- 示例：
```python
输入：n = 13
输出：4
解释：{1,10} 数位和 1，{2,11} 数位和 2，{3,12} 数位和 3，{4,13} 数位和 4，每组 2 个数字，共 4 组。
```

## 解题思路

### 思路 1：哈希表计数

#### 1. 核心思想

遍历 $1$ 到 $n$，计算每个数的数位和，用哈希表统计每个数位和的频次。再找出最大频次，统计有多少组达到该频次。

#### 2. 具体步骤

**第 1 步**：初始化 $freq$ 字典。

**第 2 步**：遍历 $i$ 从 $1$ 到 $n$，计算数位和 $s$，$freq[s] += 1$。

**第 3 步**：找出 $freq$ 中的最大值 $max\_cnt$，统计值为 $max\_cnt$ 的键的数量。

### 思路 1：代码

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}
        for i in range(1, n + 1):
            s = sum(int(d) for d in str(i))
            freq[s] = freq.get(s, 0) + 1
        max_cnt = max(freq.values())
        return sum(1 for v in freq.values() if v == max_cnt)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log n)$，每个数计算数位和需要 $O(\log n)$。
- **空间复杂度**：$O(n)$。
