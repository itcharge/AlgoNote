# [0567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)

- 标签：哈希表、双指针、字符串、滑动窗口
- 难度：中等

## 题目链接

- [0567. 字符串的排列 - 力扣](https://leetcode.cn/problems/permutation-in-string/)

## 题目大意

**描述**：给定两个字符串 $s1$ 和 $s2$ 。

**要求**：判断 $s2$ 是否包含 $s1$ 的排列。如果包含，返回 $True$；否则，返回 $False$。

**说明**：

- $1 \le s1.length, s2.length \le 10^4$。
- $s1$ 和 $s2$ 仅包含小写字母。

**示例**：

- 示例 1：

```python
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```

- 示例 2：

```python
输入：s1= "ab" s2 = "eidboaoo"
输出：False
```

## 解题思路

### 思路 1：滑动窗口

题目要求判断 $s2$ 是否包含 $s1$ 的排列，则 $s2$ 的子串长度等于 $s1$ 的长度。我们可以维护一个长度为字符串 $s1$ 长度的固定长度的滑动窗口。

先统计出字符串  $s1$ 中各个字符的数量，我们用 $s1\_count$ 来表示。这个过程可以用字典、数组来实现，也可以直接用 `collections.Counter()` 实现。再统计 $s2$ 对应窗口内的字符数量 $window\_count$，然后不断向右滑动，然后进行比较。如果对应字符数量相同，则返回 $True$，否则继续滑动。直到末尾时，返回 $False$。整个解题步骤具体如下：

1. $s1\_count$ 用来统计 $s1$ 中各个字符数量。$window\_count$ 用来维护窗口中 $s2$ 对应子串的各个字符数量。$window\_size$ 表示固定窗口的长度，值为 $len(s1)$。
2. 先统计出 $s1$ 中各个字符数量。
3. $left$ 、$right$ 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
4. 向右移动 $right$，先将 $len(s1)$ 个元素填入窗口中。
5. 当窗口元素个数为 $window\_size$ 时，即：$right - left + 1 \ge window\_size$ 时，判断窗口内各个字符数量 $window\_count$ 是否等于 $s1 $ 中各个字符数量 $s1\_count$。
   1. 如果等于，直接返回 $True$。
   2. 如果不等于，则向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $window\_size$。
6. 重复 $4 \sim 5$ 步，直到 $right$ 到达数组末尾。返回 $False$。

### 思路 1：代码

```python
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        s1_count = collections.Counter(s1)
        window_count = collections.Counter()
        window_size = len(s1)

        while right < len(s2):
            window_count[s2[right]] += 1

            if right - left + 1 >= window_size:
                if window_count == s1_count:
                    return True
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            right += 1
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m + |\sum|)$，其中 $n$、$m$ 分别是字符串 $s1$、$s2$ 的长度，$\sum$ 是字符集，本题中 $|\sum| = 26$。
- **空间复杂度**：$O(|\sum|)$。

