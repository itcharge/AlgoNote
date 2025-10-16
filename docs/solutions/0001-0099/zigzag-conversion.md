# [0006. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)

- 标签：字符串
- 难度：中等

## 题目链接

- [0006. Z 字形变换 - 力扣](https://leetcode.cn/problems/zigzag-conversion/)

## 题目大意

**描述**：

给定一个字符串 $s$ 和指定行数 $numRows$。

**要求**：

根据给定的行数 $numRows$，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"` 行数为 $3$ 时，排列如下：

```
P   A   H   N
A P L S I I G
Y   I   R
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

`string convert(string s, int numRows);`

**说明**：

- $1 \le s.length \le 1000$。
- $s$ 由英文字母（小写和大写）、`','` 和 `'.'` 组成。
- $1 \le numRows \le 1000$。

**示例**：

- 示例 1：

```python
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
```

- 示例 2：

```python
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```

## 解题思路

### 思路 1：模拟法

**核心思想**：按照 Z 字形排列的规律，模拟字符的放置过程，然后按行读取结果。

**算法步骤**：

1. **创建行数组**：创建 $numRows$ 个空字符串数组，用于存储每一行的字符。
2. **模拟 Z 字形放置**：
   - 使用变量 $row$ 表示当前行，$direction$ 表示移动方向（向下或向上）。
   - 遍历字符串 $s$ 中的每个字符，将其放入对应的行中。
   - 当到达第 $0$ 行或第 $numRows-1$ 行时，改变移动方向。
3. **按行读取结果**：将所有行的字符串连接起来。

**关键点**：

- 当 $numRows = 1$ 时，直接返回原字符串。
- 使用 $direction$ 变量控制行号的变化：向下时 $row$ 递增，向上时 $row$ 递减。
- 在边界处（第 $0$ 行或第 $numRows-1$ 行）改变移动方向。

### 思路 1：代码

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一行，直接返回原字符串
        if numRows == 1:
            return s
        
        # 创建 numRows 个空字符串，用于存储每一行的字符
        rows = [""] * numRows
        row = 0  # 当前行
        direction = 1  # 移动方向：1 表示向下，-1 表示向上
        
        # 遍历字符串中的每个字符
        for char in s:
            # 将当前字符添加到对应行
            rows[row] += char
            
            # 更新行号
            row += direction
            
            # 如果到达边界，改变移动方向
            if row == 0 or row == numRows - 1:
                direction = -direction
        
        # 将所有行的字符串连接起来
        return "".join(rows)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。需要遍历字符串中的每个字符一次
- **空间复杂度**：$O(n)$，其中 $n$ 是字符串 $s$ 的长度。需要存储所有字符到行数组中
