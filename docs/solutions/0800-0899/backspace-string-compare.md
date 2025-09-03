# [0844. 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/)

- 标签：栈、双指针、字符串、模拟
- 难度：简单

## 题目链接

- [0844. 比较含退格的字符串 - 力扣](https://leetcode.cn/problems/backspace-string-compare/)

## 题目大意

**描述**：给定 $s$ 和 $t$ 两个字符串。字符串中的 `#` 代表退格字符。

**要求**：当它们分别被输入到空白的文本编辑器后，判断二者是否相等。如果相等，返回 $True$；否则，返回 $False$。

**说明**：

- 如果对空文本输入退格字符，文本继续为空。
- $1 \le s.length, t.length \le 200$。
- $s$ 和 $t$ 只含有小写字母以及字符 `#`。

**示例**：

- 示例 1：

```python
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
```

- 示例 2：

```python
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
```

## 解题思路

这道题的第一个思路是用栈，第二个思路是使用分离双指针。

### 思路 1：栈

- 定义一个构建方法，用来将含有退格字符串构建为删除退格的字符串。构建方法如下。
  - 使用一个栈存放删除退格的字符串。
  - 遍历字符串，如果遇到的字符不是 `#`，则将其插入到栈中。
  - 如果遇到的字符是 `#`，且当前栈不为空，则将当前栈顶元素弹出。
- 分别使用构建方法处理字符串 $s$ 和 $t$，如果处理完的字符串 $s$ 和 $t$ 相等，则返回 $True$，否则返回 $False$。

### 思路 1：代码

```python
class Solution:
    def build(self, s: str):
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return stack
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 和 $m$ 分别为字符串 $s$、$t$ 的长度。
- **空间复杂度**：$O(n + m)$。

### 思路 2：分离双指针

由于 `#` 会消除左侧字符，而不会影响右侧字符，所以我们选择从字符串尾端遍历 $s$、$t$ 字符串。具体做法如下：

- 使用分离双指针 $left\_1$、$left\_2$。$left\_1$ 指向字符串 $s$ 末尾，$left\_2$ 指向字符串 $t$ 末尾。使用 $sign\_1$、$sign\_2$ 标记字符串 $s$、$t$ 中当前退格字符个数。
- 从后到前遍历字符串 $s$、$t$。
  - 先来循环处理字符串 $s$ 尾端 `#` 的影响，具体如下：
    - 如果当前字符是 `#`，则更新 $s$ 当前退格字符个数，即 `sign_1 += 1`。同时将 $left\_1$ 左移。 
    - 如果 $s$ 当前退格字符个数大于 $0$，则退格数减一，即 `sign_1 -= 1`。同时将 $left\_1$ 左移。 
    - 如果 $s$ 当前为普通字符，则跳出循环。
  - 同理再来处理字符串 $t$ 尾端 `#` 的影响，具体如下：
    - 如果当前字符是 `#`，则更新 $t$ 当前退格字符个数，即 `sign_2 += 1`。同时将 $left\_2$ 左移。 
    - 如果 $t$ 当前退格字符个数大于 $0$，则退格数减一，即 `sign_2 -= 1`。同时将 $left\_2$ 左移。 
    - 如果 $t$ 当前为普通字符，则跳出循环。
  - 处理完，如果两个字符串为空，则说明匹配，直接返回 $True$。
  - 再先排除长度不匹配的情况，直接返回 $False$。
  - 最后判断 $s[left\_1]$ 是否等于 $s[left\_2]$。不等于则直接返回 $False$，等于则令 $left\_1$、$left\_2$ 左移，继续遍历。
- 遍历完没有出现不匹配的情况，则返回 $True$。

### 思路 2：代码

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        left_1, left_2 = len(s) - 1, len(t) - 1
        sign_1, sign_2 = 0, 0
        while left_1 >= 0 or left_2 >= 0:
            while left_1 >= 0:
                if s[left_1] == '#':
                    sign_1 += 1
                    left_1 -= 1
                elif sign_1 > 0:
                    sign_1 -= 1
                    left_1 -= 1
                else:
                    break

            while left_2 >= 0:
                if t[left_2] == '#':
                    sign_2 += 1
                    left_2 -= 1
                elif sign_2 > 0:
                    sign_2 -= 1
                    left_2 -= 1
                else:
                    break

            if left_1 < 0 and left_2 < 0:
                return True
            if left_1 >= 0 and left_2 < 0:
                return False
            if left_1 < 0 and left_2 >= 0:
                return False
            if s[left_1] != t[left_2]:
                return False

            left_1 -= 1
            left_2 -= 1

        return True
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 和 $m$ 分别为字符串 $s$、$t$ 的长度。
- **空间复杂度**：$O(1)$。

