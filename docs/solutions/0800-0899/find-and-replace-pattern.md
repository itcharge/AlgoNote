# [0890. 查找和替换模式](https://leetcode.cn/problems/find-and-replace-pattern/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0890. 查找和替换模式 - 力扣](https://leetcode.cn/problems/find-and-replace-pattern/)

## 题目大意

**描述**：

你有一个单词列表 $words$ 和一个模式 $pattern$，你想知道 $words$ 中的哪些单词与模式匹配。

如果存在字母的排列 $p$ ，使得将模式中的每个字母 $x$ 替换为 $p$($x$) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

**要求**：

返回 $words$ 中与给定模式匹配的单词列表。

你可以按任何顺序返回答案。

**说明**：

- $1 \le words.length \le 50$。
- $1 \le pattern.length = words[i].length \le 20$。

**示例**：

- 示例 1：

```python
示例：

输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。
```

## 解题思路

### 思路 1：哈希表 + 双射映射

这道题要求找出与给定模式匹配的单词。单词与模式匹配的条件是：存在一个字母的排列（双射），使得将模式中的每个字母替换后得到该单词。

双射的含义是：

- 模式中的每个字母映射到单词中的唯一字母。
- 单词中的每个字母也只能由模式中的唯一字母映射而来。

算法步骤：

1. 对于每个单词，检查它是否与模式匹配。
2. 使用两个哈希表分别记录从模式到单词、从单词到模式的映射关系。
3. 遍历模式和单词的每个字符：
   - 如果模式字符已有映射，检查是否与当前单词字符一致。
   - 如果单词字符已有映射，检查是否与当前模式字符一致。
   - 如果不一致，说明不匹配。
4. 如果所有字符都匹配，将该单词加入结果。

### 思路 1：代码

```python
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word, pattern):
            # 检查 word 是否与 pattern 匹配
            if len(word) != len(pattern):
                return False
            
            # 两个哈希表分别记录双向映射
            map_p_to_w = {}  # 模式到单词的映射
            map_w_to_p = {}  # 单词到模式的映射
            
            for w_char, p_char in zip(word, pattern):
                # 检查模式到单词的映射
                if p_char in map_p_to_w:
                    if map_p_to_w[p_char] != w_char:
                        return False
                else:
                    map_p_to_w[p_char] = w_char
                
                # 检查单词到模式的映射
                if w_char in map_w_to_p:
                    if map_w_to_p[w_char] != p_char:
                        return False
                else:
                    map_w_to_p[w_char] = p_char
            
            return True
        
        # 筛选出与模式匹配的单词
        result = []
        for word in words:
            if match(word, pattern):
                result.append(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是单词列表的长度，$m$ 是单词的平均长度。需要遍历每个单词并检查是否匹配。
- **空间复杂度**：$O(m)$，需要使用两个哈希表存储映射关系。
