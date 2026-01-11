# [0418. 屏幕可显示句子的数量](https://leetcode.cn/problems/sentence-screen-fitting/)

- 标签：数组、字符串、动态规划
- 难度：中等

## 题目链接

- [0418. 屏幕可显示句子的数量 - 力扣](https://leetcode.cn/problems/sentence-screen-fitting/)

## 题目大意

**描述**：

给定一个句子数组 $sentence$ 和屏幕的行数 $rows$ 和列数 $cols$。

句子中的单词用空格分隔，需要按顺序在屏幕上显示。如果一行放不下当前单词，则将单词移到下一行。句子循环显示。

**要求**：

返回屏幕上可以显示多少次完整的句子。

**说明**：

- $1 \le sentence.length \le 100$。
- $1 \le sentence[i].length \le 10$。
- $sentence[i]$ 只包含小写英文字母。
- $1 \le rows, cols \le 2 \times 10^4$。

**示例**：

- 示例 1：

```python
输入：sentence = ["hello","world"], rows = 2, cols = 8
输出：1
解释：
hello---
world---
可以显示 1 次完整的句子。
```

- 示例 2：

```python
输入：sentence = ["a", "bcd", "e"], rows = 3, cols = 6
输出：2
解释：
a-bcd-
e-a---
bcd-e-
可以显示 2 次完整的句子。
```

## 解题思路

### 思路 1：模拟 + 优化

给定一个句子数组 $sentence$ 和屏幕的行数 $rows$ 和列数 $cols$，需要计算屏幕上可以显示多少次完整的句子。

**核心思路**：

- 将句子拼接成一个循环字符串（单词之间用空格分隔）。
- 模拟在屏幕上逐行填充字符。
- 使用优化：预计算从每个单词开始，一行可以放下多少个字符。

**解题步骤**：

1. 将句子拼接成字符串，单词之间用空格分隔，形成 `"word1 word2 ... wordn "`。
2. 使用变量 $start$ 记录当前在句子字符串中的位置。
3. 对于每一行：
   - 计算这一行可以放下多少个字符：$start += cols$。
   - 如果 $start$ 位置是空格，继续向后跳过空格。
   - 如果 $start$ 位置不是空格，需要回退到上一个空格（保证单词完整）。
4. 最后计算 $start$ 除以句子长度，得到完整句子的次数。

### 思路 1：代码

```python
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # 拼接句子，单词之间用空格分隔
        s = ' '.join(sentence) + ' '
        n = len(s)
        start = 0  # 当前在句子字符串中的位置
        
        for _ in range(rows):
            # 这一行可以放下 cols 个字符
            start += cols
            
            # 如果当前位置是空格，可以继续向后
            if s[start % n] == ' ':
                start += 1
            else:
                # 回退到上一个空格（保证单词完整）
                while start > 0 and s[(start - 1) % n] != ' ':
                    start -= 1
        
        # 计算完整句子的次数
        return start // n
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(rows \times cols)$，最坏情况下每行需要回退 $cols$ 次。实际上，由于单词长度有限，回退次数通常很少。
- **空间复杂度**：$O(m)$，其中 $m$ 是句子的总长度。
