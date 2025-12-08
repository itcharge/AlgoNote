# [1247. 交换字符使得字符串相同](https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal/)

- 标签：贪心、数学、字符串
- 难度：中等

## 题目链接

- [1247. 交换字符使得字符串相同 - 力扣](https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal/)

## 题目大意

**描述**：给定两个长度相同的字符串 $s1$ 和 $s2$，并且两个字符串中只含有字符 `'x'` 和 `'y'`。现在需要通过「交换字符」的方式使两个字符串相同。

- 每次「交换字符」，需要分别从两个字符串中各选一个字符进行交换。
- 「交换字符」只能发生在两个不同的字符串之间，不能发生在同一个字符串内部。

**要求**：返回使 $s1$ 和 $s2$ 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 $-1$。

**说明**：

- $1 \le s1.length, s2.length \le 1000$。
- $s1$、$s2$ 只包含 `'x'` 或 `'y'`。

**示例**：

- 示例 1：

```python
输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
```

## 解题思路

### 思路 1：贪心算法

- 如果 $s1 == s2$，则不需要交换。
- 如果 `s1 = "xx"`，`s2 = "yy"`，则最少需要交换一次，才可以使两个字符串相等。
- 如果 `s1 = "yy"`，`s2 = "xx"`，则最少需要交换一次，才可以使两个字符串相等。
- 如果 `s1 = "xy"`，`s2 = "yx"`，则最少需要交换两次，才可以使两个字符串相等。
- 如果 `s1 = "yx"`，`s2 = "xy"`，则最少需要交换两次，才可以使两个字符串相等。

则可以总结为：

- `"xx"` 与 `"yy"`、`"yy"` 与 `"xx"` 只需要交换一次。
- `"xy"` 与 `"yx"`、`"yx"` 与 `"xy"` 需要交换两次。

我们把这两种情况分别进行统计。

- 当遇到 $s1[i] == s2[i]$ 时直接跳过。
- 当遇到 $s1[i] \ne s2[i]$ 时：
	- 如果 `s1[i] == 'x'`，`s2[i] == 'y'`，则统计数量到变量 $xyCnt$ 中。
	- 如果 `s1[i] == 'y'`，`s2[i] == 'y'`，则统计数量到变量 $yxCnt$ 中。


则最后我们只需要判断 $xyCnt$ 和 $yxCnt$ 的个数即可。

- 如果 $xyCnt + yxCnt$ 是奇数，则说明最终会有一个位置上的两个字符无法通过交换相匹配。
- 如果 $xyCnt + yxCnt$ 是偶数，并且 $xyCnt$ 为偶数，则 $yxCnt$ 也为偶数。则优先交换 `"xx"` 与 `"yy"`、`"yy"` 与 `"xx"`。即每两个 $xyCnt$ 对应一次交换，每两个 $yxCnt$ 对应交换一次，则结果为 $xyCnt \div 2 + yxCnt \div 2$。
- 如果 $xyCnt + yxCnt$ 是偶数，并且 $xyCnt$ 为奇数，则 $yxCnt$ 也为奇数。则优先交换 `"xx"` 与 `"yy"`、`"yy"` 与 `"xx"`。即每两个 $xyCnt$ 对应一次交换，每两个 $yxCnt$ 对应交换一次，则结果为 $xyCnt \div 2 + yxCnt \div 2$。最后还剩一组 `"xy"` 与 `"yx"` 或者 `"yx"` 与 `"xy"`，则再交换一次，则结果为 $xyCnt \div 2 + yxCnt \div 2 + 2$。

以上结果可以统一写成 $xyCnt \div 2 + yxCnt \div 2 + xyCnt \mod 2 \times 2$。

### 思路 1：贪心算法代码

```python
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xyCnt, yxCnt = 0, 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] == 'x':
                xyCnt += 1
            else:
                yxCnt += 1

        if (xyCnt + yxCnt) & 1:
            return -1
        return xyCnt // 2 + yxCnt // 2 + (xyCnt % 2 * 2)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串的长度。
- **空间复杂度**：$O(1)$。
