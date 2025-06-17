# [1893. 检查是否区域内所有整数都被覆盖](https://leetcode.cn/problems/check-if-all-the-integers-in-a-range-are-covered/)

- 标签：数组、哈希表、前缀和
- 难度：简单

## 题目链接

- [1893. 检查是否区域内所有整数都被覆盖 - 力扣](https://leetcode.cn/problems/check-if-all-the-integers-in-a-range-are-covered/)

## 题目大意

**描述**：给定一个二维整数数组 $ranges$ 和两个整数 $left$ 和 $right$。每个 $ranges[i] = [start_i, end_i]$ 表示一个从 $start_i$ 到 $end_i$ 的 闭区间 。

**要求**：如果闭区间 $[left, right]$ 内每个整数都被 $ranges$ 中至少一个区间覆盖，那么请你返回 $True$ ，否则返回 $False$。

**说明**：

- $1 \le ranges.length \le 50$。
- $1 \le start_i \le end_i \le 50$。
- $1 \le left \le right \le 50$。

**示例**：

- 示例 1：

```python
输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：True
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。
```

- 示例 2：

```python
输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：False
解释：21 没有被任何一个区间覆盖。
```

## 解题思路

### 思路 1：暴力

区间的范围为 $[1, 50]$，所以我们可以使用一个长度为 $51$ 的标志数组 $flags$ 用于标记区间内的所有整数。

1. 遍历数组 $ranges$ 中的所有区间 $[l, r]$。
2. 对于区间 $[l, r]$ 和区间 $[left, right]$，将两区间相交部分标记为 $True$。
3. 遍历区间 $[left, right]$ 上的所有整数，判断对应标志位是否为 $False$。
4. 如果对应标志位出现 $False$，则返回 $False$。
5. 如果遍历完所有标志位都为 $True$，则返回 $True$。

### 思路 1：代码

```Python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        flags = [False for _ in range(51)]
        for l, r in ranges:
            for i in range(max(l, left), min(r, right) + 1):
                flags[i] = True
            
        for i in range(left, right + 1):
            if not flags[i]:
                return False
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(50 \times n)$。
- **空间复杂度**：$O(50)$。
