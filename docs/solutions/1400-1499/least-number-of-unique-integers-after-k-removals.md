# [1481. 不同整数的最少数目](https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/)

- 标签：贪心、数组、哈希表、计数、排序
- 难度：中等

## 题目链接

- [1481. 不同整数的最少数目 - 力扣](https://leetcode.cn/problems/least-number-of-unique-integers-after-k-removals/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个整数 $k$，可以移除 $k$ 个元素。

**要求**：返回移除 $k$ 个元素后，剩余数组中不同整数的最少数目。

**说明**：
- $1 \le arr.length \le 10^5$。
- $0 \le k \le arr.length$。

**示例**：

- 示例 1：

```python
输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
```

- 示例 2：

```python
输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。
```

## 解题思路

### 思路 1：贪心

#### 1. 核心思想

要使剩余的不同整数最少，应该尽可能多地**完整移除某个整数**（即移除它的全部出现次数）。贪心地优先移除出现次数少的整数。

#### 2. 具体步骤

**第 1 步**：统计每个整数的出现次数。

**第 2 步**：将出现次数排序（升序）。

**第 3 步**：遍历出现次数，如果当前整数的出现次数 $\le k$，可以完整移除它，$k$ 减去该次数，不同整数数量减 $1$。

**第 4 步**：返回剩余的不同整数数量。

#### 3. 举例说明

以 $arr = [4,3,1,1,3,3,2], k = 3$ 为例：

统计：$4:1, 3:3, 1:2, 2:1$

排序后次数：$[1,1,2,3]$

- $k=3$：$1 \le 3$，移除 $4$，$k=2$，剩余 $3$ 种
- $k=2$：$1 \le 2$，移除 $2$，$k=1$，剩余 $2$ 种
- $k=1$：$2 > 1$，不能完整移除 $1$
- 最终剩余 $2$ 种（$1$ 和 $3$）

### 思路 1：代码

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        counts = sorted(freq.values())
        unique = len(counts)

        for cnt in counts:
            if k >= cnt:
                k -= cnt
                unique -= 1
            else:
                break

        return unique
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序次数数组。
- **空间复杂度**：$O(n)$，哈希表。
