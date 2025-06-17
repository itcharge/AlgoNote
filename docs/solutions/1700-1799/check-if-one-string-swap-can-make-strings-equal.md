# [1790. 仅执行一次字符串交换能否使两个字符串相等](https://leetcode.cn/problems/check-if-one-string-swap-can-make-strings-equal/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1790. 仅执行一次字符串交换能否使两个字符串相等 - 力扣](https://leetcode.cn/problems/check-if-one-string-swap-can-make-strings-equal/)

## 题目大意

**描述**：给定两个长度相等的字符串 `s1` 和 `s2`。

已知一次「字符串交换操作」步骤如下：选出某个字符串中的两个下标（不一定要相同），并交换这两个下标所对应的字符。

**要求**：如果对其中一个字符串执行最多一次字符串交换可以使两个字符串相等，则返回 `True`；否则返回 `False`。

**说明**：

- $1 \le s1.length, s2.length \le 100$。
- $s1.length == s2.length$。
- `s1` 和 `s2` 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
给定：s1 = "bank", s2 = "kanb"
输出：True
解释：交换 s1 中的第一个和最后一个字符可以得到 "kanb"，与 s2 相同
```

## 解题思路

### 思路 1：

- 用一个变量 `diff_cnt` 记录两个字符串中对应位置上出现不同字符的次数。用 `c1`、`c2` 记录第一次出现不同字符时两个字符串对应位置上的字符。
- 遍历两个字符串，对于第 `i` 个位置的字符 `s1[i]` 和 `s2[i]`：
  - 如果 `s1[i] == s2[i]`，继续判断下一个位置。
  - 如果 `s1[i] != s2[i]`，则出现不同字符的次数加 `1`。
  - 如果出现不同字符的次数等于 `1`，则记录第一次出现不同字符时两个字符串对应位置上的字符。
  - 如果出现不同字符的次数等于 `2`，则判断第一次出现不同字符时两个字符串对应位置上的字符与当前位置字符交换之后是否相等。如果不等，则说明交换之后 `s1` 和 `s2` 不相等，返回 `False`。如果相等，则继续判断下一个位置。
  - 如果出现不同字符的次数超过 `2`，则不符合最多一次字符串交换的要求，返回 `False`。
- 如果遍历完，出现不同字符的次数为 `0` 或者 `2`，为 `0` 说明无需交换，本身 `s1` 和 `s2` 就是相等的，为 `2` 说明交换一次字符串之后  `s1` 和 `s2`  相等，此时返回 `True`。否则返回 `False`。

## 代码

### 思路 1 代码：

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        size = len(s1)
        diff_cnt = 0
        c1, c2 = None, None
        for i in range(size):
            if s1[i] == s2[i]:
                continue
            diff_cnt += 1
            if diff_cnt == 1:
                c1 = s1[i]
                c2 = s2[i]
            elif diff_cnt == 2:
                if c1 != s2[i] or c2 != s1[i]:
                    return False
            else:
                return False

        return diff_cnt == 0 or diff_cnt == 2
```

