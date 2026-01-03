# [0748. 最短补全词](https://leetcode.cn/problems/shortest-completing-word/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [0748. 最短补全词 - 力扣](https://leetcode.cn/problems/shortest-completing-word/)

## 题目大意

**描述**：

「补全词」是一个包含 $licensePlate$ 中所有字母的单词。忽略 $licensePlate$ 中的「数字和空格」。不区分大小写。如果某个字母在 $licensePlate$ 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。

例如：`licensePlate = "aBc 12c"`，那么它的补全词应当包含字母 `'a'`、`'b'` （忽略大写）和两个 `'c'`。可能的「补全词」有 `"abccdef"`、`"caaacab"` 以及 `"cbca"`。

给定一个字符串 $licensePlate$ 和一个字符串数组 $words$。

**要求**：

请你找出 $words$ 中的「最短补全词」。

题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 $words$ 中 第一个 出现的那个。


**说明**：

- $1 \le licensePlate.length \le 7$。
- $licensePlate$ 由数字、大小写字母或空格 `' '` 组成。
- $1 \le words.length \le 10^{3}$。
- $1 \le words[i].length \le 15$。
- $words[i]$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
解释：最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。
"step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。
"steps" 包含 "t"、"p" 和两个 "s"。
"stripe" 缺一个 "s"。
"stepple" 缺一个 "s"。
因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。
```

- 示例 2：

```python
输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
输出："pest"
解释：licensePlate 只包含字母 "s" 。所有的单词都包含字母 "s" ，其中 "pest"、"stew"、和 "show" 三者最短。答案是 "pest" ，因为它是三个单词中在 words 里最靠前的那个。
```

## 解题思路

### 思路 1：哈希表

补全词是包含 $licensePlate$ 中所有字母的单词（忽略数字、空格和大小写）。我们需要找到最短的补全词。

**实现步骤**：

1. 统计 $licensePlate$ 中每个字母（转为小写）的出现次数，忽略数字和空格。
2. 遍历 $words$ 中的每个单词：
   - 统计单词中每个字母的出现次数。
   - 检查单词是否包含 $licensePlate$ 中所有字母（次数要足够）。
3. 在所有补全词中，返回长度最短的那个（如果有多个，返回第一个）。

### 思路 1：代码

```python
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        
        # 统计 licensePlate 中字母的出现次数（忽略数字和空格，转为小写）
        plate_count = Counter()
        for char in licensePlate:
            if char.isalpha():
                plate_count[char.lower()] += 1
        
        result = None
        min_length = float('inf')
        
        # 遍历每个单词
        for word in words:
            word_count = Counter(word)
            
            # 检查是否是补全词
            is_completing = True
            for char, count in plate_count.items():
                if word_count[char] < count:
                    is_completing = False
                    break
            
            # 更新最短补全词
            if is_completing and len(word) < min_length:
                result = word
                min_length = len(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是 $words$ 的长度，$m$ 是单词的平均长度。
- **空间复杂度**：$O(1)$，字母表大小固定为 $26$。
