# [0316. 去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/)

- 标签：栈、贪心、字符串、单调栈
- 难度：中等

## 题目链接

- [0316. 去除重复字母 - 力扣](https://leetcode.cn/problems/remove-duplicate-letters/)

## 题目大意

**描述**：给定一个字符串 `s`。

**要求**：去除字符串中重复的字母，使得每个字母只出现一次。需要保证 **「返回结果的字典序最小（要求不能打乱其他字符的相对位置）」**。

**说明**：

- $1 \le s.length \le 10^4$。
- `s` 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：s = "bcabc"
输出："abc"
```

- 示例 2：

```python
输入：s = "cbacdcbc"
输出："acdb"
```

## 解题思路

### 思路 1：哈希表 + 单调栈

针对题目的三个要求：去重、不能打乱其他字符顺序、字典序最小。我们来一一分析。

1. **去重**：可以通过 **「使用哈希表存储字母出现次数」** 的方式，将每个字母出现的次数统计起来，再遍历一遍，去除重复的字母。
2. **不能打乱其他字符顺序**：按顺序遍历，将非重复的字母存储到答案数组或者栈中，最后再拼接起来，就能保证不打乱其他字符顺序。
3. **字典序最小**：意味着字典序小的字母应该尽可能放在前面。
   1. 对于第 `i` 个字符 `s[i]` 而言，如果第 `0` ~ `i - 1` 之间的某个字符 `s[j]` 在 `s[i]` 之后不再出现了，那么 `s[j]` 必须放到 `s[i]` 之前。
   2. 而如果 `s[j]` 在之后还会出现，并且 `s[j]` 的字典序大于 `s[i]`，我们则可以先舍弃 `s[j]`，把 `s[i]` 尽可能的放到前面。后边再考虑使用 `s[j]` 所对应的字符。


要满足第 3 条需求，我们可以使用 **「单调栈」** 来解决。我们使用单调栈存储 `s[i]` 之前出现的非重复、并且字典序最小的字符序列。整个算法步骤如下：

1. 先遍历一遍字符串，用哈希表 `letter_counts` 统计出每个字母出现的次数。
2. 然后使用单调递减栈保存当前字符之前出现的非重复、并且字典序最小的字符序列。
3. 当遍历到 `s[i]` 时，如果 `s[i]` 没有在栈中出现过：
   1. 比较 `s[i]` 和栈顶元素 `stack[-1]` 的字典序。如果 `s[i]` 的字典序小于栈顶元素 `stack[-1]`，并且栈顶元素之后的出现次数大于 `0`，则将栈顶元素弹出。
   2. 然后继续判断 `s[i]` 和栈顶元素 `stack[-1]`，并且知道栈顶元素出现次数为 `0` 时停止弹出。此时将 `s[i]` 添加到单调栈中。
4. 从哈希表 `letter_counts` 中减去 `s[i]` 出现的次数，继续遍历。
5. 最后将单调栈中的字符依次拼接为答案字符串，并返回。

### 思路 1：代码

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        letter_counts = dict()
        for ch in s:
            if ch in letter_counts:
                letter_counts[ch] += 1
            else:
                letter_counts[ch] = 1

        for ch in s:
            if ch not in stack:
                while stack and ch < stack[-1] and stack[-1] in letter_counts and letter_counts[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            letter_counts[ch] -= 1

        return ''.join(stack)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(|\sum|)$，其中 $\sum$ 为字符集合，$|\sum|$ 为字符种类个数。由于栈中字符不能重复，因此栈中最多有 $|\sum|$ 个字符。

## 参考资料

- 【题解】[去除重复数组 - 去除重复字母 - 力扣（LeetCode）](https://leetcode.cn/problems/remove-duplicate-letters/solution/qu-chu-zhong-fu-shu-zu-by-lu-shi-zhe-sokp/)
