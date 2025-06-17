# [0383. 赎金信](https://leetcode.cn/problems/ransom-note/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [0383. 赎金信 - 力扣](https://leetcode.cn/problems/ransom-note/)

## 题目大意

**描述**：为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。

给定一个赎金信字符串 $ransomNote$ 和一个杂志字符串 $magazine$。

**要求**：判断 $ransomNote$ 能不能由 $magazines$ 里面的字符构成。如果可以构成，返回 `True`；否则返回 `False`。

**说明**：

- $magazine$ 中的每个字符只能在 $ransomNote$ 中使用一次。
- $1 \le ransomNote.length, magazine.length \le 10^5$。
- $ransomNote$ 和 $magazine$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：ransomNote = "a", magazine = "b"
输出：False
```

- 示例 2：

```python
输入：ransomNote = "aa", magazine = "ab"
输出：False
```

## 解题思路

### 思路 1：哈希表

暴力做法是双重循环遍历字符串 $ransomNote$ 和 $magazines$。我们可以用哈希表来减少算法的时间复杂度。具体做法如下：

- 先用哈希表存储 $magazines$ 中各个字符的个数（哈希表可用字典或数组实现）。
- 再遍历字符串 $ransomNote$ 中每个字符，对于每个字符：
  - 如果在哈希表中个数为 $0$，直接返回 `False`。
  - 如果在哈希表中个数不为 $0$，将其个数减 $1$。
- 遍历到最后，则说明 $ransomNote$ 能由 $magazines$ 里面的字符构成。返回 `True`。

### 思路 1：代码

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = [0 for _ in range(26)]

        for ch in magazine:
            num = ord(ch) - ord('a')
            magazine_counts[num] += 1

        for ch in ransomNote:
            num = ord(ch) - ord('a')
            if magazine_counts[num] == 0:
                return False
            else:
                magazine_counts[num] -= 1

        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$ 是字符串 $ransomNote$ 的长度，$n$ 是字符串 $magazines$ 的长度。
- **空间复杂度**：$O(|S|)$，其中 $S$ 是字符集，本题中 $|S| = 26$。

