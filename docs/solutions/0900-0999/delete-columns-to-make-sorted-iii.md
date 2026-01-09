# [0960. 删列造序 III](https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/)

- 标签：数组、字符串、动态规划
- 难度：困难

## 题目链接

- [0960. 删列造序 III - 力扣](https://leetcode.cn/problems/delete-columns-to-make-sorted-iii/)

## 题目大意

**描述**：

给定由 $n$ 个小写字母字符串组成的数组 $strs$，其中每个字符串长度相等。

选取一个删除索引序列，对于 $strs$ 中的每个字符串，删除对应每个索引处的字符。

比如，有 $strs = ["abcdef","uvwxyz"]$，删除索引序列 ${0, 2, 3}$，删除后为 $["bef", "vyz"]$。

假设，我们选择了一组删除索引 $answer$，那么在执行删除操作之后，最终得到的数组的行中的「每个元素」都是按字典序排列的（即 ($strs[0][0] \le strs[0][1] \le ... \le strs[0][strs[0].length - 1]$) 和 ($strs[1][0] \le strs[1][1] \le ... \le strs[1][strs[1].length - 1]$)，依此类推）。

**要求**：

请返回 $answer.length$ 的最小可能值。

**说明**：

- $n == strs.length$。
- $1 \le n \le 10^{3}$。
- $1 \le strs[i].length \le 10^{3}$。
- $strs[i]$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：strs = ["babca","bbazb"]
输出：3
解释：
删除 0、1 和 4 这三列后，最终得到的数组是 strs = ["bc", "az"]。
这两行是分别按字典序排列的（即，strs[0][0] <= strs[0][1] 且 strs[1][0] <= strs[1][1]）。
注意，strs[0] > strs[1] —— 数组 strs 不一定是按字典序排列的。
```

- 示例 2：

```python
输入：strs = ["edcba"]
输出：4
解释：如果删除的列少于 4 列，则剩下的行都不会按字典序排列。
```

## 解题思路

### 思路 1：动态规划 + 最长公共子序列（LCS）

#### 思路

这道题要求删除最少的列，使得删除后每一行都按字典序非严格递增。这等价于保留最多的列，使得保留的列满足条件。

我们可以使用动态规划求解最长递增子序列（LIS）的变体：

- 定义 $dp[j]$ 表示以第 $j$ 列结尾的最长合法列数。
- 对于每一列 $j$，检查它能否接在之前的某一列 $i$ 后面：
  - 如果对于所有行，都有 $strs[row][i] \le strs[row][j]$，则可以接在后面。
  - $dp[j] = \max(dp[j], dp[i] + 1)$
- 最终答案为 $m - \max(dp)$，其中 $m$ 是列数。

#### 代码

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)  # 行数
        m = len(strs[0])  # 列数
        
        # dp[j] 表示以第 j 列结尾的最长合法列数
        dp = [1] * m
        
        # 对于每一列 j
        for j in range(1, m):
            # 检查能否接在之前的某一列 i 后面
            for i in range(j):
                # 检查所有行是否满足 strs[row][i] <= strs[row][j]
                valid = True
                for row in range(n):
                    if strs[row][i] > strs[row][j]:
                        valid = False
                        break
                
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # 最少删除的列数 = 总列数 - 最长合法列数
        return m - max(dp)
```

#### 复杂度分析

- **时间复杂度**：$O(n \times m^2)$，其中 $n$ 是字符串数组的长度，$m$ 是每个字符串的长度。需要枚举所有列对，并检查所有行。
- **空间复杂度**：$O(m)$，需要一个长度为 $m$ 的 $dp$ 数组。
