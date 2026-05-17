# [1189. "气球" 的最大数量](https://leetcode.cn/problems/maximum-number-of-balloons/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1189. "气球" 的最大数量 - 力扣](https://leetcode.cn/problems/maximum-number-of-balloons/)

## 题目大意

**描述**：给定一个字符串 $text$，里面的每个字母最多用一次。可以用 $text$ 中的字母拼出单词 `"balloon"`。

**要求**：最多能拼出多少个 `"balloon"`？

**说明**：

- $1 \le text.length \le 10^4$。
- $text$ 只含小写英文字母。

**示例**：

```python
输入：text = "loonbalxballpoon"
输出：2
```

## 解题思路

### 思路 1：计数取最小值

`"balloon"` 由 5 种字母组成：b、a、l、o、n，其中 l 和 o 各需要 2 个，其他各需要 1 个。

所以只要统计 $text$ 中这 5 种字母的数量，然后看能组成几个完整的 `"balloon"` 即可。由于 l 和 o 需要 2 个，它们要除以 2 再比较。

**步骤拆解：**

1. 统计 $text$ 中 b、a、l、o、n 的出现次数。
2. 把 l 和 o 的次数除以 2。
3. 返回 5 种字母中能凑出的最小值。

### 思路 1：代码

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        
        count = Counter(text)  # 统计每个字母出现了几次
        
        # 能拼出的 "balloon" 数量取决于 5 种字母中最紧缺的那个
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,  # 需要 2 个
            count['o'] // 2,  # 需要 2 个
            count['n']
        )
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。遍历一次字符串就够了。
- **空间复杂度**：$O(1)$。只有 26 个小写字母，计数器大小是常数。
