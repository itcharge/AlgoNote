# [1234. 替换子串得到平衡字符串](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/)

- 标签：字符串、滑动窗口
- 难度：中等

## 题目链接

- [1234. 替换子串得到平衡字符串 - 力扣](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/)

## 题目大意

**描述**：给定一个长度为 $n$ 的字符串 $s$，其中只包含 `'Q'`、`'W'`、`'E'`、`'R'` 四种字符。如果四个字符在该字符串中恰好出现 $n/4$ 次，则称其为平衡字符串。

**要求**：通过替换一个子串，使得原字符串 $s$ 变为平衡字符串。返回可以达成目标的最短子串长度。

**说明**：

- $n$ 是 $4$ 的倍数。
- $1 \le n \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：s = "QWER"
输出：0
解释：已经是平衡的。
```

- 示例 2：

```python
输入：s = "QQWE"
输出：1
解释：将 "Q" 替换为 "R" 即可。
```

- 示例 3：

```python
输入：s = "QQQW"
输出：2
解释：将 "QQ" 替换为 "ER"。
```

## 解题思路

### 思路 1：滑动窗口

#### 1. 核心思想

设 $target = n/4$。`'Q'`、`'W'`、`'E'`、`'R'` 每种字符的目标出现次数是 $target$。

如果一个字符在当前字符串中出现的次数 $count[ch] > target$，说明它多了 $count[ch] - target$ 次。我们需要通过替换一个子串来"去掉"这些多余的字符。

滑动窗口用于找到**最短的子串**，使得该子串内包含所有多余的字符（每个多余字符出现的次数至少等于多余的数量）。

换句话说，对于窗口外的字符，每个字符的出现次数 $\le target$。我们要找最短的窗口，使得移除窗口（将窗口内的字符替换为需要的字符）后，整个字符串平衡。

#### 2. 具体步骤

**第 1 步**：统计字符串中每个字符的出现次数 $count$。

**第 2 步**：如果所有字符的 $count[ch] \le target$，说明已经平衡，返回 $0$。

**第 3 步**：使用滑动窗口找最短子串长度：
- 右指针 $r$ 向右扩展窗口。
- 每加入一个字符 $s[r]$，$count[s[r]] -= 1$（窗口内移除了该字符）。
- 当满足条件 $\max(count['Q'], count['W'], count['E'], count['R']) \le target$ 时：
  - 更新最短长度：$ans = \min(ans, r-l+1)$。
  - 左指针 $l$ 向右收缩窗口：$count[s[l]] += 1$，$l += 1$。

**第 4 步**：返回 $ans$。

#### 3. 为什么窗口满足条件时更新？

当窗口外的每种字符出现次数 $\le target$ 时，说明窗口内的字符被替换后（放入需要的字符），所有字符都能达到 $target$ 次。窗口长度可以任意替换，所以满足条件。

#### 4. 结合示例走一遍

$s = \text{"QQQW"}, n=4, target=1$

初始 $count = \{Q:3, W:1, E:0, R:0\}$

$count[Q]=3 > 1$，多余 $2$ 个 Q。

滑动窗口：
```
l=0, r=0: 窗口="Q", count={Q:2,W:1} → max=2>1
l=0, r=1: 窗口="QQ", count={Q:1,W:1} → max=1≤1 ✓, ans=2, 收缩左
l=1, r=1: 窗口="Q", count={Q:2,W:1} → max=2>1
l=1, r=2: 窗口="QQ", count={Q:1,W:1} → max=1≤1 ✓, ans=min(2,2)=2
l=2, r=2: 窗口="Q", count={Q:2,W:1} → max=2>1
l=2, r=3: 窗口="QW", count={Q:1,W:0} → max=1≤1 ✓, ans=min(2,2)=2
```

结果 $2$。

### 思路 1：代码

```python
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for ch in s:
            count[ch] += 1

        # 如果已经平衡
        if max(count.values()) <= target:
            return 0

        ans = n
        l = 0
        for r in range(n):
            # 将 s[r] 纳入窗口（窗口外该字符减少）
            count[s[r]] -= 1

            # 当窗口外每种字符的频率都 <= target 时
            while max(count.values()) <= target:
                ans = min(ans, r - l + 1)
                # 收缩左边界
                count[s[l]] += 1
                l += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。左右指针各遍历一次。
- **空间复杂度**：$O(1)$，只需要常数大小的哈希表。
