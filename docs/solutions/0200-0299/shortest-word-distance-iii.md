# [0245. 最短单词距离 III](https://leetcode.cn/problems/shortest-word-distance-iii/)

- 标签：数组、字符串
- 难度：中等

## 题目链接

- [0245. 最短单词距离 III - 力扣](https://leetcode.cn/problems/shortest-word-distance-iii/)

## 题目大意

**描述**：

给定一个字符串数组 $wordsDict$ 和两个字符串 $word1$ 和 $word2$。

**要求**：

返回这两个单词在列表中出现的最短距离。

**说明**：

- 注意：$word1$ 和 $word2$ 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。
- $1 \le wordsDict.length \le 10^{5}$。
- $1 \le wordsDict[i].length \le 10$。
- $wordsDict[i]$ 由小写英文字母组成。
- $word1$ 和 $word2$ 都在 $wordsDict$ 中。

**示例**：

- 示例 1：

```python
输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
输出：1
```

- 示例 2：

```python
输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
输出：3
```

## 解题思路

### 思路 1：双指针

这道题与前面两题的区别在于 $word1$ 和 $word2$ 可能相同。当两个单词相同时，我们需要找到同一个单词在数组中的两个不同位置之间的最短距离。

具体步骤如下：

1. 遍历数组 $wordsDict$，维护两个指针 $index1$ 和 $index2$ 分别记录 $word1$ 和 $word2$ 的最新位置。
2. 当遇到 $word1$ 时：
   - 如果 $word1 \neq word2$，直接更新 $index1$ 为当前位置。
   - 如果 $word1 = word2$，需要特殊处理：先将 $index2$ 更新为之前的 $index1$，再将 $index1$ 更新为当前位置。
3. 当遇到 $word2$ 且 $word1 \neq word2$ 时，更新 $index2$ 为当前位置。
4. 当 $index1$ 和 $index2$ 都有效且 $index1 \neq index2$ 时，计算距离 $|index1 - index2|$ 并更新最小距离。
5. 最终返回最小距离。

这种方法只需要遍历一次数组，时间复杂度为 $O(n)$，空间复杂度为 $O(1)$。

### 思路 1：代码

```python
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # 初始化两个指针，-1 表示还未找到对应的单词
        index1, index2 = -1, -1
        # 初始化最小距离为数组长度
        min_distance = len(wordsDict)
        
        # 遍历数组
        for i in range(len(wordsDict)):
            # 如果当前单词是 word1
            if wordsDict[i] == word1:
                # 如果 word1 和 word2 相同，需要特殊处理
                if word1 == word2:
                    # 先更新 index2 为之前的 index1，再更新 index1 为当前位置
                    if index1 != -1:
                        index2 = index1
                    index1 = i
                else:
                    # 如果不同，直接更新 index1
                    index1 = i
            # 如果当前单词是 word2 且与 word1 不同
            elif wordsDict[i] == word2:
                index2 = i
            
            # 如果两个单词都找到了且不是同一个位置，计算距离并更新最小值
            if index1 != -1 and index2 != -1 and index1 != index2:
                min_distance = min(min_distance, abs(index1 - index2))
        
        return min_distance
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $wordsDict$ 的长度。我们只需要遍历一次数组。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
