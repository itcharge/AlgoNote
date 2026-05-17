# [1297. 子串的最大出现次数](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [1297. 子串的最大出现次数 - 力扣](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/)

## 题目大意

**描述**：给定一个字符串 $s$，以及两个整数 $maxLetters$ 和 $minSize$、$maxSize$。

**要求**：找到满足下面所有条件的任意子串，并返回它的最大出现次数：
1. 子串的长度在 $minSize$ 到 $maxSize$ 之间（包含边界）。
2. 子串中不同字母的数目不超过 $maxLetters$。

如果没有满足条件的子串，返回 $0$。

**说明**：

- $1 \le s.length \le 10^{5}$。
- $1 \le maxLetters \le 26$。
- $1 \le minSize \le maxSize \le min(26, s.length)$。

**示例**：

- 示例 1：

```python
输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次，且不同字母数为 2（'a' 和 'b'），满足条件。
```

- 示例 2：

```python
输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且不同字母数为 1，满足条件。
```

- 示例 3：

```python
输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
```

## 解题思路

### 思路 1：滑动窗口 + 哈希表

#### 1. 核心思想

这道题有一个重要的简化技巧：**只需要考虑长度为 $minSize$ 的子串**。

为什么呢？假设有一个长度为 $L$（$L > minSize$）的子串 $t$ 出现了 $k$ 次，那么 $t$ 的每个长度为 $minSize$ 的前缀也一定出现了至少 $k$ 次（因为每次出现 $t$ 时，它的前 $minSize$ 个字符也同时出现）。如果 $t$ 满足不同字母数不超过 $maxLetters$，它的前缀自然也满足（前缀的字母集合是 $t$ 字母集合的子集）。

所以，**最大出现次数一定出现在长度为 $minSize$ 的子串中**。$maxSize$ 这个参数其实是用来迷惑人的，我们只需要固定窗口大小为 $minSize$。

这个简化的正确性依赖于：子串的"出现次数"统计的是所有位置上的出现。如果 $t$ 出现了 $k$ 次，它的 $minSize$ 前缀至少也出现了 $k$ 次（可能在更多位置出现）。我们寻找的是**最大出现次数**，所以只需关注最短的有效长度即可。

#### 2. 具体步骤

**第 1 步**：固定窗口大小为 $minSize$，用一个长度为 $minSize$ 的滑动窗口遍历字符串 $s$。

**第 2 步**：对每个窗口：
- 用一个哈希表 $letter\_count$ 统计窗口内每个字符的出现次数（或直接用 26 大小的数组）。
- 如果 $letter\_count$ 中不同字母的数量 $\le maxLetters$，则该子串符合条件。
- 用另一个哈希表 $substring\_count$ 统计这个子串的出现次数。

**第 3 步**：遍历过程中，更新 $substring\_count$ 中的最大值作为答案。

**第 4 步**：返回最大出现次数。

#### 3. 优化技巧

每次滑动窗口时，不需要重新统计整个窗口的字母频率。可以用**滑动窗口的增量更新**技巧：
- 窗口右移一位时，新字符进入窗口，旧字符离开窗口。
- 维护一个长度为 26 的数组 $count$ 和当前不同字母的数量 $unique$。
- 新字符加入：如果 $count[ch]$ 从 $0$ 变成 $1$，$unique$ 加 $1$。
- 旧字符离开：如果 $count[ch]$ 从 $1$ 变成 $0$，$unique$ 减 $1$。

#### 4. 结合示例走一遍

$s = \text{"aababcaab"}, maxLetters = 2, minSize = 3$

固定窗口大小 $3$，从左到右滑动：

```
窗口位置      子串    不同字母数(≤2?)    substring_count
[0,3)  aab    a:2,b:1 → 2 ✓     {"aab": 1}
[1,4)  aba    a:2,b:1 → 2 ✓     {"aab": 1, "aba": 1}
[2,5)  bab    b:2,a:1 → 2 ✓     {"aab": 1, "aba": 1, "bab": 1}
[3,6)  abc    a:1,b:1,c:1 → 3 ✗
[4,7)  bca    b:1,c:1,a:1 → 3 ✗
[5,8)  caa    c:1,a:2 → 2 ✓     {"aab": 1, "aba": 1, "bab": 1, "caa": 1}
[6,9)  aab    a:2,b:1 → 2 ✓     {"aab": 2, "aba": 1, "bab": 1, "caa": 1}
```

最大出现次数为 $2$，对应子串 `"aab"`。

### 思路 1：代码

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        # 统计窗口内每个字母出现的频率（26 个小写字母）
        count = [0] * 26
        unique = 0      # 窗口内不同字母的数量
        substring_count = {}    # 子串 -> 出现次数
        ans = 0

        # 初始化第一个窗口
        for i in range(minSize):
            idx = ord(s[i]) - ord('a')
            if count[idx] == 0:
                unique += 1
            count[idx] += 1

        # 检查第一个窗口
        if unique <= maxLetters:
            sub = s[:minSize]
            substring_count[sub] = 1
            ans = 1

        # 滑动窗口
        for i in range(minSize, n):
            # 移入新字符 s[i]
            idx_in = ord(s[i]) - ord('a')
            if count[idx_in] == 0:
                unique += 1
            count[idx_in] += 1

            # 移出旧字符 s[i - minSize]
            idx_out = ord(s[i - minSize]) - ord('a')
            count[idx_out] -= 1
            if count[idx_out] == 0:
                unique -= 1

            # 检查当前窗口
            if unique <= maxLetters:
                sub = s[i - minSize + 1 : i + 1]
                substring_count[sub] = substring_count.get(sub, 0) + 1
                ans = max(ans, substring_count[sub])

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。滑动窗口遍历一次，每次窗口操作是 $O(1)$。子串入哈希表时，Python 截取子串需要 $O(minSize)$ 时间，但 $minSize \le 26$，可以视为常数。
- **空间复杂度**：$O(n)$，哈希表在最坏情况下需要存储 $O(n)$ 个不同的子串。
