# [0422. 有效的单词方块](https://leetcode.cn/problems/valid-word-square/)

- 标签：数组、矩阵
- 难度：简单

## 题目链接

- [0422. 有效的单词方块 - 力扣](https://leetcode.cn/problems/valid-word-square/)

## 题目大意

**描述**：

给定一个单词序列 $words$，判断它是否构成一个有效的单词方块。

有效的单词方块需要满足：第 $i$ 行第 $j$ 列的字符等于第 $j$ 行第 $i$ 列的字符，即 $words[i][j] = words[j][i]$。

**要求**：

如果是有效的单词方块，返回 $true$；否则返回 $false$。

**说明**：

- $1 \le words.length \le 500$。
- $1 \le words[i].length \le 500$。
- $words[i]$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/04/09/validsq1-grid.jpg)

```python
输入: words = ["abcd","bnrt","crmy","dtye"]
输出: true
解释:
第 1 行和第 1 列都读作 "abcd"。
第 2 行和第 2 列都读作 "bnrt"。
第 3 行和第 3 列都读作 "crmy"。
第 4 行和第 4 列都读作 "dtye"。
因此，它构成了一个有效的单词方块。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/04/09/validsq2-grid.jpg)

```python
输入: words = ["abcd","bnrt","crm","dt"]
输出: true
解释:
第 1 行和第 1 列都读作 "abcd"。
第 2 行和第 2 列都读作 "bnrt"。
第 3 行和第 3 列都读作 "crm"。
第 4 行和第 4 列都读作 "dt"。
因此，它构成了一个有效的单词方块。
```

## 解题思路

### 思路 1：矩阵转置验证

有效的单词方块需要满足：第 $i$ 行的第 $j$ 个字符等于第 $j$ 行的第 $i$ 个字符，即 $words[i][j] = words[j][i]$。

**解题步骤**：

1. 遍历每一行 $i$ 和每一列 $j$。
2. 检查 $words[i][j]$ 是否等于 $words[j][i]$。
3. 需要注意边界情况：
   - 行的长度可能不同。
   - 访问 $words[j][i]$ 时，需要确保 $j < len(words)$ 且 $i < len(words[j])$。
   - 访问 $words[i][j]$ 时，需要确保 $i < len(words)$ 且 $j < len(words[i])$。

**关键点**：

- 如果 $words[i]$ 的长度大于 $words$ 的行数，说明存在列索引超出行数，不是有效的单词方块。
- 对称性检查：$words[i][j]$ 必须等于 $words[j][i]$。

### 思路 1：代码

```python
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        
        for i in range(n):
            for j in range(len(words[i])):
                # 检查对称位置是否存在且相等
                # words[i][j] 应该等于 words[j][i]
                
                # 如果 j >= n，说明列索引超出行数
                if j >= n:
                    return False
                
                # 如果 words[j] 的长度不够，或者字符不匹配
                if i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是行数，$m$ 是平均每行的字符数。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
