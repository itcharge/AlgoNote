# [0451. 根据字符出现频率排序](https://leetcode.cn/problems/sort-characters-by-frequency/)

- 标签：哈希表、字符串、桶排序、计数、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0451. 根据字符出现频率排序 - 力扣](https://leetcode.cn/problems/sort-characters-by-frequency/)

## 题目大意

**描述**：给定一个字符串 `s`。

**要求**：将字符串 `s` 里的字符按照出现的频率降序排列。如果有多个答案，返回其中任何一个。

**说明**：

- $1 \le s.length \le 5 * 10^5$。
- `s` 由大小写英文字母和数字组成。

**示例**：

- 示例 1：

```python
输入: s = "tree"
输出: "eert"
解释: 'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
```

- 示例 2：

```python
输入: s = "cccaaa"
输出: "cccaaa"
解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
```

## 解题思路

### 思路 1：优先队列

1. 使用哈希表 `s_dict` 统计字符频率。
2. 然后遍历哈希表 `s_dict`，将字符以及字符频数存入优先队列中。
3. 将优先队列中频数最高的元素依次加入答案数组中。
4. 最后拼接答案数组为字符串，将其返回。

### 思路 1：代码

```python
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # 统计元素频数
        s_dict = dict()
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
        
        priority_queue = []
        for ch in s_dict:
            heapq.heappush(priority_queue, (-s_dict[ch], ch))
        
        res = []
        while priority_queue:
            ch = heapq.heappop(priority_queue)[-1]
            times = s_dict[ch]
            while times:
                res.append(ch)
                times -= 1
        return ''.join(res)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n  + k \times log_2k)$。其中 $n$ 为字符串 $s$ 的长度，$k$ 是字符串中不同字符的个数。
- **空间复杂度**：$O(n + k)$。

