# [1417. 重新格式化字符串](https://leetcode.cn/problems/reformat-the-string/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1417. 重新格式化字符串 - 力扣](https://leetcode.cn/problems/reformat-the-string/)

## 题目大意

**描述**：给定一个混合了字母和数字的字符串 $s$。

**要求**：重新格式化字符串，使得任意两个相邻字符类型不同。返回任意一种有效结果。如果无法实现，返回空字符串。

**说明**：
- $1 \le s.length \le 500$。
- $s$ 只有小写字母和数字。

**示例**：

- 示例 1：

```python
输入：s = "a0b1c2"
输出："0a1b2c"
解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。
```

- 示例 2：

```python
输入：s = "leetcode"
输出：""
解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。
```

## 解题思路

### 思路 1：分类 + 间隔插入

#### 1. 核心思想

分别收集字母和数字。如果两者数量差 $> 1$，无法格式化。

将数量多的类型放在偶数位（开头），少的放在奇数位。交替拼接。

#### 2. 具体步骤

**第 1 步**：分离字母和数字到两个列表。

**第 2 步**：如果 $|letters - digits| > 1$，返回空字符串。

**第 3 步**：将多的类型作为第一个，交替拼接。

#### 3. 举例说明

以 $s = "ab123"$ 为例：

字母：$[a,b]$，数字：$[1,2,3]$

$|2-3|=1 \le 1$，可以格式化。数字多，开头放数字。

结果：$"1a2b3"$ 或 $"a1b23"$ 等。

以 $s = "abc1234"$ 为例：

字母：$[a,b,c]$，数字：$[1,2,3,4]$

$|3-4|=1$，可以。结果：$"1a2b3c4"$。

### 思路 1：代码

```python
class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        ans = []
        i, j = 0, 0
        while i < len(first) or j < len(second):
            if i < len(first):
                ans.append(first[i])
                i += 1
            if j < len(second):
                ans.append(second[j])
                j += 1

        return ''.join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
