# [0792. 匹配子序列的单词数](https://leetcode.cn/problems/number-of-matching-subsequences/)

- 标签：字典树、数组、哈希表、字符串、二分查找、动态规划、排序
- 难度：中等

## 题目链接

- [0792. 匹配子序列的单词数 - 力扣](https://leetcode.cn/problems/number-of-matching-subsequences/)

## 题目大意

**描述**：

给定字符串 $s$ 和字符串数组 $words$。

**要求**：

返回 $words[i]$ 中是 $s$ 的子序列的单词个数。

**说明**：

- 字符串的「子序列」：是从原始字符串中生成的新字符串，可以从中删去一些字符（可以是 none），而不改变其余字符的相对顺序。
   - 例如，`"ace"` 是 `"abcde"` 的子序列。
- $1 \le s.length \le 5 * 10^{4}$。
- $1 \le words.length \le 5000$。
- $1 \le words[i].length \le 50$。
- $words[i]$ 和 $s$ 都只由小写字母组成。

**示例**：

- 示例 1：

```python
输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
```

- 示例 2：

```python
输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2
```

## 解题思路

### 思路 1：哈希表 + 双指针

这道题要求统计有多少个单词是字符串 $s$ 的子序列。

**解题步骤**：

1. **优化方法**：为了避免对每个单词都遍历一次 $s$，可以使用哈希表将单词按首字母分组。
2. 对于 $s$ 中的每个字符 $c$，找到所有以 $c$ 开头的单词，尝试匹配。
3. 使用双指针判断单词是否是 $s$ 的子序列：
   - 对于每个单词，维护一个指针指向当前需要匹配的字符。
   - 遍历 $s$，如果当前字符与单词的当前字符匹配，移动单词指针。
   - 如果单词指针到达末尾，说明该单词是 $s$ 的子序列。

**优化**：将单词按首字母分组，每次只处理首字母匹配的单词。

### 思路 1：代码

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        
        # 将单词按首字母分组，存储 (单词, 当前匹配位置)
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append((word, 0))
        
        count = 0
        
        # 遍历 s 中的每个字符
        for char in s:
            # 获取所有等待匹配当前字符的单词
            current_waiting = waiting[char]
            waiting[char] = []
            
            for word, index in current_waiting:
                index += 1
                if index == len(word):
                    # 单词匹配完成
                    count += 1
                else:
                    # 继续等待下一个字符
                    waiting[word[index]].append((word, index))
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是字符串 $s$ 的长度，$m$ 是所有单词的总长度。每个字符最多被访问一次。
- **空间复杂度**：$O(m)$。需要存储所有单词的状态。
