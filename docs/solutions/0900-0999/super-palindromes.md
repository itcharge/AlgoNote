# [0906. 超级回文数](https://leetcode.cn/problems/super-palindromes/)

- 标签：数学、字符串、枚举
- 难度：困难

## 题目链接

- [0906. 超级回文数 - 力扣](https://leetcode.cn/problems/super-palindromes/)

## 题目大意

**描述**：

如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为「超级回文数」。

现在，给定两个以字符串形式表示的正整数 $left$ 和 $right$，

**要求**：

统计并返回区间 $[left, right]$ 中的「超级回文数」的数目。

**说明**：

- $1 \le left.length, right.length \le 18$。
- $left$ 和 $right$ 仅由数字（0 - 9）组成。
- $left$ 和 $right$ 不含前导零。
- $left$ 和 $right$ 表示的整数在区间 $[1, 10^{18} - 1]$ 内。
- $left$ 小于等于 $right$。

**示例**：

- 示例 1：

```python
输入：left = "4", right = "1000"
输出：4
解释：4、9、121 和 484 都是超级回文数。
注意 676 不是超级回文数：26 * 26 = 676 ，但是 26 不是回文数。
```

- 示例 2：

```python
输入：left = "1", right = "2"
输出：1
```

## 解题思路

### 思路 1：枚举 + 回文数构造

超级回文数是回文数的平方，且平方后仍是回文数。我们可以枚举所有可能的回文数，然后检查其平方是否也是回文数。

1. 由于 $left$ 和 $right$ 最大为 $10^{18}$，所以回文数最大为 $\sqrt{10^{18}} = 10^9$。
2. 我们可以通过构造前半部分来生成回文数，这样只需要枚举到 $10^5$ 左右。
3. 对于每个构造的回文数，计算其平方，检查是否在范围内且是回文数。

### 思路 1：代码

```python
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        
        # 判断是否为回文数
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        
        count = 0
        
        # 枚举回文数的前半部分（长度为 1 到 5）
        for length in range(1, 6):
            # 枚举前半部分的所有可能值
            for i in range(10**(length - 1), 10**length):
                s = str(i)
                # 构造奇数长度的回文数
                for root in [int(s + s[-2::-1]), int(s + s[::-1])]:
                    square = root * root
                    # 检查平方是否在范围内且是回文数
                    if L <= square <= R and is_palindrome(square):
                        count += 1
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt[4]{R})$，其中 $R$ 是右边界。需要枚举所有可能的回文数根。
- **空间复杂度**：$O(\log R)$，用于存储字符串。
