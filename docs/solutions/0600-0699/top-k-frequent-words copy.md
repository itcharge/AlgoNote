# [0692. 前K个高频单词](https://leetcode.cn/problems/top-k-frequent-words/)

- 标签：字典树、数组、哈希表、字符串、桶排序、计数、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0692. 前K个高频单词 - 力扣](https://leetcode.cn/problems/top-k-frequent-words/)

## 题目大意

**描述**：

给定一个单词列表 $words$ 和一个整数 $k$。

**要求**：

返回前 $k$ 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字典顺序排序。

**说明**：

- $1 \le words.length \le 500$。
- $1 \le words[i].length \le 10$。
- $words[i]$ 由小写英文字母组成。
- $k$ 的取值范围是 $[1, \text{不同 words[i] 的数量}]$

- 进阶：尝试以 $O(n \log k)$ 时间复杂度和 $O(n)$ 空间复杂度解决。

**示例**：

- 示例 1：

```python
输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
```

- 示例 2：

```python
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
```

## 解题思路

### 思路 1：哈希表 + 排序

这道题目要求找出前 $k$ 个出现频率最高的单词，频率相同时按字典序排序。

1. 使用哈希表统计每个单词的出现频率。
2. 将哈希表中的单词按照以下规则排序：
   - 首先按频率从高到低排序。
   - 频率相同时按字典序从小到大排序。
3. 返回排序后的前 $k$ 个单词。

### 思路 1：代码

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        
        # 统计单词频率
        freq = Counter(words)
        
        # 按照频率从高到低，频率相同时按字典序从小到大排序
        result = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        # 返回前 k 个单词
        return result[:k]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是不同单词的数量。统计频率需要 $O(m)$（$m$ 是单词总数），排序需要 $O(n \log n)$。
- **空间复杂度**：$O(n)$，需要使用哈希表存储单词频率。

## 解题思路

### 思路 2：堆（优先队列）+ 哈希表

使用最小堆来优化时间复杂度，只维护前 $k$ 个高频单词。

1. 使用哈希表统计每个单词的出现频率。
2. 使用最小堆维护前 $k$ 个高频单词：
   - 堆的大小最多为 $k$。
   - 堆中元素按照频率从小到大排序，频率相同时按字典序从大到小排序（这样可以保证频率小的或字典序大的在堆顶，会被优先弹出）。
3. 遍历哈希表，将单词加入堆：
   - 直接将单词加入堆。
   - 如果堆的大小超过 $k$，弹出堆顶元素（频率最小的，或频率相同时字典序最大的）。
4. 将堆中的元素按照频率从高到低、频率相同时按字典序从小到大排序后返回。

**关键点**：使用自定义类来实现堆的比较逻辑，确保频率相同时字典序大的在堆顶。

### 思路 2：代码

```python
from collections import Counter
import heapq

# 自定义类，用于堆的比较
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        # 频率不同时，频率小的在堆顶
        if self.freq != other.freq:
            return self.freq < other.freq
        # 频率相同时，字典序大的在堆顶（会被弹出）
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # 统计单词频率
        freq = Counter(words)
        
        # 使用最小堆
        heap = []
        
        for word, count in freq.items():
            heapq.heappush(heap, Word(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 按照频率从高到低，频率相同时按字典序从小到大排序
        heap.sort(key=lambda x: (-x.freq, x.word))
        
        return [x.word for x in heap]
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n \log k)$，其中 $n$ 是不同单词的数量。统计频率需要 $O(m)$（$m$ 是单词总数），维护大小为 $k$ 的堆需要 $O(n \log k)$，最后排序需要 $O(k \log k)$。
- **空间复杂度**：$O(n)$，需要使用哈希表存储单词频率，堆的大小为 $O(k)$。
