# [0306. 累加数](https://leetcode.cn/problems/additive-number/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [0306. 累加数 - 力扣](https://leetcode.cn/problems/additive-number/)

## 题目大意

**描述**：

「累加数」是一个字符串，组成它的数字可以形成累加序列。
一个有效的 累加序列 必须「至少」包含 $3$ 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

给定一个只包含数字 $0 \sim 9$ 的字符串。

**要求**：

编写一个算法来判断给定输入是否是「累加数 」。如果是，返回 $true$；否则，返回 $false$。

**说明**：

- 累加序列里的数，除数字 $0$ 之外，不会以 $0$ 开头，所以不会出现 $1, 2, 03$ 或者 $1, 02, 3$ 的情况。
- $1 \le num.length \le 35$。
- $num$ 仅由数字 $0 sim 9$ 组成。

- 进阶：你计划如何处理由过大的整数输入导致的溢出?

**示例**：

- 示例 1：

```python
输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```

- 示例 2：

```python
输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
```

## 解题思路

### 思路 1：回溯算法

累加数问题可以通过回溯算法来解决。我们需要找到字符串中所有可能的数字分割方式，使得分割后的数字序列满足累加数的定义。

**问题分析**：

对于字符串 $num$，我们需要：

- 确定前两个数字 $a$ 和 $b$。
- 验证后续数字是否满足 $c = a + b$ 的关系。
- 递归验证整个序列。

**算法步骤**：

1. **枚举前两个数字**：使用双重循环枚举所有可能的前两个数字 $a$ 和 $b$ 的起始位置。
2. **验证数字有效性**：确保数字不以 $0$ 开头（除非数字本身就是 $0$）。
3. **递归验证序列**：从第三个数字开始，验证每个数字是否等于前两个数字的和。
4. **回溯剪枝**：如果某个分支不满足条件，立即返回 $false$。

###### 3. 关键变量

- $i$：第一个数字的结束位置。
- $j$：第二个数字的结束位置。
- $a$：第一个数字的值。
- $b$：第二个数字的值。
- $sum$：前两个数字的和，用于验证第三个数字。

### 思路 1：代码

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        # 枚举前两个数字的所有可能位置
        for i in range(1, n):
            for j in range(i + 1, n):
                # 获取第一个数字
                first = num[:i]
                # 获取第二个数字
                second = num[i:j]
                
                # 检查数字是否有效（不能以0开头，除非数字本身就是0）
                if (len(first) > 1 and first[0] == '0') or \
                   (len(second) > 1 and second[0] == '0'):
                    continue
                
                # 转换为整数
                a = int(first)
                b = int(second)
                
                # 递归验证剩余部分
                if self._isValid(num, j, a, b):
                    return True
        
        return False
    
    def _isValid(self, num: str, start: int, a: int, b: int) -> bool:
        # 递归验证从 start 位置开始的字符串是否满足累加数条件

        # 如果已经到达字符串末尾，说明验证成功
        if start == len(num):
            return True
        
        # 计算下一个数字的期望值
        expected_sum = a + b
        expected_str = str(expected_sum)
        
        # 检查剩余字符串是否以期望的数字开头
        if num[start:].startswith(expected_str):
            # 递归验证下一个数字
            return self._isValid(num, start + len(expected_str), b, expected_sum)
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 是字符串长度。外层双重循环枚举前两个数字的位置需要 $O(n^2)$ 时间，内层递归验证需要 $O(n)$ 时间，因此总时间复杂度为 $O(n^3)$。
- **空间复杂度**：$O(n)$，递归调用栈的深度最多为 $O(n)$。
