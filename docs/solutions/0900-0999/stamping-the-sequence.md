# [0936. 戳印序列](https://leetcode.cn/problems/stamping-the-sequence/)

- 标签：栈、贪心、队列、字符串
- 难度：困难

## 题目链接

- [0936. 戳印序列 - 力扣](https://leetcode.cn/problems/stamping-the-sequence/)

## 题目大意

**描述**：

你想要用小写字母组成一个目标字符串 $target$。

开始的时候，序列由 $target.length$ 个 `'?'` 记号组成。而你有一个小写字母印章 $stamp$。

在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 $10 \times target.length$ 个回合。

举个例子，如果初始序列为 `"?????"`，而你的印章 $stamp$ 是 `"abc"`，那么在第一回合，你可以得到 `"abc??"`、`"?abc?"`、`"??abc"`。（请注意，印章必须完全包含在序列的边界内才能盖下去。）

**要求**：

如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。

例如，如果序列是 `"ababc"`，印章是 `"abc"`，那么我们就可以返回与操作 `"?????"` -> `"abc??"` -> `"ababc"` 相对应的答案 $[0, 2]$；

另外，如果可以印出序列，那么需要保证可以在 $10 \times target.length$ 个回合内完成。任何超过此数字的答案将不被接受。

**说明**：

- $1 \le stamp.length \le target.length \le 10^{3}$
- $stamp$ 和 $target$ 只包含小写字母。

**示例**：

- 示例 1：

```python
输入：stamp = "abc", target = "ababc"
输出：[0,2]
（[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
```

- 示例 2：

```python
输入：stamp = "abca", target = "aabcaca"
输出：[3,0,1]
```

## 解题思路

### 思路 1：逆向思维 + 贪心

这道题正向思考比较困难，我们可以逆向思考：从目标字符串 $target$ 逆推回全 `?` 的初始状态。

1. 将 $target$ 转换为字符数组，方便修改。
2. 从后往前，每次找到一个可以被"擦除"的位置（即该位置的字符可以被替换为 `?`）。
3. 一个位置可以被擦除的条件是：该位置的字符与 $stamp$ 匹配，或者已经是 `?`。
4. 每次擦除后，记录擦除的起始位置。
5. 重复上述过程，直到所有字符都变成 `?`。
6. 最后将记录的位置反转，即为答案。

### 思路 1：代码

```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        target = list(target)  # 转换为列表方便修改
        result = []
        visited = [False] * n  # 标记是否已经被戳印覆盖
        stars = 0  # 记录 '?' 的数量
        
        # 检查从位置 pos 开始是否可以戳印
        def canStamp(pos):
            changed = False
            for i in range(m):
                if target[pos + i] == '?':
                    continue
                if target[pos + i] != stamp[i]:
                    return False
                changed = True
            return changed
        
        # 从位置 pos 开始戳印（将字符替换为 '?'）
        def doStamp(pos):
            nonlocal stars
            for i in range(m):
                if target[pos + i] != '?':
                    target[pos + i] = '?'
                    stars += 1
        
        # 不断尝试戳印，直到所有字符都变成 '?'
        while stars < n:
            stamped = False
            for i in range(n - m + 1):
                if not visited[i] and canStamp(i):
                    doStamp(i)
                    result.append(i)
                    visited[i] = True
                    stamped = True
            # 如果一轮下来没有任何戳印，说明无法完成
            if not stamped:
                return []
        
        # 反转结果（因为是逆向推导）
        return result[::-1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times (n - m))$，其中 $n$ 是 $target$ 的长度，$m$ 是 $stamp$ 的长度。最多需要 $n$ 次戳印，每次需要检查 $O(n - m)$ 个位置。
- **空间复杂度**：$O(n)$，需要存储 $target$ 的字符数组和访问标记数组。
