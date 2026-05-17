# [1249. 移除无效的括号](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/)

- 标签：栈、字符串
- 难度：中等

## 题目链接

- [1249. 移除无效的括号 - 力扣](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/)

## 题目大意

**描述**：给定一个由 `'('`、`')'` 和小写字母组成的字符串 $s$。

**要求**：从字符串中移除最少数量的括号（可以移除任意位置的括号），使得剩下的字符串是有效的括号字符串。返回所有可能的有效字符串中，任意一个即可。

有效括号字符串的定义：
- 空字符串是有效的。
- 如果 $A$ 是有效的，那么 $(A)$ 也是有效的。
- 如果 $A$ 和 $B$ 都是有效的，那么 $AB$ 也是有效的。

**说明**：

- $1 \le s.length \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" 和 "lee(t(c)ode)" 也是有效答案。
```

- 示例 2：

```python
输入：s = "a)b(c)d"
输出："ab(c)d"
```

- 示例 3：

```python
输入：s = "))(("
输出：""
解释：空字符串也是有效的。
```

## 解题思路

### 思路 1：栈

#### 1. 核心思想

括号匹配的经典工具是**栈**。遍历字符串时：
- 遇到 `'('` 将其下标入栈。
- 遇到 `')'`：
  - 如果栈不为空（说明有未匹配的 `'('`），栈顶出栈，这对括号匹配成功。
  - 如果栈为空（说明没有未匹配的 `'('`），这个 `')'` 是多余的，需要移除。

遍历结束后，栈中剩余的下标对应的是**没有匹配的 `'('`**，也需要移除。

移除这些位置的字符即可得到有效字符串。

#### 2. 具体步骤

**第 1 步**：初始化一个栈 $stack$（存储 `'('` 的下标），和一个集合 $remove$（存储需要移除的字符下标）。

**第 2 步**：遍历字符串 $s$：
- 如果 $s[i] == \text{'('}$，将 $i$ 入栈。
- 如果 $s[i] == \text{')'}$：
  - 如果栈不为空，栈顶出栈（匹配成功）。
  - 如果栈为空，将 $i$ 加入 $remove$（多余的右括号）。

**第 3 步**：遍历结束后，栈中剩余的下标都是未匹配的 `'('`，加入 $remove$。

**第 4 步**：遍历原字符串，跳过 $remove$ 中的下标，将剩余字符拼接成结果字符串返回。

#### 3. 结合示例走一遍

$s = \text{"lee(t(c)o)de)"}$

```
i=0  'l' → 字母，跳过
i=1  'e' → 字母，跳过
i=2  'e' → 字母，跳过
i=3  '(' → stack=[3]
i=4  't' → 字母，跳过
i=5  '(' → stack=[3,5]
i=6  'c' → 字母，跳过
i=7  ')' → stack.pop()=5，匹配成功，stack=[3]
i=8  'o' → 字母，跳过
i=9  ')' → stack.pop()=3，匹配成功，stack=[]
i=10 'd' → 字母，跳过
i=11 'e' → 字母，跳过
i=12 ')' → stack为空 → remove={12}
```

栈为空，遍历结束，$remove = \{12\}$。

跳过下标 $12$ 的字符 `')'`，结果为 `"lee(t(c)o)de"`。

### 思路 1：代码

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []      # 存储 '(' 的下标
        remove = set()  # 需要移除的字符下标

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()  # 配对成功
                else:
                    remove.add(i)  # 多余的右括号

        # 未匹配的左括号也需要移除
        remove.update(stack)

        # 构建结果字符串
        ans = []
        for i, ch in enumerate(s):
            if i not in remove:
                ans.append(ch)
        return ''.join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串的长度。只需两次遍历。
- **空间复杂度**：$O(n)$，栈和集合在最坏情况下需要 $O(n)$ 空间。

### 思路 2：两次遍历（不依赖栈）

#### 1. 核心思想

不用栈也可以：从左到右遍历，记录当前未匹配 `'('` 的数量。遇到 `')'` 时，如果未匹配 `'('` 数量为 $0$，则这个 `')'` 是多余的，标记移除。最后再把多余的 `'('` 从右到左移除。

#### 2. 代码

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 第一轮：从左到右，移除多余的右括号
        open_count = 0
        arr = list(s)
        for i, ch in enumerate(arr):
            if ch == '(':
                open_count += 1
            elif ch == ')':
                if open_count == 0:
                    arr[i] = ''  # 标记移除
                else:
                    open_count -= 1

        # 第二轮：从右到左，移除多余的左括号
        close_count = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == ')':
                close_count += 1
            elif arr[i] == '(':
                if close_count == 0:
                    arr[i] = ''  # 标记移除
                else:
                    close_count -= 1

        return ''.join(arr)
```

#### 3. 复杂度分析

- **时间复杂度**：$O(n)$，两次遍历。
- **空间复杂度**：$O(n)$，将字符串转为列表修改。

思路 2 省去了集合和栈的额外空间，但本质上是相同的思路（第一轮处理多余的 `')'`，第二轮处理多余的 `'('`）。
