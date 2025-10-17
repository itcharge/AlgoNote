# [0126. 单词接龙 II](https://leetcode.cn/problems/word-ladder-ii/)

- 标签：广度优先搜索、哈希表、字符串、回溯
- 难度：困难

## 题目链接

- [0126. 单词接龙 II - 力扣](https://leetcode.cn/problems/word-ladder-ii/)

## 题目大意

**描述**：

给你两个单词 $beginWord$ 和 $endWord$ ，以及一个字典 $wordList$。

**要求**：

按字典 $wordList$ 完成从单词 $beginWord$ 到单词 $endWord$ 转化，一个表示此过程的「转换序列」是形式上像 $beginWord \rightarrow s1 \rightarrow s2 \rightarrow ... \rightarrow sk$ 这样的单词序列，并满足：

- 每对相邻的单词之间仅有单个字母不同。
- 转换过程中的每个单词 $si$（$1 \le i \le k$）必须是字典 $wordList$ 中的单词。注意，$beginWord$ 不必是字典 $wordList$ 中的单词。
- $sk == endWord$。

找出并返回所有从 $beginWord$ 到 $endWord$ 的「最短转换序列」，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 $[beginWord, s1, s2, ..., sk]$ 的形式返回。

**说明**：

- $1 \le beginWord.length \le 5$。
- $endWord.length == beginWord.length$。
- $1 \le wordList.length \le 500$。
- $wordList[i].length == beginWord.length$。
- $beginWord$、$endWord$ 和 $wordList[i]$ 由小写英文字母组成。
- $beginWord \ne endWord$。
- $wordList$ 中的所有单词 互不相同。

**示例**：

- 示例 1：

```python
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

- 示例 2：

```python
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
```

## 解题思路

### 思路 1：BFS 构建图 + DFS 回溯

这道题是单词接龙的进阶版本，需要找到所有最短转换序列。我们需要先使用 BFS 找到最短路径长度，然后使用 DFS 回溯找到所有最短路径。

###### 1. 算法思路

1. **BFS 构建图**：使用 BFS 从 $beginWord$ 开始，逐层扩展，构建转换图 $graph$，同时记录每个单词到 $beginWord$ 的最短距离 $distance$。
2. **DFS 回溯找路径**：从 $endWord$ 开始，使用 DFS 回溯，只访问距离递减的路径，找到所有最短路径。

###### 2. 具体步骤

1. **预处理**：将 $wordList$ 转换为集合 $wordSet$，便于快速查找。
2. **BFS 构建图**：使用队列进行 BFS，记录每个单词的下一层可达单词和距离。
3. **DFS 回溯**：从 $endWord$ 开始，沿着距离递减的路径回溯到 $beginWord$。

###### 3. 关键变量

- $wordSet$：字典集合，用于快速查找单词是否存在
- $graph$：转换图，$graph[word]$ 存储 $word$ 可以转换到的所有单词
- $distance$：距离字典，$distance[word]$ 存储 $word$ 到 $beginWord$ 的最短距离
- $result$：存储所有找到的最短路径

### 思路 1：代码

```python
import collections
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 将 wordList 转换为集合，便于快速查找
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # 构建转换图和距离字典
        graph = collections.defaultdict(list)
        distance = {}
        
        # BFS 构建图
        queue = collections.deque([beginWord])
        distance[beginWord] = 0
        
        while queue:
            current = queue.popleft()
            if current == endWord:
                break
                
            # 尝试改变每个位置的字符
            for i in range(len(current)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != current[i]:
                        new_word = current[:i] + c + current[i+1:]
                        if new_word in wordSet:
                            if new_word not in distance:
                                distance[new_word] = distance[current] + 1
                                queue.append(new_word)
                            if distance[new_word] == distance[current] + 1:
                                graph[new_word].append(current)
        
        # 如果 endWord 不在距离字典中，说明无法到达
        if endWord not in distance:
            return []
        
        # DFS 回溯找所有最短路径
        result = []
        
        def dfs(current_word, path):
            if current_word == beginWord:
                result.append(path[::-1])  # 反转路径
                return
            
            for next_word in graph[current_word]:
                if next_word in distance and distance[next_word] == distance[current_word] - 1:
                    dfs(next_word, path + [next_word])
        
        dfs(endWord, [endWord])
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N \times M \times 26 + K \times L)$，其中 $N$ 是 $wordList$ 的长度，$M$ 是单词的长度，$K$ 是最短路径的数量，$L$ 是最短路径的长度。BFS 构建图的时间复杂度是 $O(N \times M \times 26)$，DFS 回溯的时间复杂度是 $O(K \times L)$。
- **空间复杂度**：$O(N \times M + K \times L)$，用于存储图结构、距离字典和所有最短路径。

