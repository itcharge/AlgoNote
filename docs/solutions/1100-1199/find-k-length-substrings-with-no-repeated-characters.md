# [1100. 长度为 K 的无重复字符子串](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [1100. 长度为 K 的无重复字符子串 - 力扣](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/)

## 题目大意

**描述**：给定一个字符串 `s`。

**要求**：找出所有长度为 `k` 且不含重复字符的子串，返回全部满足要求的子串的数目。

**说明**：

- $1 \le s.length \le 10^4$。
- $s$ 中的所有字符均为小写英文字母。
- $1 <= k <= 10^4$。

**示例**：

- 示例 1：

```python
输入：s = "havefunonleetcode", k = 5
输出：6
解释：
这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。
```

- 示例 2：

```python
输入：s = "home", K = 5
输出：0
解释：
注意：k 可能会大于 s 的长度。在这种情况下，就无法找到任何长度为 k 的子串。
```

## 解题思路

### 思路 1：滑动窗口

固定长度滑动窗口的题目。维护一个长度为 `k` 的滑动窗口。用 `window_count` 来表示窗口内所有字符个数。可以用字典、数组来实现，也可以直接用 `collections.Counter()` 实现。然后不断向右滑动，然后进行比较。如果窗口内字符无重复，则答案数目 + 1。然后继续滑动。直到末尾时。整个解题步骤具体如下：

1. `window_count` 用来维护窗口中 `2` 对应子串的各个字符数量。
2. `left` 、`right` 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
3. 向右移动 `right`，先将 `k` 个元素填入窗口中。
4. 当窗口元素个数为 `k` 时，即：`right - left + 1 >= k` 时，判断窗口内各个字符数量 `window_count` 是否等于 `k`。
   1. 如果等于，则答案 + 1。
   2. 如果不等于，则向右移动 `left`，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 `k`。
5. 重复 3 ~ 4 步，直到 `right` 到达数组末尾。返回答案。

### 思路 1：代码

```python
import collections

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left, right = 0, 0
        window_count = collections.Counter()
        ans = 0

        while right < len(s):
            window_count[s[right]] += 1

            if right - left + 1 >= k:
                if len(window_count) == k:
                    ans += 1
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(|\sum|)$，其中 $\sum$ 是字符集。

