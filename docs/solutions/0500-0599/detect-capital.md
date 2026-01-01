# [0520. 检测大写字母](https://leetcode.cn/problems/detect-capital/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0520. 检测大写字母 - 力扣](https://leetcode.cn/problems/detect-capital/)

## 题目大意

**描述**：

我们定义，在以下情况时，单词的大写用法是正确的：

- 全部字母都是大写，比如 `"USA"`。
- 所有字母都不是大写，比如 `"leetcode"`。
- 只有首字母大写， 比如 `"Google"`。

给定一个字符串 $word$。

**要求**：

如果大写用法正确，返回 true；否则，返回 false。

**说明**：

- $1 \le word.length \le 10^{3}$。
- word 由小写和大写英文字母组成。

**示例**：

- 示例 1：

```python
输入：word = "USA"
输出：true
```

- 示例 2：

```python
输入：word = "FlaG"
输出：false
```

## 解题思路

### 思路 1：分类判断

根据题目要求，大写用法正确的情况有三种：

1. 全部字母都是大写
2. 所有字母都不是大写
3. 只有首字母大写

我们可以统计字符串中大写字母的数量 $upper\_count$ 和总长度 $n$：

- 如果 $upper\_count == 0$：所有字母都不是大写，正确
- 如果 $upper\_count == n$：全部字母都是大写，正确
- 如果 $upper\_count == 1$ 且首字母是大写：只有首字母大写，正确
- 其他情况：不正确

### 思路 1：代码

```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        upper_count = sum(1 for c in word if c.isupper())
        
        # 全部小写
        if upper_count == 0:
            return True
        
        # 全部大写
        if upper_count == n:
            return True
        
        # 只有首字母大写
        if upper_count == 1 and word[0].isupper():
            return True
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度，需要遍历字符串统计大写字母数量。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
