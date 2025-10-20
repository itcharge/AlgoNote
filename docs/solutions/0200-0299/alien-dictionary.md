# [0269. 火星词典](https://leetcode.cn/problems/alien-dictionary/)

- 标签：深度优先搜索、广度优先搜索、图、拓扑排序、数组、字符串
- 难度：困难

## 题目链接

- [0269. 火星词典 - 力扣](https://leetcode.cn/problems/alien-dictionary/)

## 题目大意

**描述**：

现有一种使用英语字母的火星语言，这门语言的字母顺序对你来说是未知的。

给定一个来自这种外星语言字典的字符串列表 $words$ ，$words$ 中的字符串已经「按这门新语言的字典序进行了排序」。

**要求**：

如果这种说法是错误的，并且给出的 $words$ 不能对应任何字母的顺序，则返回 `""`。

否则，返回一个按新语言规则的「字典递增顺序」排序的独特字符串。如果有多个解决方案，则返回其中任意一个。

**说明**：

- $1 \le words.length \le 10^{3}$。
- $1 \le words[i].length \le 10^{3}$。
- $words[i]$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
```

- 示例 2：

```python
输入：words = ["z","x"]
输出："zx"
```

## 解题思路

### 思路 1：拓扑排序 + 广度优先搜索

使用拓扑排序来解决这个问题。我们需要构建一个图来表示字母之间的相对顺序关系，然后使用拓扑排序来找到字母的正确顺序。

具体步骤如下：

1. 构建图：遍历相邻的单词对 $(words[i], words[i+1])$，找到第一个不同的字符，建立字符 $c_1$ 到字符 $c_2$ 的边，表示 $c_1$ 在 $c_2$ 之前。
2. 计算入度：统计每个字符的入度 $indegree[c]$。
3. 拓扑排序：使用广度优先搜索，从入度为 $0$ 的字符开始，逐步构建字母顺序。
4. 验证结果：检查是否所有字符都被包含在结果中。

关键点：

- 如果存在环，说明无法确定字母顺序，返回空字符串。
- 如果拓扑排序后仍有字符未被访问，说明存在环。
- 需要处理所有出现的字符，包括那些没有相对顺序关系的字符。

### 思路 1：代码

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 构建图：字符到其后继字符的映射
        graph = {}
        # 统计每个字符的入度
        indegree = {}
        
        # 初始化所有出现的字符
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
                if char not in indegree:
                    indegree[char] = 0
        
        # 构建图：比较相邻单词
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # 检查是否存在前缀关系
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # 找到第一个不同的字符，建立边关系
                    char1, char2 = word1[j], word2[j]
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegree[char2] += 1
                    break
            else:
                # 如果所有字符都相同，但第一个单词更长，则无效
                if len(word1) > len(word2):
                    return ""
        
        # 拓扑排序：使用广度优先搜索
        queue = []
        # 找到所有入度为 0 的字符
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
        
        result = []
        while queue:
            char = queue.pop(0)
            result.append(char)
            
            # 处理当前字符的所有后继字符
            for next_char in graph[char]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    queue.append(next_char)
        
        # 检查是否所有字符都被访问（无环）
        if len(result) != len(indegree):
            return ""
        
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(C)$，其中 $C$ 是所有单词中字符的总数。需要遍历所有字符来构建图和进行拓扑排序。
- **空间复杂度**：$O(1)$，因为字符集大小固定为 $26$ 个字母，所以图的大小和入度数组都是常数级别。
