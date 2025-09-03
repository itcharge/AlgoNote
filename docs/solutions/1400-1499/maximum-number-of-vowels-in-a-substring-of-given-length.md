# [1456. 定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

- 标签：字符串、滑动窗口
- 难度：中等

## 题目链接

- [1456. 定长子串中元音的最大数目 - 力扣](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

## 题目大意

**描述**：给定字符串 $s$ 和整数 $k$。

**要求**：返回字符串 $s$ 中长度为 $k$ 的单个子字符串中可能包含的最大元音字母数。

**说明**：

- 英文中的元音字母为（$a$, $e$, $i$, $o$, $u$）。
- $1 <= s.length <= 10^5$。
- $s$ 由小写英文字母组成。
- $1 <= k <= s.length$。

**示例**：

- 示例 1：

```python
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。
```

- 示例 2：

```python
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。
```

## 解题思路

### 思路 1：滑动窗口

固定长度的滑动窗口题目。维护一个长度为 $k$ 的窗口，并统计滑动窗口中最大元音字母数。具体做法如下：

1. $ans$ 用来维护长度为 $k$ 的单个字符串中最大元音字母数。$window\_count$ 用来维护窗口中元音字母数。集合 $vowel\_set$ 用来存储元音字母。
2. $left$ 、$right$ 都指向字符串 $s$ 的第一个元素，即：$left = 0$，$right = 0$。
3. 判断 $s[right]$ 是否在元音字母集合中，如果在则用 $window\_count$ 进行计数。
4. 当窗口元素个数为 $k$ 时，即：$right - left + 1 \ge k$ 时，更新 $ans$。然后判断 $s[left]$ 是否为元音字母，如果是则 `window_count -= 1`，并向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $k$。
5. 重复 $3 \sim 4$ 步，直到 $right$ 到达数组末尾。
6. 最后输出 $ans$。

### 思路 1：代码

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        ans = 0
        window_count = 0
        vowel_set = ('a','e','i','o','u')

        while right < len(s):
            if s[right] in vowel_set:
                window_count += 1

            if right - left + 1 >= k:
                ans = max(ans, window_count)
                if s[left] in vowel_set:
                    window_count -= 1
                left += 1

            right += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(1)$。

