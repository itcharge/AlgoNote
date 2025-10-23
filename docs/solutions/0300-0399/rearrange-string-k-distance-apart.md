# [0358. K 距离间隔重排字符串](https://leetcode.cn/problems/rearrange-string-k-distance-apart/)

- 标签：贪心、哈希表、字符串、计数、排序、堆（优先队列）
- 难度：困难

## 题目链接

- [0358. K 距离间隔重排字符串 - 力扣](https://leetcode.cn/problems/rearrange-string-k-distance-apart/)

## 题目大意

**描述**：

给定一个非空的字符串 $s$ 和一个整数 $k$。

**要求**：

你要将这个字符串 $s$ 中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离「至少」为 $k$。如果无法做到，请返回一个空字符串 `""`。

**说明**：

- $1 \le s.length \le 3 \times 10^{5}$。
- $s$ 仅由小写英文字母组成。
- $0 \le k \le s.length$。

**示例**：

- 示例 1：

```python
输入: s = "aabbcc", k = 3
输出: "abcabc" 
解释: 相同的字母在新的字符串中间隔至少 3 个单位距离。
```

- 示例 2：

```python
输入: s = "aaabc", k = 3
输出: "" 
解释: 没有办法找到可能的重排结果。
```

## 解题思路

### 思路 1：贪心算法 + 优先队列

这道题的核心思想是贪心策略：每次选择剩余字符中频率最高的字符，但要确保它与之前放置的字符保持至少 $k$ 的距离。

###### 1. 问题分析

- 统计每个字符的出现频率 $freq[c]$。
- 使用优先队列（最大堆）维护字符频率，优先选择频率高的字符。
- 维护一个队列记录最近使用的字符，确保距离约束。

###### 2. 算法步骤

1. **统计频率**：遍历字符串 $s$，统计每个字符 $c$ 的出现次数 $freq[c]$。
2. **构建优先队列**：将所有字符按频率降序放入优先队列。
3. **贪心放置**：
   - 每次从优先队列中取出频率最高的字符。
   - 如果该字符与最近 $k-1$ 个位置上的字符不同，则放置。
   - 将使用过的字符放入等待队列，当距离满足条件时重新加入优先队列。
4. **检查可行性**：如果无法放置所有字符，返回空字符串。

###### 3. 关键变量

- $freq[c]$：字符 $c$ 的出现频率。
- $wait\_queue$：等待队列，存储最近使用的字符。
- $result$：结果字符串。
- $used\_chars$：最近使用的字符集合。

### 思路 1：代码

```python
import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # 特殊情况：k <= 1 时不需要间隔
        if k <= 1:
            return s
        
        # 统计字符频率
        freq = Counter(s)
        
        # 构建最大堆（使用负数实现）
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-count, char))
        
        # 等待队列，存储最近使用的字符
        wait_queue = deque()
        result = []
        
        while max_heap:
            # 取出频率最高的字符
            neg_count, char = heapq.heappop(max_heap)
            count = -neg_count
            
            # 将字符添加到结果中
            result.append(char)
            
            # 将使用过的字符加入等待队列
            wait_queue.append((count - 1, char))
            
            # 如果等待队列长度达到 k-1，说明可以重新使用最早使用的字符
            if len(wait_queue) >= k:
                old_count, old_char = wait_queue.popleft()
                # 如果该字符还有剩余，重新加入优先队列
                if old_count > 0:
                    heapq.heappush(max_heap, (-old_count, old_char))
        
        # 检查是否所有字符都被使用
        if len(result) == len(s):
            return ''.join(result)
        else:
            return ""
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log m)$，其中 $n$ 为字符串长度，$m$ 为不同字符的数量。每个字符最多被处理 $O(n)$ 次，每次堆操作的时间复杂度为 $O(\log m)$。
- **空间复杂度**：$O(m)$，其中 $m$ 为不同字符的数量。用于存储字符频率、优先队列和等待队列。
