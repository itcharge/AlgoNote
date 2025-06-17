# [0394. 字符串解码](https://leetcode.cn/problems/decode-string/)

- 标签：栈、递归、字符串
- 难度：中等

## 题目链接

- [0394. 字符串解码 - 力扣](https://leetcode.cn/problems/decode-string/)

## 题目大意

**描述**：给定一个经过编码的字符串 `s`。

**要求**：返回 `s` 经过解码之后的字符串。

**说明**：

- 编码规则：`k[encoded_string]`。`encoded_string` 为字符串，`k` 为整数。表示字符串 `encoded_string` 重复 `k` 次。
- $1 \le s.length \le 30$。
- `s` 由小写英文字母、数字和方括号 `[]` 组成。
- `s` 保证是一个有效的输入。
- `s` 中所有整数的取值范围为 $[1, 300]$。

**示例**：

- 示例 1：

```python
输入：s = "3[a]2[bc]"
输出："aaabcbc"
```

- 示例 2：

```python
输入：s = "3[a2[c]]"
输出："accaccacc"
```

## 解题思路

### 思路 1：栈

1. 使用两个栈 `stack1`、`stack2`。`stack1` 用来保存左括号前已经解码的字符串，`stack2` 用来存储左括号前的数字。
2. 用 `res` 存储待解码的字符串、`num` 存储当前数字。
3. 遍历字符串。
   1. 如果遇到数字，则累加数字到 `num`。
   2. 如果遇到左括号，将当前待解码字符串入栈 `stack1`，当前数字入栈 `stack2`，然后将 `res`、`nums` 清空。
   3. 如果遇到右括号，则从 `stack1` 的取出待解码字符串 `res`，从 `stack2` 中取出当前数字 `num`，将其解码拼合成字符串赋值给 `res`。
   4. 如果遇到其他情况（遇到字母），则将当前字母加入 `res` 中。
4. 遍历完输出解码之后的字符串 `res`。

### 思路 1：代码

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack1.append(res)
                stack2.append(num)
                res = ""
                num = 0
            elif ch == ']':
                cur_res = stack1.pop()
                cur_num = stack2.pop()
                res = cur_res + res * cur_num
            else:
                res += ch
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

