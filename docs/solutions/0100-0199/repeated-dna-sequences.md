# [0187. 重复的DNA序列](https://leetcode.cn/problems/repeated-dna-sequences/)

- 标签：位运算、哈希表、字符串、滑动窗口、哈希函数、滚动哈希
- 难度：中等

## 题目链接

- [0187. 重复的DNA序列 - 力扣](https://leetcode.cn/problems/repeated-dna-sequences/)

## 题目大意

**描述**：

DNA 序列由一系列核苷酸组成，缩写为 `'A'`, `'C'`, `'G'` 和 `'T'`。
* 例如，`"ACGAATTCCG"` 是一个 DNA 序列。

在研究 DNA 时，识别 DNA 中的重复序列非常有用。

给定一个表示「DNA 序列」的字符串 $s$。

**要求**：

返回所有在 DNA 分子中出现不止一次的「长度为 $10$」的序列(子字符串)。

你可以按「任意顺序」返回答案。

**说明**：

- $0 \le s.length \le 10^{5}$。
- `s[i]=='A'`、`'C'`、`'G'` or `'T'`。

**示例**：

- 示例 1：

```python
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
```

- 示例 2：

```python
输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
```

## 解题思路

### 思路 1：哈希表

我们可以使用哈希表来统计所有长度为 $10$ 的子串出现次数，然后找出出现次数大于 $1$ 的子串。

**核心思想**：

1. **滑动窗口**：使用滑动窗口遍历字符串 $s$，每次取长度为 $10$ 的子串。
2. **哈希统计**：使用哈希表 $count\_dict$ 统计每个长度为 $10$ 的子串出现次数。
3. **筛选结果**：遍历哈希表，找出出现次数大于 $1$ 的子串。

**算法步骤**：

1. **边界处理**：如果字符串长度小于 $10$，直接返回空列表。
2. **滑动窗口遍历**：从位置 $0$ 开始，每次取长度为 $10$ 的子串 $s[i:i+10]$。
3. **哈希统计**：将每个子串作为键，出现次数作为值存入哈希表。
4. **结果筛选**：遍历哈希表，将出现次数大于 $1$ 的子串加入结果列表。

**关键点**：

- 使用滑动窗口确保每个长度为 $10$ 的子串都被统计。
- 哈希表的时间复杂度为 $O(1)$，可以高效统计子串出现次数。
- 结果去重：由于使用哈希表，重复的子串只会被添加一次。

### 思路 1：代码

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 如果字符串长度小于10，直接返回空列表
        if len(s) < 10:
            return []
        
        # 使用哈希表统计每个长度为10的子串出现次数
        count_dict = {}
        
        # 滑动窗口遍历字符串
        for i in range(len(s) - 9):  # 确保有足够的字符组成长度为 10 的子串
            # 提取长度为10的子串
            substring = s[i:i + 10]
            
            # 统计子串出现次数
            count_dict[substring] = count_dict.get(substring, 0) + 1
        
        # 筛选出现次数大于1的子串
        result = []
        for substring, count in count_dict.items():
            if count > 1:
                result.append(substring)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。我们需要遍历字符串一次，每次操作的时间复杂度为 $O(1)$。
- **空间复杂度**：$O(n)$，最坏情况下需要存储 $n-9$ 个不同的长度为 $10$ 的子串。
