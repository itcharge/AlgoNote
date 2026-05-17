# [1165. 单行键盘](https://leetcode.cn/problems/single-row-keyboard/)

- 标签：哈希表、字符串
- 难度：简单

## 题目链接

- [1165. 单行键盘 - 力扣](https://leetcode.cn/problems/single-row-keyboard/)

## 题目大意

**描述**：有一个特殊的键盘，所有键排成一行。给定一个长度为 $26$ 的字符串 $keyboard$ 表示键盘布局（索引从 $0$ 到 $25$）。一开始手指在索引 $0$ 处。输入一个字符时，需要把手指移动到该字符所在的索引位置。从索引 $i$ 移到 $j$ 耗时 $|i - j|$。

**要求**：计算用一个手指输入字符串 $word$ 需要多少时间。

**说明**：

- $keyboard.length == 26$，包含每个小写英文字母恰好一次。
- $1 \le word.length \le 10^4$。

**示例**：

- 示例 1：

```python
输入：keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
输出：4
解释：从 0 号键移动到 2 号键来输出 'c'，又移动到 1 号键来输出 'b'，接着移动到 0 号键来输出 'a'。
总用时 = 2 + 1 + 1 = 4。
```

- 示例 2：

```python
输入：keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
输出：73
```

## 解题思路

### 思路 1：哈希表

**拆解步骤**：

1. **建立字母到位置的映射**：遍历 $keyboard$，用字典记录每个字母的索引位置。

2. **模拟打字过程**：
   - 手指初始位置为 $0$
   - 遍历 $word$ 中的每个字符，查出它在键盘上的位置
   - 计算手指当前位置到目标位置的距离，累加到总时间
   - 更新手指位置

3. **返回总时间**。

### 思路 1：代码

```python
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # 建立每个字母在键盘上的位置映射
        pos = {}
        for i, ch in enumerate(keyboard):
            pos[ch] = i

        curr = 0  # 手指当前位置
        total = 0  # 累计移动时间

        for ch in word:
            target = pos[ch]          # 目标字符的位置
            total += abs(curr - target)  # 累加移动距离
            curr = target                # 手指移到新位置

        return total
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$。用人话说就是：建立映射需要遍历 $keyboard$（固定 26 个字符），输入单词需要遍历每个字符，总时间和单词长度成正比。
- **空间复杂度**：$O(1)$。映射表最多存储 26 个字母，是常数空间。
