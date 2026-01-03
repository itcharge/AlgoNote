# [0791. 自定义字符串排序](https://leetcode.cn/problems/custom-sort-string/)

- 标签：哈希表、字符串、排序
- 难度：中等

## 题目链接

- [0791. 自定义字符串排序 - 力扣](https://leetcode.cn/problems/custom-sort-string/)

## 题目大意

**描述**：

给定两个字符串 $order$ 和 $s$。$order$ 的所有字母都是「唯一」的，并且以前按照一些自定义的顺序排序。

对 $s$ 的字符进行置换，使其与排序的 $order$ 相匹配。更具体地说，如果在 $order$ 中的字符 $x$ 出现字符 $y$ 之前，那么在排列后的字符串中，$x$ 也应该出现在 $y$ 之前。

**要求**：

返回满足这个性质的 $s$ 的任意一种排列。

**说明**：

- $1 \le order.length \le 26$。
- $1 \le s.length \le 200$。
- $order$ 和 $s$ 由小写英文字母组成。
- $order$ 中的所有字符都不同。

**示例**：

- 示例 1：

```python
输入: order = "cba", s = "abcd"
输出: "cbad"
解释: 
"a"、"b"、"c"是按顺序出现的，所以"a"、"b"、"c"的顺序应该是"c"、"b"、"a"。
因为"d"不是按顺序出现的，所以它可以在返回的字符串中的任何位置。"dcba"、"cdba"、"cbda"也是有效的输出。
```

- 示例 2：

```python
输入: order = "cbafg", s = "abcd"
输出: "cbad"
解释：字符 "b"、"c" 和 "a" 规定了 s 中字符的顺序。s 中的字符 "d" 没有在 order 中出现，所以它的位置是弹性的。

按照出现的顺序，s 中的 "b"、"c"、"a" 应排列为"b"、"c"、"a"。"d" 可以放在任何位置，因为它没有按顺序排列。输出 "bcad" 遵循这一规则。其他排序如 "dbca" 或 "bcda" 也是有效的，只要维持 "b"、"c"、"a" 的顺序。
```

## 解题思路

### 思路 1：自定义排序

这道题要求按照 $order$ 中的顺序对 $s$ 进行排序。

**解题步骤**：

1. 使用哈希表记录 $order$ 中每个字符的优先级（位置索引）。
2. 对于不在 $order$ 中的字符，赋予一个较大的优先级，使其排在后面。
3. 使用自定义排序函数，按照优先级对 $s$ 中的字符进行排序。

**优化方法**：
- 可以先统计 $s$ 中每个字符的出现次数。
- 按照 $order$ 的顺序，依次将字符添加到结果中。
- 最后将不在 $order$ 中的字符添加到结果末尾。

### 思路 1：代码

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 统计 s 中每个字符的出现次数
        from collections import Counter
        count = Counter(s)
        
        result = []
        
        # 按照 order 的顺序添加字符
        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]
        
        # 添加不在 order 中的字符
        for char, freq in count.items():
            result.append(char * freq)
        
        return ''.join(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是字符串 $s$ 的长度，$m$ 是字符串 $order$ 的长度。需要遍历两个字符串各一次。
- **空间复杂度**：$O(|\Sigma|)$，其中 $|\Sigma|$ 是字符集大小（这里是 $26$）。需要存储字符计数。
