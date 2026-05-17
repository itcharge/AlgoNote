# [1153. 字符串转化](https://leetcode.cn/problems/string-transforms-into-another-string/)

- 标签：图、哈希表、字符串
- 难度：困难

## 题目链接

- [1153. 字符串转化 - 力扣](https://leetcode.cn/problems/string-transforms-into-another-string/)

## 题目大意

**描述**：给出两个长度相同的字符串 $str1$ 和 $str2$。每次转化，你可以将 $str1$ 中出现的**所有**相同字母变成其他**任何**小写英文字母。

**要求**：判断 $str1$ 能否通过零次或多次转化变成 $str2$。

**说明**：

- $1 \le str1.length = str2.length \le 10^4$。
- 字符串中只会出现小写英文字母。

**示例**：

- 示例 1：

```python
输入：str1 = "aabcc", str2 = "ccdee"
输出：true
解释：将 'c' 变成 'e'，然后把 'b' 变成 'd'，接着再把 'a' 变成 'c'。注意，转化的顺序也很重要。
```

- 示例 2：

```python
输入：str1 = "leetcode", str2 = "codeleet"
输出：false
```

## 解题思路

### 思路 1：图 + 哈希表

**核心限制条件**：

1. **映射一致性**：$str1$ 中的同一个字符，不能映射到 $str2$ 中的不同字符。比如 $str1$ 中的 `a` 既要变成 `c` 又要变成 `d`，这不可能。

2. **26 个字符全满**：如果 $str2$ 中 26 个小写字母都出现了，那么 $str1$ 必须和 $str2$ 完全相同。因为任何有环的映射（比如 $a \to b \to a$）都需要一个临时字符来打破循环，但所有字母都在 $str2$ 中用掉了，没有多余的临时字符可用。

**拆解步骤**：

1. 如果 $str1 == str2$，直接返回 `True`。

2. **建立映射关系**：遍历两个字符串的对应位置，记录 $str1$ 中每个字符映射到 $str2$ 中的哪个字符。如果发现同一个字符映射到不同目标，返回 `False`。

3. **检查 26 个字母是否全满**：如果 $str2$ 中包含了全部 26 个小写字母，返回 `False`（因为无法处理循环映射）。

4. **通过所有检查，返回 `True`**。

### 思路 1：代码

```python
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # 如果两个字符串相同，不需要任何转化
        if str1 == str2:
            return True

        # 建立 str1 → str2 的映射关系
        mapping = {}
        for c1, c2 in zip(str1, str2):
            if c1 in mapping:
                # 同一个字符不能映射到不同目标
                if mapping[c1] != c2:
                    return False
            else:
                mapping[c1] = c2

        # 如果 str2 包含了全部 26 个字母，没有临时字符可用
        if len(set(str2)) == 26:
            return False

        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。用人话说就是：只需要遍历一次字符串，长度 $n$ 就是时间。
- **空间复杂度**：$O(1)$。映射表最多存储 26 个字符，是常数空间。
