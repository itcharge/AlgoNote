# [1209. 删除字符串中的所有相邻重复项 II](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/)

- 标签：栈、字符串
- 难度：中等

## 题目链接

- [1209. 删除字符串中的所有相邻重复项 II - 力扣](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/)

## 题目大意

**描述**：给定一个字符串 $s$ 和一个整数 $k$，你需要反复删除字符串中连续 $k$ 个相同的相邻字符，直到无法继续删除为止。

**要求**：返回最终得到的字符串。

**说明**：

- $1 \le s.length \le 10^{5}$。
- $2 \le k \le 10^{4}$。
- $s$ 中只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "abcd", k = 2
输出："abcd"
解释：没有连续 2 个相同的相邻字符。
```

- 示例 2：

```python
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：先删 "eee" → "ddbbcccbdaa" → 删 "ccc" → "ddbbbdaa" → 删 "bbb" → "dddaa" → 删 "ddd" → "aa"
```

- 示例 3：

```python
输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"
```

## 解题思路

### 思路 1：栈

#### 1. 核心思想

用栈来模拟删除过程。栈中每个元素为 $(字符, 连续出现次数)$。

遍历字符串时：
- 如果当前字符和栈顶字符相同，栈顶计数加 $1$。
- 如果栈顶计数达到 $k$，删除栈顶。
- 如果当前字符和栈顶字符不同，入栈 $(当前字符, 1)$。

#### 2. 具体步骤

**第 1 步**：初始化栈 $stack = []$。

**第 2 步**：遍历 $s$ 中的每个字符 $ch$：
- 如果 $stack$ 不为空且 $stack[-1][0] == ch$：
  - $stack[-1][1] += 1$。
  - 如果 $stack[-1][1] == k$，弹出栈顶。
- 否则：$stack.append((ch, 1))$。

**第 3 步**：遍历结束后，根据栈中的 $(字符, 次数)$ 构建最终字符串。

#### 3. 结合示例走一遍

$s = \text{"deeedbbcccbdaa"}, k = 3$

```
ch='d' → stack=[(d,1)]
ch='e' → stack=[(d,1),(e,1)]
ch='e' → stack=[(d,1),(e,2)]
ch='e' → stack=[(d,1),(e,3)] → 计数=3，弹出 → stack=[(d,1)]
ch='d' → stack=[(d,2)]
ch='b' → stack=[(d,2),(b,1)]
ch='b' → stack=[(d,2),(b,2)]
ch='c' → stack=[(d,2),(b,2),(c,1)]
ch='c' → stack=[(d,2),(b,2),(c,2)]
ch='c' → stack=[(d,2),(b,2),(c,3)] → 弹出 → stack=[(d,2),(b,2)]
ch='b' → stack=[(d,2),(b,3)] → 弹出 → stack=[(d,2)]
ch='d' → stack=[(d,3)] → 弹出 → stack=[]
ch='a' → stack=[(a,1)]
ch='a' → stack=[(a,2)]
```

最终栈为空？不对，最后 `"aa"` 的 $k=3$ 达不到 → stack=[(a,2)]

但结果应该是 "aa"... 再想想。是的，k=3 但只有 2 个 a，所以删不掉。

等等，让我重新做一遍示例 2：

$s = \text{"deeedbbcccbdaa"}, k=3$

```
d → [(d,1)]
e → [(d,1),(e,1)]
e → [(d,1),(e,2)]
e → [(d,1),(e,3)] → 弹出 e → [(d,1)]
d → [(d,2)]
b → [(d,2),(b,1)]
b → [(d,2),(b,2)]
c → [(d,2),(b,2),(c,1)]
c → [(d,2),(b,2),(c,2)]
c → [(d,2),(b,2),(c,3)] → 弹出 c → [(d,2),(b,2)]
b → [(d,2),(b,3)] → 弹出 b → [(d,2)]
d → [(d,3)] → 弹出 d → []
a → [(a,1)]
a → [(a,2)]
```

最终 stack = [(a,2)]，构建得到 "aa"。✓

### 思路 1：代码

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # 元素为 (字符, 连续出现次数)
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        # 构建结果字符串
        ans = []
        for ch, cnt in stack:
            ans.append(ch * cnt)
        return ''.join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。每个字符入栈出栈最多一次。
- **空间复杂度**：$O(n)$，栈空间。
