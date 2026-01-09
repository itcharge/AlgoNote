# [0916. 单词子集](https://leetcode.cn/problems/word-subsets/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0916. 单词子集 - 力扣](https://leetcode.cn/problems/word-subsets/)

## 题目大意

**描述**：

给定两个字符串数组 $words1$ 和 $words2$。

现在，如果 $b$ 中的每个字母都出现在 $a$ 中，包括重复出现的字母，那么称字符串 $b$ 是字符串 $a$ 的「子集」。

- 例如，`"wrr"` 是 `"warrior"` 的子集，但不是 `"world"` 的子集。

如果对 $words2$ 中的每一个单词 $b$，$b$ 都是 $a$ 的子集，那么我们称 $words1$ 中的单词 $a$ 是「通用单词」。

**要求**：

以数组形式返回 $words1$ 中所有的「通用」单词。你可以按任意顺序返回答案。

**说明**：

- $1 \le words1.length, words2.length \le 10^{4}$。
- $1 \le words1[i].length, words2[i].length \le 10$。
- $words1[i]$ 和 $words2[i]$ 仅由小写英文字母组成。
- $words1$ 中的所有字符串「互不相同」。

**示例**：

- 示例 1：

```python
输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

输出：["facebook","google","leetcode"]
```

- 示例 2：

```python
输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

输出：["leetcode"]
```

## 解题思路

### 思路 1：哈希表

对于 $words1$ 中的每个单词，检查它是否包含 $words2$ 中所有单词的字母（包括重复）。

1. 首先统计 $words2$ 中每个字母的最大需求量（对所有单词取并集）。
2. 对于 $words1$ 中的每个单词，统计其字母频率。
3. 检查该单词是否满足 $words2$ 的所有字母需求。
4. 如果满足，将该单词加入结果列表。

### 思路 1：代码

```python
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # 统计 words2 中每个字母的最大需求量
        max_freq = collections.Counter()
        for word in words2:
            freq = collections.Counter(word)
            for char, count in freq.items():
                max_freq[char] = max(max_freq[char], count)
        
        result = []
        # 检查 words1 中的每个单词
        for word in words1:
            freq = collections.Counter(word)
            # 检查是否满足所有字母需求
            is_universal = True
            for char, count in max_freq.items():
                if freq[char] < count:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n_1 \times m_1 + n_2 \times m_2)$，其中 $n_1$ 和 $n_2$ 分别是 $words1$ 和 $words2$ 的长度，$m_1$ 和 $m_2$ 是单词的平均长度。
- **空间复杂度**：$O(1)$，字母表大小固定为 $26$。
