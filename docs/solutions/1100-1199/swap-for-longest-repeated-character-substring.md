# [1156. 单字符重复子串的最大长度](https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/)

- 标签：哈希表、字符串、滑动窗口
- 难度：中等

## 题目链接

- [1156. 单字符重复子串的最大长度 - 力扣](https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/)

## 题目大意

**描述**：给定一个字符串 $text$，你最多可以交换其中两个字符的位置一次（也可以不交换）。

**要求**：返回操作后能得到的最长单字符重复子串的长度。

**说明**：

- $1 \le text.length \le 20000$。
- $text$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：text = "ababa"
输出：3
```

- 示例 2：

```python
输入：text = "aaabaaa"
输出：6
```

- 示例 3：

```python
输入：text = "aaabbaaa"
输出：4
```

## 解题思路

### 思路 1：分段统计 + 分类讨论

**拆解步骤**：

1. **统计每种字符的总出现次数**——用来判断是否有多余的字符可以"借"过来。

2. **找出每个字符的所有连续段**——记录每段的起始和结束位置。

3. **对每种字符分别计算最长可能长度**，分三种情况：
   - **不交换**：最长就是当前段的长度。
   - **从别处借一个字符**：其他地方还有这个字符，可以交换一个过来接在段尾，长度 = 段长 $+ 1$。
   - **连接两个相邻段**：两个段之间正好隔了一个字符（如 `"aaabaaa"` 中两个 `a` 段只隔了一个 `b`），把中间那个字符换成 `a`，两段就连起来了。长度为两段之和。如果其他地方还有多余的 `a`，还可以再 $+ 1$。

4. **取所有情况中的最大值**。

### 思路 1：代码

```python
from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # 统计每个字符在字符串中出现的总次数
        total_count = Counter(text)
        n = len(text)
        max_len = 0

        # 对每个字符分别处理
        for ch in total_count:
            # 找出该字符的所有连续段
            segments = []
            i = 0
            while i < n:
                if text[i] == ch:
                    start = i
                    while i < n and text[i] == ch:
                        i += 1
                    segments.append((start, i - 1))
                else:
                    i += 1

            # 分情况计算最长长度
            for i, (start, end) in enumerate(segments):
                seg_len = end - start + 1

                # 情况 1：从别处借一个字符来延长
                if total_count[ch] > seg_len:
                    max_len = max(max_len, seg_len + 1)
                else:
                    max_len = max(max_len, seg_len)

                # 情况 2：连接两个相邻段（中间隔了一个其他字符）
                if i + 1 < len(segments):
                    next_start, next_end = segments[i + 1]
                    gap = next_start - end  # 两段之间的距离
                    if gap == 2:  # 中间只隔了一个字符
                        combined = seg_len + (next_end - next_start + 1)
                        if total_count[ch] > combined:
                            max_len = max(max_len, combined + 1)
                        else:
                            max_len = max(max_len, combined)

        return max_len
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：只需要遍历字符串几次（一次统计字符出现次数，一次找出连续段），每次遍历都是线性时间。
- **空间复杂度**：$O(n)$。需要存储每个字符的连续段信息。
