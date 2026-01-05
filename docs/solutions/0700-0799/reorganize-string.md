# [0767. 重构字符串](https://leetcode.cn/problems/reorganize-string/)

- 标签：贪心、哈希表、字符串、计数、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0767. 重构字符串 - 力扣](https://leetcode.cn/problems/reorganize-string/)

## 题目大意

**描述**：

给定一个字符串 $s$。

**要求**：

检查是否能重新排布其中的字母，使得两相邻的字符不同。

返回 $s$ 的任意可能的重新排列。若不可行，返回空字符串 `""`。

**说明**：

- $1 \le s.length \le 500$。
- $s$ 只包含小写字母。

**示例**：

- 示例 1：

```python
输入: s = "aab"
输出: "aba"
```

- 示例 2：

```python
输入: s = "aaab"
输出: ""
```

## 解题思路

### 思路 1：贪心 + 堆

要使相邻字符不同，我们应该优先放置出现次数最多的字符。使用最大堆来维护字符的出现次数。

**实现步骤**：

1. 统计每个字符的出现次数。
2. 如果某个字符的出现次数超过 $\lceil \frac{n}{2} \rceil$，则无法重排，返回空字符串。
3. 使用最大堆，每次取出出现次数最多的字符：
   - 如果结果字符串为空或最后一个字符与当前字符不同，直接添加。
   - 否则，取出次多的字符添加，然后将之前的字符放回堆中。
4. 重复直到所有字符都被添加。

### 思路 1：代码

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq
        
        # 统计字符出现次数
        count = Counter(s)
        n = len(s)
        
        # 如果某个字符出现次数超过 (n + 1) // 2，无法重排
        if max(count.values()) > (n + 1) // 2:
            return ""
        
        # 使用最大堆（Python 的 heapq 是最小堆，所以用负数）
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)
        
        result = []
        
        while heap:
            # 取出出现次数最多的字符
            first_cnt, first_char = heapq.heappop(heap)
            
            # 如果结果为空或最后一个字符与当前字符不同
            if not result or result[-1] != first_char:
                result.append(first_char)
                # 如果还有剩余，放回堆中
                if first_cnt + 1 < 0:
                    heapq.heappush(heap, (first_cnt + 1, first_char))
            else:
                # 需要取次多的字符
                if not heap:
                    return ""
                second_cnt, second_char = heapq.heappop(heap)
                result.append(second_char)
                # 放回第一个字符
                heapq.heappush(heap, (first_cnt, first_char))
                # 如果第二个字符还有剩余，放回堆中
                if second_cnt + 1 < 0:
                    heapq.heappush(heap, (second_cnt + 1, second_char))
        
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log k)$，其中 $n$ 是字符串长度，$k$ 是不同字符的个数（最多 $26$）。
- **空间复杂度**：$O(k)$，堆的空间。
