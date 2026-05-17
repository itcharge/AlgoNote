# [1207. 独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [1207. 独一无二的出现次数 - 力扣](https://leetcode.cn/problems/unique-number-of-occurrences/)

## 题目大意

**描述**：给定一个整数数组 $arr$。

**要求**：判断数组中每个数字的出现次数是否互不相同。如果是返回 $True$，否则返回 $False$。

**说明**：

- $1 \le arr.length \le 1000$。
- $-1000 \le arr[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,2,1,1,3]
输出：true
解释：1 出现 3 次，2 出现 2 次，3 出现 1 次，所有次数互不相同。
```

- 示例 2：

```python
输入：arr = [1,2]
输出：false
解释：1 和 2 各出现 1 次，次数相同。
```

## 解题思路

### 思路 1：哈希表

#### 1. 核心思想

用两个哈希表：
1. 第一个哈希表统计每个数字出现的次数 $freq$。
2. 第二个哈希表（或集合）记录出现次数是否出现过。如果某个出现次数已经存在，说明有重复，返回 $False$。

#### 2. 具体步骤

**第 1 步**：遍历 $arr$，用 $freq$ 统计每个数字的出现次数。

**第 2 步**：遍历 $freq$ 中的所有值，用集合 $seen$ 记录已经见过的出现次数：
- 如果某个次数已在 $seen$ 中，返回 $False$。
- 否则加入 $seen$。

**第 3 步**：遍历完成后返回 $True$。

#### 3. 结合示例走一遍

$arr = [1,2,2,1,1,3]$

统计频率：$1 \to 3$，$2 \to 2$，$3 \to 1$。

检查唯一性：
- $3$ 不在 $seen$ 中 → $seen = \{3\}$
- $2$ 不在 $seen$ 中 → $seen = \{2,3\}$
- $1$ 不在 $seen$ 中 → $seen = \{1,2,3\}$

所有次数唯一，返回 $True$。

### 思路 1：代码

```python
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # 统计每个数字的出现次数
        freq = Counter(arr)
        # 检查次数是否唯一
        seen = set()
        for cnt in freq.values():
            if cnt in seen:
                return False
            seen.add(cnt)
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。
- **空间复杂度**：$O(n)$，需要存储频率表。
