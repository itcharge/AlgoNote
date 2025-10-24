# [0472. 连接词](https://leetcode.cn/problems/concatenated-words/)

- 标签：深度优先搜索、字典树、数组、字符串、动态规划、排序
- 难度：困难

## 题目链接

- [0472. 连接词 - 力扣](https://leetcode.cn/problems/concatenated-words/)

## 题目大意

**描述**：

给定一个「不含重复」单词的字符串数组 $words$。

**要求**：

请你找出并返回 $words$ 中的所有 连接词。

**说明**：

- 连接词：一个完全由给定数组中的至少两个较短单词（不一定是不同的两个单词）组成的字符串。
- $1 \le words.length \le 10^{4}$。
- $1 \le words[i].length \le 30$。
- $words[i]$ 仅由小写英文字母组成。
- $words$ 中的所有字符串都是唯一的。
- $1 \le sum(words[i].length) \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
```

- 示例 2：

```python
输入：words = ["cat","dog","catdog"]
输出：["catdog"]
```

## 解题思路

### 思路 1：深度优先搜索 + 记忆化

1. 首先将 $words$ 数组按长度排序，这样可以确保在处理较长的单词时，所有较短的单词都已经被处理过。
2. 对于每个单词 $word$，使用深度优先搜索来判断它是否可以由其他单词组成。
3. 定义函数 `canForm(word, wordSet)` 来判断单词 $word$ 是否可以由集合 $wordSet$ 中的单词组成。
4. 在 `canForm` 函数中，使用记忆化来避免重复计算。定义 $memo[i]$ 表示从位置 $i$ 开始的后缀是否可以由其他单词组成。
5. 对于每个位置 $i$，尝试所有可能的前缀 $word[i:j+1]$，如果前缀在 $wordSet$ 中，则递归检查后缀 $word[j+1:]$。
6. 如果找到任何一个有效的前缀和后缀组合，则返回 $True$。
7. 将可以组成的单词添加到结果列表中。

### 思路 1：代码

```python
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 按长度排序，确保处理长单词时短单词已经处理过
        words.sort(key=len)
        
        result = []
        word_set = set()
        
        def canForm(word, wordSet):
            """判断单词是否可以由集合中的其他单词组成"""
            if not word:
                return True
            
            # 记忆化数组，memo[i] 表示从位置 i 开始的后缀是否可以组成
            memo = {}
            
            def dfs(start):
                if start in memo:
                    return memo[start]
                
                if start == len(word):
                    return True
                
                # 尝试所有可能的前缀
                for end in range(start + 1, len(word) + 1):
                    prefix = word[start:end]
                    # 如果前缀在集合中，且不是当前单词本身
                    if prefix in wordSet and prefix != word:
                        if dfs(end):
                            memo[start] = True
                            return True
                
                memo[start] = False
                return False
            
            return dfs(0)
        
        # 逐个处理每个单词
        for word in words:
            if canForm(word, word_set):
                result.append(word)
            # 将当前单词添加到集合中，供后续单词使用
            word_set.add(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m^3)$，其中 $n$ 是单词的数量，$m$ 是单词的平均长度。对于每个单词，最坏情况下需要检查所有可能的前缀和后缀组合。
- **空间复杂度**：$O(n \times m)$，其中 $n$ 是单词的数量，$m$ 是单词的平均长度。主要用于存储单词集合和记忆化数组。
