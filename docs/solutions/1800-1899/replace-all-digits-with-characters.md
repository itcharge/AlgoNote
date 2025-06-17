# [1844. 将所有数字用字符替换](https://leetcode.cn/problems/replace-all-digits-with-characters/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1844. 将所有数字用字符替换 - 力扣](https://leetcode.cn/problems/replace-all-digits-with-characters/)

## 题目大意

**描述**：给定一个下标从 $0$ 开始的字符串 $s$。字符串 $s$ 的偶数下标处为小写英文字母，奇数下标处为数字。

定义一个函数 `shift(c, x)`，其中 $c$ 是一个字符且 $x$ 是一个数字，函数返回字母表中 $c$ 后边第 $x$ 个字符。

- 比如，`shift('a', 5) = 'f'`，`shift('x', 0) = 'x'`。

对于每个奇数下标 $i$，我们需要将数字 $s[i]$ 用 `shift(s[i - 1], s[i])` 替换。

**要求**：替换字符串 $s$ 中所有数字以后，将字符串 $s$ 返回。

**说明**：

- 题目保证 `shift(s[i - 1], s[i])` 不会超过 `'z'`。
- $1 \le s.length \le 100$。
- $s$ 只包含小写英文字母和数字。
- 对所有奇数下标处的 $i$，满足 `shift(s[i - 1], s[i]) <= 'z'` 。

**示例**：

- 示例 1：

```python
输入：s = "a1c1e1"
输出："abcdef"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
```

- 示例 2：

```python
输入：s = "a1b2c3d4e"
输出："abbdcfdhe"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
```

## 解题思路

### 思路 1：模拟

1. 先定义一个 `shift(ch, x)` 用于替换 `s[i]`。
2. 将字符串转为字符串列表，定义为 $res$。
3. 以两个字符为一组遍历字符串，对 $res[i]$ 进行修改。
4. 将字符串列表连接起来，作为答案返回。

### 思路 1：代码

```python
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, x):
            return chr(ord(ch) + x) 
        
        res = list(s)
        for i in range(1, len(s), 2):
            res[i] = shift(res[i - 1], int(res[i]))
        
        return "".join(res)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

