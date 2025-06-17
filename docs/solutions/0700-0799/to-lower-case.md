# [0709. 转换成小写字母](https://leetcode.cn/problems/to-lower-case/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0709. 转换成小写字母 - 力扣](https://leetcode.cn/problems/to-lower-case/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

**说明**：

- $1 \le s.length \le 100$。
- $s$ 由 ASCII 字符集中的可打印字符组成。

**示例**：

- 示例 1：

```python
输入：s = "Hello"
输出："hello"
```

- 示例 2：

```python
输入：s = "LOVELY"
输出："lovely"
```

## 解题思路

### 思路 1：直接模拟

- 大写字母 $A \sim Z$ 的 ASCII 码范围为 $[65, 90]$。
- 小写字母 $a \sim z$ 的 ASCII 码范围为 $[97, 122]$。

将大写字母的 ASCII 码加 $32$，就得到了对应的小写字母，则解决步骤如下：

1. 使用一个字符串变量 $ans$ 存储最终答案字符串。
2. 遍历字符串 $s$，对于当前字符 $ch$：
   1. 如果 $ch$ 的 ASCII 码范围在 $[65, 90]$，则说明 $ch$ 为大写字母。将 $ch$ 的 ASCII 码增加 $32$，再转换为对应的字符，存入字符串 $ans$ 的末尾。
   2. 如果 $ch$ 的 ASCII 码范围不在 $[65, 90]$，则说明 $ch$ 为小写字母。直接将 $ch$ 存入字符串 $ans$ 的末尾。
3. 遍历完字符串 $s$，返回答案字符串 $ans$。

### 思路 1：代码

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ord('A') <= ord(ch) <= ord('Z'):
                ans += chr(ord(ch) + 32)
            else:
                ans += ch
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。一重循环遍历的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$。如果算上答案数组的空间占用，则空间复杂度为 $O(n)$。不算上则空间复杂度为 $O(1)$。

### 思路 2：使用 API

Python 语言中自带大写字母转小写字母的 API：`lower()`，用 API 转换完成之后，直接返回新的字符串。

### 思路 2：代码

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。一重循环遍历的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$。如果算上答案数组的空间占用，则空间复杂度为 $O(n)$。不算上则空间复杂度为 $O(1)$。