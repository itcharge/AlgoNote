# [1002. 查找共用字符](https://leetcode.cn/problems/find-common-characters/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [1002. 查找共用字符 - 力扣](https://leetcode.cn/problems/find-common-characters/)

## 题目大意

**描述**：给定一个字符串数组 $words$。

**要求**：找出所有在 $words$ 的每个字符串中都出现的公用字符（包括重复字符），并以数组形式返回。可以按照任意顺序返回答案。

**说明**：

- $1 \le words.length \le 100$。
- $1 \le words[i].length \le 100$。
- $words[i]$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：words = ["bella","label","roller"]
输出：["e","l","l"]
```

- 示例 2：

```python
输入：words = ["cool","lock","cook"]
输出：["c","o"]
```

## 解题思路

### 思路 1：哈希表

如果某个字符 $ch$ 在所有字符串中都出现了 $k$ 次以上，则最终答案中需要包含 $k$ 个 $ch$。因此，我们可以使用哈希表 $minfreq[ch]$ 记录字符 $ch$ 在所有字符串中出现的最小次数。具体步骤如下：

1. 定义长度为 $26$ 的哈希表 $minfreq$，初始化所有字符出现次数为无穷大，$minfreq[ch] = float('inf')$。
2. 遍历字符串数组中的所有字符串 $word$，对于字符串 $word$：
   1. 记录 $word$ 中所有字符串的出现次数 $freq[ch]$。
   2. 取 $freq[ch]$ 与 $minfreq[ch]$ 中的较小值更新 $minfreq[ch]$。
3. 遍历完之后，再次遍历 $26$ 个字符，将所有最小出现次数大于零的字符按照出现次数存入答案数组中。
4. 最后将答案数组返回。

### 思路 1：代码

```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        minfreq = [float('inf') for _ in range(26)]
        for word in words:
            freq = [0 for _ in range(26)]
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        res = []
        for i in range(26):
            while minfreq[i]:
                res.append(chr(i + ord('a')))
                minfreq[i] -= 1
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times (|\sum| + m))$，其中 $n$ 为字符串数组 $words$ 的长度，$m$ 为每个字符串的平均长度，$|\sum|$ 为字符集。
- **空间复杂度**：$O(|\sum|)$。

