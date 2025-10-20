# [0243. 最短单词距离](https://leetcode.cn/problems/shortest-word-distance/)

- 标签：数组、字符串
- 难度：简单

## 题目链接

- [0243. 最短单词距离 - 力扣](https://leetcode.cn/problems/shortest-word-distance/)

## 题目大意

**描述**：

给定一个字符串数组 $wordDict$ 和两个已经存在于该数组中的不同的字符串 $word1$ 和 $word2$。

**要求**：

返回列表中这两个单词之间的最短距离。

**说明**：

- $1 \le wordsDict.length \le 3 \times 10^{4}$。
- $1 \le wordsDict[i].length \le 10$。
- $wordsDict[i]$ 由小写英文字母组成。
- $word1$ 和 $word2$ 在 $wordsDict$ 中。
- $word1 \ne word2$。

**示例**：

- 示例 1：

```python
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
输出: 3
```

- 示例 2：

```python
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
输出: 1
```

## 解题思路

### 思路 1：双指针

使用双指针的方法来解决这个问题。我们可以维护两个指针 $i$ 和 $j$，分别指向 $word1$ 和 $word2$ 在数组中的位置。

具体步骤如下：
1. 遍历数组 $wordsDict$，当遇到 $word1$ 时，更新指针 $i$ 为当前位置
2. 当遇到 $word2$ 时，更新指针 $j$ 为当前位置  
3. 当 $i$ 和 $j$ 都有效时（即 $i \neq -1$ 且 $j \neq -1$），计算距离 $|i - j|$ 并更新最小距离
4. 最终返回最小距离

这种方法只需要遍历一次数组，时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。

### 思路 1：代码

```python
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # 初始化两个指针，-1 表示还未找到对应的单词
        index1, index2 = -1, -1
        # 初始化最小距离为数组长度
        min_distance = len(wordsDict)
        
        # 遍历数组
        for i in range(len(wordsDict)):
            # 如果当前单词是 word1，更新 index1
            if wordsDict[i] == word1:
                index1 = i
            # 如果当前单词是 word2，更新 index2  
            elif wordsDict[i] == word2:
                index2 = i
            
            # 如果两个单词都找到了，计算距离并更新最小值
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
        
        return min_distance
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $wordsDict$ 的长度。我们只需要遍历一次数组。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
