# [0937. 重新排列日志文件](https://leetcode.cn/problems/reorder-data-in-log-files/)

- 标签：数组、字符串、排序
- 难度：中等

## 题目链接

- [0937. 重新排列日志文件 - 力扣](https://leetcode.cn/problems/reorder-data-in-log-files/)

## 题目大意

**描述**：

给定一个日志数组 $logs$。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的「标识符」。

有两种不同类型的日志：

- 字母日志：除标识符之外，所有字均由小写字母组成
- 数字日志：除标识符之外，所有字均由数字组成

请按下述规则将日志重新排序：

- 所有「字母日志」都排在「数字日志」之前。
- 「字母日志」在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
- 「数字日志」应该保留原来的相对顺序。

**要求**：

返回日志的最终顺序。

**说明**：

- $1 \le logs.length \le 10^{3}$。
- $3 \le logs[i].length \le 10^{3}$。
- $logs[i]$ 中，字与字之间都用 单个 空格分隔。
- 题目数据保证 $logs[i]$ 都有一个标识符，并且在标识符之后至少存在一个字。

**示例**：

- 示例 1：

```python
输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
解释：
字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
```

- 示例 2：

```python
输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

## 解题思路

### 思路 1：自定义排序

根据题目要求，需要对日志进行自定义排序。

1. **分类日志**：将日志分为字母日志和数字日志。
2. **排序规则**：
   - 字母日志排在数字日志之前
   - 字母日志按内容排序，内容相同时按标识符排序
   - 数字日志保持原有顺序
3. **实现方式**：使用自定义排序函数，返回排序键。

### 思路 1：代码

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_key(log):
            identifier, content = log.split(' ', 1)
            
            # 判断是字母日志还是数字日志
            if content[0].isalpha():
                # 字母日志：返回 (0, 内容, 标识符)
                return (0, content, identifier)
            else:
                # 数字日志：返回 (1,)，保持原有顺序
                return (1,)
        
        return sorted(logs, key=sort_key)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n \cdot m)$，其中 $n$ 是日志数量，$m$ 是日志的平均长度。排序需要 $O(n \log n)$ 次比较，每次比较需要 $O(m)$ 时间。
- **空间复杂度**：$O(n \cdot m)$，排序需要的额外空间。
