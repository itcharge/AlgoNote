# [1593. 拆分字符串使唯一子字符串的数目最大](https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/)

- 标签：哈希表、字符串、回溯
- 难度：中等

## 题目链接

- [1593. 拆分字符串使唯一子字符串的数目最大 - 力扣](https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/)

## 题目大意

**描述**：给定一个字符串 $s$。将字符串 $s$ 拆分后可以得到若干非空子字符串，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是唯一的 。

**要求**：拆分该字符串，并返回拆分后唯一子字符串的最大数目。

**说明**：

- 子字符串是字符串中的一个连续字符序列。
- $1 \le s.length \le 16$。
- $s$ 仅包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "ababccc"
输出：5
解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
```

- 示例 2：

```python
输入：s = "aba"
输出：2
解释：一种最大拆分方法为 ['a', 'ba']。
```

## 解题思路

### 思路 1：回溯算法

维护一个全局变量 $ans$ 用于记录拆分后唯一子字符串的最大数目。并使用集合 $s\underline{\hspace{0.5em}}set$ 记录不重复的子串。

- 从下标为 $0$ 开头的子串回溯。
- 对于下标为 $index$ 开头的子串，我们可以在 $index + 1$ 开始到 $len(s) - 1$ 的位置上，分别进行子串拆分，将子串拆分为 $s[index: i + 1]$。

- 如果当前子串不在 $s\underline{\hspace{0.5em}}set$ 中，则将其存入 $s\underline{\hspace{0.5em}}set$ 中，然后记录当前拆分子串个数，并从 $i + 1$ 的位置进行下一层递归拆分。然后在拆分完，对子串进行回退操作。
- 如果拆到字符串 $s$ 的末尾，则记录并更新 $ans$。
- 在开始位置还可以进行以下剪枝：如果剩余字符个数 + 当前子串个数 <= 当前拆分后子字符串的最大数目，则直接返回。

最后输出 $ans$。

### 思路 1：代码

```python
class Solution:
    ans = 0
    def backtrack(self, s, index, count, s_set):
        if len(s) - index + count <= self.ans:
            return 
        if index >= len(s):
            self.ans = max(self.ans, count)
            return

        for i in range(index, len(s)):
            sub_s = s[index: i + 1]
            if sub_s not in s_set:
                s_set.add(sub_s)
                self.backtrack(s, i + 1, count + 1, s_set)
                s_set.remove(sub_s)


    def maxUniqueSplit(self, s: str) -> int:
        s_set = set()
        self.ans = 0
        self.backtrack(s, 0, 0, s_set)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 为字符串的长度。
- **空间复杂度**：$O(n)$。

