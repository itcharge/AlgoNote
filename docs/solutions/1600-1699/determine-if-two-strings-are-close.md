# [1657. 确定两个字符串是否接近](https://leetcode.cn/problems/determine-if-two-strings-are-close/)

- 标签：哈希表、字符串、排序
- 难度：中等

## 题目链接

- [1657. 确定两个字符串是否接近 - 力扣](https://leetcode.cn/problems/determine-if-two-strings-are-close/)

## 题目大意

**描述**：如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

- 操作 1：交换任意两个现有字符。
  - 例如，`abcde` -> `aecdb`。
- 操作 2：将一个 现有 字符的每次出现转换为另一个现有字符，并对另一个字符执行相同的操作。
  - 例如，`aacabb` -> `bbcbaa`（所有 `a` 转化为 `b`，而所有的 `b` 转换为 `a` ）。

给定两个字符串，$word1$ 和 $word2$。

**要求**：如果 $word1$ 和 $word2$ 接近 ，就返回 $True$；否则，返回 $False$。

**说明**：

- $1 \le word1.length, word2.length \le 10^5$。
- $word1$ 和 $word2$ 仅包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：word1 = "abc", word2 = "bca"
输出：True
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"
```

- 示例 2：

```python
输入：word1 = "a", word2 = "aa"
输出：False
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```

## 解题思路

### 思路 1：模拟

无论是操作 1，还是操作 2，只是对字符位置进行交换，而不会产生或者删除字符。

则我们只需要检查两个字符串的字符种类以及每种字符的个数是否相同即可。

具体步骤如下：

1. 分别使用哈希表 $cnts1$、$cnts2$ 统计每个字符串中的字符种类，每种字符的个数。
2. 判断两者的字符种类是否相等，并且判断每种字符的个数是否相同。
3. 如果字符种类相同，且每种字符的个数完全相同，则返回 $True$，否则，返回 $False$。

### 思路 1：代码

```Python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnts1 = Counter(word1)
        cnts2 = Counter(word2)

        return cnts1.keys() == cnts2.keys() and sorted(cnts1.values()) == sorted(cnts2.values())
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(max(n1, n2) + |\sum| \times \log | \sum |)$，其中 $n1$、$n2$ 分别为字符串 $word1$、$word2$ 的长度，$\sum$ 为字符集，本题中 $| \sum | = 26$。
- **空间复杂度**：$O(| \sum |)$。

