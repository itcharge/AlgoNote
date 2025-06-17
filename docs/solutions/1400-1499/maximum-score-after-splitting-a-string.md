# [1422. 分割字符串的最大得分](https://leetcode.cn/problems/maximum-score-after-splitting-a-string/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1422. 分割字符串的最大得分 - 力扣](https://leetcode.cn/problems/maximum-score-after-splitting-a-string/)

## 题目大意

**描述**：给定一个由若干 $0$ 和 $1$ 组成的字符串。将字符串分割成两个非空子字符串的得分为：左子字符串中 $0$ 的数量 + 右子字符串中 $1$ 的数量。

**要求**：计算并返回该字符串分割成两个非空子字符串（即左子字符串和右子字符串）所能获得的最大得分。

**说明**：

- $2 \le s.length \le 500$。
- 字符串 $s$ 仅由字符 $0$ 和 $1$ 组成。

**示例**：

- 示例 1：

```python
输入：s = "011101"
输出：5 
解释：
将字符串 s 划分为两个非空子字符串的可行方案有：
左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5 
左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4 
左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3 
左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2 
左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3
```

- 示例 2：

```python
输入：s = "00111"
输出：5
解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5
```

## 解题思路

### 思路 1：前缀和

1. 遍历字符串 $s$，使用前缀和数组来记录每个前缀子字符串中 $1$ 的个数。
2. 再次遍历字符串 $s$，枚举每个分割点，利用前缀和数组计算出当前分割出的左子字符串中 $1$ 的个数与右子字符串中 $0$ 的个数，并计算当前得分，然后更新最大得分。
3. 返回最大得分作为答案。

### 思路 1：代码

```python
class Solution:
    def maxScore(self, s: str) -> int:
        size = len(s)
        one_cnts = [0 for _ in range(size + 1)]

        for i in range(1, size + 1):
            if s[i - 1] == '1':
                one_cnts[i] = one_cnts[i - 1] + 1
            else:
                one_cnts[i] = one_cnts[i - 1]

        ans = 0
        for i in range(1, size):
            left_score = i - one_cnts[i]
            right_score = one_cnts[size] - one_cnts[i]
            ans = max(ans, left_score + right_score)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(n)$。
