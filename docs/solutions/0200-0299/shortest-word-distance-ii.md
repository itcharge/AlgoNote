# [0244. 最短单词距离 II](https://leetcode.cn/problems/shortest-word-distance-ii/)

- 标签：设计、数组、哈希表、双指针、字符串
- 难度：中等

## 题目链接

- [0244. 最短单词距离 II - 力扣](https://leetcode.cn/problems/shortest-word-distance-ii/)

## 题目大意

**要求**：

请设计一个类，使该类的构造函数能够接收一个字符串数组。然后再实现一个方法，该方法能够分别接收两个单词，并返回列表中这两个单词之间的最短距离。

实现 `WordDistanc` 类:

- `WordDistance(String[] wordsDict)` 用字符串数组 $wordsDict$ 初始化对象。
* `int shortest(String word1, String word2)` 返回数组 $worddict$ 中 $word1$ 和 $word2$ 之间的最短距离。

**说明**：

- $1 \le wordsDict.length <= 3 \times 10^{4}$
- $1 \le wordsDict[i].length \le 10$。
* $wordsDict[i]$ 由小写英文字母组成。
* $word1$ 和 $word2$ 在数组 $wordsDict$ 中。
* $word1 \ne word2$。
* `shortest` 操作次数不大于 $5000$。

**示例**：

- 示例 1：

```python
输入: 
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
输出:
[null, 3, 1]

解释：
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // 返回 3
wordDistance.shortest("makes", "coding");    // 返回 1
```

## 解题思路

### 思路 1：哈希表 + 双指针

由于 `shortest` 方法会被多次调用，我们需要在构造函数中预处理数据，将每个单词的所有位置索引存储起来，这样在查询时可以快速找到两个单词的所有位置，然后使用双指针方法计算最短距离。

具体步骤如下：

1. 在构造函数中，遍历 $wordsDict$ 数组，使用哈希表 $word\_positions$ 记录每个单词 $word$ 在数组中的所有位置索引。
2. 在 `shortest` 方法中，获取 $word1$ 和 $word2$ 的所有位置列表 $positions1$ 和 $positions2$。
3. 使用双指针 $i$ 和 $j$ 分别指向 $positions1$ 和 $positions2$ 的当前位置。
4. 比较 $positions1[i]$ 和 $positions2[j]$ 的距离，移动较小位置的指针。
5. 重复步骤 4 直到遍历完所有位置，返回最小距离。

这种方法的时间复杂度为 $O(m + n)$，其中 $m$ 和 $n$ 分别是 $word1$ 和 $word2$ 在数组中的出现次数。

### 思路 1：代码

```python
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # 使用哈希表存储每个单词的所有位置索引
        self.word_positions = {}
        
        # 遍历数组，记录每个单词的位置
        for i, word in enumerate(wordsDict):
            if word not in self.word_positions:
                self.word_positions[word] = []
            self.word_positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # 获取两个单词的所有位置列表
        positions1 = self.word_positions[word1]
        positions2 = self.word_positions[word2]
        
        # 初始化双指针和最小距离
        i, j = 0, 0
        min_distance = float('inf')
        
        # 使用双指针遍历两个位置列表
        while i < len(positions1) and j < len(positions2):
            # 计算当前位置的距离
            distance = abs(positions1[i] - positions2[j])
            min_distance = min(min_distance, distance)
            
            # 移动较小位置的指针
            if positions1[i] < positions2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 构造函数：$O(n)$，其中 $n$ 是 $wordsDict$ 的长度。
  - `shortest` 方法：$O(m + n)$，其中 $m$ 和 $n$ 分别是 $word1$ 和 $word2$ 在数组中的出现次数。
- **空间复杂度**：$O(n)$，用于存储每个单词的位置索引。
