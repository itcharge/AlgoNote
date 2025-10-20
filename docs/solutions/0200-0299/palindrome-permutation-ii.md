# [0267. 回文排列 II](https://leetcode.cn/problems/palindrome-permutation-ii/)

- 标签：哈希表、字符串、回溯
- 难度：中等

## 题目链接

- [0267. 回文排列 II - 力扣](https://leetcode.cn/problems/palindrome-permutation-ii/)

## 题目大意

**描述**：

给定一个字符串 $s$。

**要求**：

返回「其重新排列组合后可能构成的所有回文字符串，并去除重复的组合」。

你可以按任意顺序返回答案。如果 $s$ 不能形成任何回文排列时，则返回一个空列表。

**说明**：

- $1 \le s.length \le 16$。
- $s$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入: s = "aabb"
输出: ["abba", "baab"]
```

- 示例 2：

```python
输入: s = "abc"
输出: []
```

## 解题思路

### 思路 1：

先统计每个字符出现次数。记字符串长度为 $n$，各字符计数为 $\{c_i\}$。如果出现次数为奇数的字符超过 $1$ 个，则无法构成回文，直接返回空列表。

如果至多 $1$ 个字符出现奇数次：

- 将每个字符取一半次数（即 $\lfloor c_i/2 \rfloor$）构造「左半部分」可用的多重集合，记其总长度为 $m = \sum_i \lfloor c_i/2 \rfloor$。
- 通过回溯在该多重集合上生成所有不重复的半串 $h$（长度为 $m$），回溯过程中对每个字符仅按计数使用，避免因相同字符导致的重复。
- 若存在奇数计数字符，记其中点字符为 $mid$，否则 `mid = ""`。对每个半串 $h$，构造回文 $h + mid + h^R$。

正确性：回文由对称的两半与可选中点构成，穷举半串可唯一确定一个回文。去重依赖「基于计数的回溯」，不会对同一字符的相同选择顺序重复生成。

### 思路 1：代码

```python
from typing import List
from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # 统计每个字符的频次
        freq = Counter(s)

        # 检查是否可构成回文：至多 1 个奇数频次
        odd_chars = [ch for ch, cnt in freq.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return []

        # 中间字符（若存在奇数频次）
        mid = odd_chars[0] if odd_chars else ""

        # 半串的可用字符次数（每种字符取一半）
        half_counts = {ch: cnt // 2 for ch, cnt in freq.items()}
        target_len = sum(half_counts.values())

        path: List[str] = []  # 当前构造的半串
        res: List[str] = []   # 结果集合

        # 回溯基于计数，不会产生重复排列
        def dfs() -> None:
            if len(path) == target_len:
                half = "".join(path)
                res.append(half + mid + half[::-1])
                return

            for ch in sorted(half_counts.keys()):  # 固定遍历顺序，稳定输出
                if half_counts[ch] == 0:
                    continue
                half_counts[ch] -= 1
                path.append(ch)
                dfs()
                path.pop()
                half_counts[ch] += 1

        dfs()
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：令 $m = \sum_i \lfloor c_i/2 \rfloor$。半串的唯一排列数为 $\dfrac{m!}{\prod_i (\lfloor c_i/2 \rfloor)!}$。对每个半串构造完整回文需要 $O(n)$ 拼接与拷贝，因此总复杂度为 $O\!\left(\dfrac{m!}{\prod_i (\lfloor c_i/2 \rfloor)!} \cdot n\right)$。在 $n \le 16$ 的约束下不会超时。
- **空间复杂度**：回溯深度与路径为 $O(m)$，计数表为 $O(\Sigma)$（$\Sigma$ 为字符集大小，这里为小写字母）。不计输出的额外空间为 $O(m + \Sigma)$。
