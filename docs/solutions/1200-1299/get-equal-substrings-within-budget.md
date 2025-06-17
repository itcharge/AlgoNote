# [1208. 尽可能使字符串相等](https://leetcode.cn/problems/get-equal-substrings-within-budget/)

- 标签：字符串、二分查找、前缀和、滑动窗口
- 难度：中等

## 题目链接

- [1208. 尽可能使字符串相等 - 力扣](https://leetcode.cn/problems/get-equal-substrings-within-budget/)

## 题目大意

**描述**：给定两个长度相同的字符串，$s$ 和 $t$。将 $s$ 中的第 $i$ 个字符变到 $t$ 中的第 $i$ 个字符需要 $| s[i] - t[i] |$ 的开销（开销可能为 $0$），也就是两个字符的 ASCII 码值的差的绝对值。用于变更字符串的最大预算是 $maxCost$。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

**要求**：如果你可以将 $s$ 的子字符串转化为它在 $t$ 中对应的子字符串，则返回可以转化的最大长度。如果 $s$ 中没有子字符串可以转化成 $t$ 中对应的子字符串，则返回 $0$。

**说明**：

- $1 \le s.length, t.length \le 10^5$。
- $0 \le maxCost \le 10^6$。
- $s$ 和 $t$ 都只含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```

- 示例 2：

```python
输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
```

## 解题思路

### 思路 1：滑动窗口

维护一个滑动窗口 $window\underline{\hspace{0.5em}}sum$ 用于记录窗口内的开销总和，保证窗口内的开销总和小于等于 $maxCost$。使用 $ans$ 记录可以转化的最大长度。具体做法如下：

使用两个指针 $left$、$right$。分别指向滑动窗口的左右边界，保证窗口内所有元素转化开销总和小于等于 $maxCost$。

- 先统计出 $s$ 中第 $i$ 个字符变为 $t$ 的第 $i$ 个字符的开销，用数组 $costs$ 保存。
- 一开始，$left$、$right$ 都指向 $0$。
- 将最右侧字符的转变开销填入窗口中，向右移动 $right$。
- 直到窗口内开销总和 $window\underline{\hspace{0.5em}}sum$ 大于 $maxCost$。则不断右移 $left$，缩小窗口长度。直到 $window\underline{\hspace{0.5em}}sum \le maxCost$ 时，更新可以转换的最大长度 $ans$。
- 向右移动 $right$，直到 $right \ge len(s)$ 为止。
- 输出答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        size = len(s)
        costs = [0 for _ in range(size)]
        for i in range(size):
            costs[i] = abs(ord(s[i]) - ord(t[i]))

        left, right = 0, 0
        ans = 0
        window_sum = 0
        while right < size:
            window_sum += costs[right]
            while window_sum > maxCost:
                window_sum -= costs[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：
- **空间复杂度**：

