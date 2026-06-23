# [1433. 检查一个字符串是否可以打破另一个字符串](https://leetcode.cn/problems/check-if-a-string-can-break-another-string/)

- 标签：贪心、字符串、排序
- 难度：中等

## 题目链接

- [1433. 检查一个字符串是否可以打破另一个字符串 - 力扣](https://leetcode.cn/problems/check-if-a-string-can-break-another-string/)

## 题目大意

**描述**：给定两个长度相同的字符串 $s1$ 和 $s2$。

**要求**：判断 $s1$ 是否可以打破 $s2$，或者 $s2$ 是否可以打破 $s1$。如果至少一个成立，返回 $True$，否则 $False$。

**定义**：如果 $s1$ 在每一个位置上都不小于 $s2$ 的对应位置（即 $s1[i] \ge s2[i]$ 对所有 $i$ 成立），则 $s1$ 可以打破 $s2$。通过重排字符串的顺序可以实现。

**说明**：
- $1 \le s1.length = s2.length \le 10^5$。
- 字符串只包含小写字母。

**示例**：

- 示例 1：

```python
输入：s1 = "abc", s2 = "xya"
输出：true
解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。
```

- 示例 2：

```python
输入：s1 = "abe", s2 = "acd"
输出：false 
解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。
```

## 解题思路

### 思路 1：排序后逐位比较

#### 1. 核心思想

通过重排字符串，我们可以让两个字符串按相同顺序排列。贪心地想：将两个字符串分别排序，然后逐位比较即可。

将 $s1$ 和 $s2$ 分别排序为 $s1\_sorted$ 和 $s2\_sorted$。然后检查两种情况：
1. $s1\_sorted[i] \ge s2\_sorted[i]$ 对所有 $i$ 成立
2. $s2\_sorted[i] \ge s1\_sorted[i]$ 对所有 $i$ 成立

#### 2. 正确性证明

排序后逐位比较的正确性基于重排最优性：要使某个字符串能打破另一个，应该将每个字符串中最小位置对应最小位置、次小对应次小……即排序后比较。如果排序后的对应位置不满足条件，则任何其他排列也无法满足（可以反证法证明）。

#### 3. 具体步骤

**第 1 步**：将 $s1$ 和 $s2$ 转换为列表并排序。

**第 2 步**：检查 $s1$ 是否能打破 $s2$（逐个位置比较是否 $s1[i] \ge s2[i]$）。

**第 3 步**：检查 $s2$ 是否能打破 $s1$。

**第 4 步**：返回任意一个成立的结果。

#### 4. 举例说明

以 $s1 = "abc", s2 = "xya"$ 为例：

排序后：$s1 = "abc", s2 = "axy"$

$s1$ 打破 $s2$？$a \ge a, b \ge x$？$b < x$，不成立。

$s2$ 打破 $s1$？$a \ge a, x \ge b, y \ge c$ → 成立！

返回 $True$。

### 思路 1：代码

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)

        # 检查 s1 是否可打破 s2
        can_s1_break = all(a >= b for a, b in zip(s1_sorted, s2_sorted))
        # 检查 s2 是否可打破 s1
        can_s2_break = all(b >= a for a, b in zip(s1_sorted, s2_sorted))

        return can_s1_break or can_s2_break
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序为主。
- **空间复杂度**：$O(n)$，存储排序后的列表。

---

### 思路 2：计数排序优化

由于只有小写字母，可以用计数排序做到 $O(n)$：

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def can_break(a, b):
            # 检查 sorted(a) >= sorted(b) 逐位
            cnt_a = [0] * 26
            cnt_b = [0] * 26
            for ch in a:
                cnt_a[ord(ch) - 97] += 1
            for ch in b:
                cnt_b[ord(ch) - 97] += 1
            # 模拟逐位比较
            greater = True
            i = j = 0
            while i < 26 and j < 26:
                while i < 26 and cnt_a[i] == 0:
                    i += 1
                while j < 26 and cnt_b[j] == 0:
                    j += 1
                if i >= 26 or j >= 26:
                    break
                if i < j:
                    return False
                # 消耗一个较小的计数
                take = min(cnt_a[i], cnt_b[j])
                cnt_a[i] -= take
                cnt_b[j] -= take
            return True

        return can_break(s1, s2) or can_break(s2, s1)
```
