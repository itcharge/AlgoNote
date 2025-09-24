## 1. 双串线性 DP 问题简介

> **双串线性 DP 问题**：指输入为两个数组或两个字符串的线性动态规划问题。常见的状态定义为 $dp[i][j]$，其含义主要有以下三种方式：
>
> 1. 以 $nums1[i]$ 结尾的子数组（$nums1[0]$ 到 $nums1[i]$，$1 \leq i \leq n$）与以 $nums2[j]$ 结尾的子数组（$nums2[0]$ 到 $nums2[j]$，$1 \leq j \leq m$）之间的相关解。
> 2. 以 $nums1[i - 1]$ 结尾的子数组（$nums1[0]$ 到 $nums1[i - 1]$，$1 \leq i \leq n$）与以 $nums2[j - 1]$ 结尾的子数组（$nums2[0]$ 到 $nums2[j - 1]$，$1 \leq j \leq m$）之间的相关解。
> 3. 由前 $i$ 个元素组成的 $nums1$ 子数组（$nums1[0]$ 到 $nums1[i - 1]$，$1 \leq i \leq n$）与前 $j$ 个元素组成的 $nums2$ 子数组（$nums2[0]$ 到 $nums2[j - 1]$，$1 \leq j \leq m$）之间的相关解。

这三种状态定义的主要区别在于下标的取值范围，以及是否包含当前元素 $nums1[i]$ 或 $nums2[j]$。

- 第 1 种：子数组长度为 $i + 1$ 或 $j + 1$，不允许为空。
- 第 2、3 种：子数组长度为 $i$ 或 $j$，允许为空（当 $i = 0$ 或 $j = 0$ 时表示空数组），便于初始化和边界处理。

## 2. 双串线性 DP 问题经典题目

### 2.1 经典例题：最长公共子序列

双串线性 DP 问题中最经典的问题就是「最长公共子序列（Longest Common Subsequence，简称 LCS）」。

#### 2.1.1 题目链接

- [1143. 最长公共子序列 - 力扣](https://leetcode.cn/problems/longest-common-subsequence/)

#### 2.1.2 题目大意

**描述**：给定两个字符串 $text1$ 和 $text2$。

**要求**：返回两个字符串的最长公共子序列的长度。如果不存在公共子序列，则返回 $0$。

**说明**：

- **子序列**：原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
- **公共子序列**：两个字符串所共同拥有的子序列。
- $1 \le text1.length, text2.length \le 1000$。
- $text1$ 和 $text2$ 仅由小写英文字符组成。

**示例**：

- 示例 1：

```python
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
```

- 示例 2：

```python
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
```

#### 2.1.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以两个字符串的结尾下标作为阶段。

###### 2. 状态定义

令 $dp[i][j]$ 表示 $text1$ 的前 $i$ 个字符与 $text2$ 的前 $j$ 个字符的最长公共子序列长度。

###### 3. 状态转移方程

遍历 $text1$ 和 $text2$ 的所有前缀，状态转移分为两种情况：

- 如果 $text1[i - 1] == text2[j - 1]$，说明当前字符相同，则最长公共子序列长度在 $dp[i - 1][j - 1]$ 基础上加 $1$，即 $dp[i][j] = dp[i - 1][j - 1] + 1$。
- 如果 $text1[i - 1] \ne text2[j-1]$，则当前字符不同，$dp[i][j]$ 取 $dp[i - 1][j]$ 和 $dp[i][j - 1]$ 的较大值，即 $dp[i][j] = \max(dp[i - 1][j], dp[i][j - 1])$。

###### 4. 初始条件

- $dp[0][j] = 0$，即 $text1$ 为空时，与 $text2$ 任意前缀的最长公共子序列长度为 $0$。
- $dp[i][0] = 0$，即 $text2$ 为空时，与 $text1$ 任意前缀的最长公共子序列长度为 $0$。

###### 5. 结果表示

最终答案为 $dp[size1][size2]$，即 $text1$ 与 $text2$ 的最长公共子序列长度，其中 $size1$、$size2$ 分别为 $text1$、$text2$ 的长度。

##### 思路 1：代码

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[size1][size2]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$、$m$ 分别是字符串 $text1$、$text2$ 的长度。两重循环遍历的时间复杂度是 $O(n \times m)$，所以总的时间复杂度为 $O(n \times m)$。
- **空间复杂度**：$O(n \times m)$。用到了二维数组保存状态，所以总体空间复杂度为 $O(n \times m)$。

### 2.2 经典例题：最长重复子数组
本节介绍与 LCS（最长公共子序列）类似的「最长重复子数组」问题。两者主要区别在于：

- LCS 求最长公共「子序列」，可不连续；
- 最长重复子数组要求最长公共「子数组」，必须连续。

两者的状态定义和转移类似，但最长重复子数组只有当前元素相等时才能从左上角转移，否则状态归零。

#### 2.2.1 题目链接

- [718. 最长重复子数组 - 力扣](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/)

#### 2.2.2 题目大意

**描述**：给定两个整数数组 $nums1$、$nums2$。

**要求**：计算两个数组中公共的、长度最长的子数组长度。

**说明**：

- $1 \le nums1.length, nums2.length \le 1000$。
- $0 \le nums1[i], nums2[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。
```

- 示例 2：

```python
输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5
```

#### 2.2.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以两个数组的结尾位置 $(i, j)$ 作为阶段。

###### 2. 定义状态

设 $dp[i][j]$ 表示以 $nums1$ 的第 $i - 1$ 个元素和 $nums2$ 的第 $j - 1$ 个元素结尾的最长公共子数组长度。

###### 3. 状态转移方程

- 如果 $nums1[i - 1] == nums2[j - 1]$，则当前元素可以作为公共子数组的延续：$dp[i][j] = dp[i - 1][j - 1] + 1$。
- 如果 $nums1[i - 1] \ne nums2[j - 1]$，则无法延续公共子数组：$dp[i][j] = 0$。

###### 4. 初始条件

- $dp[0][j] = 0$，表示 $nums1$ 为空时，公共子数组长度为 0；
- $dp[i][0] = 0$，表示 $nums2$ 为空时，公共子数组长度为 0。

###### 5. 最终结果

- 在遍历过程中，用 $res$ 记录所有 $dp[i][j]$ 的最大值，最终 $res$ 即为所求答案。

##### 思路 1：代码

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]
        res = 0
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > res:
                    res = dp[i][j]

        return res
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$。其中 $n$ 是数组 $nums1$ 的长度，$m$ 是数组 $nums2$ 的长度。
- **空间复杂度**：$O(n \times m)$。

### 2.3 经典例题：编辑距离

双串线性 DP 问题中除了经典的最长公共子序列问题之外，还包括字符串的模糊匹配问题。

#### 2.3.1 题目链接

- [72. 编辑距离 - 力扣](https://leetcode.cn/problems/edit-distance/)

#### 2.3.2 题目大意

**描述**：给定两个单词 $word1$、$word2$。

对一个单词可以进行以下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符

**要求**：计算出将 $word1$ 转换为 $word2$ 所使用的最少操作数。

**说明**：

- $0 \le word1.length, word2.length \le 500$。
- $word1$ 和 $word2$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

- 示例 2：

```python
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

#### 2.3.3 解题思路

##### 思路 1：动态规划

###### 1. 阶段划分

以两个字符串的结尾位置作为阶段进行划分。

###### 2. 定义状态

设 $dp[i][j]$ 表示将 $word1$ 的前 $i$ 个字符（记为 $str1$）转换为 $word2$ 的前 $j$ 个字符（记为 $str2$）所需的最少操作次数。

###### 3. 状态转移方程

- 如果当前字符相同（$word1[i - 1] == word2[j - 1]$），则无需操作：$dp[i][j] = dp[i - 1][j - 1]$。
- 如果当前字符不同（$word1[i - 1] \ne word2[j - 1]$），则有三种操作可选，取最小值：
  1. 替换：$dp[i - 1][j - 1] + 1$
  2. 插入：$dp[i][j - 1] + 1$
  3. 删除：$dp[i - 1][j] + 1$

因此，状态转移方程为：

$$
dp[i][j] = 
\begin{cases}
dp[i - 1][j - 1] & \text{如果 } word1[i - 1] == word2[j - 1] \\ \min
\left(
\begin{array}{l}
dp[i - 1][j - 1], \\
dp[i][j - 1], \\
dp[i - 1][j] \\
\end{array} 
\right) + 1 & \text{否则}
\end{cases}
$$

###### 4. 初始条件

- $dp[0][j] = j$：将空串变为 $word2$ 的前 $j$ 个字符，需要插入 $j$ 次。
- $dp[i][0] = i$：将 $word1$ 的前 $i$ 个字符变为空串，需要删除 $i$ 次。

###### 5. 最终结果

最终答案为 $dp[size1][size2]$，即将 $word1$ 转换为 $word2$ 所需的最少操作次数，其中 $size1$ 和 $size2$ 分别为 $word1$ 和 $word2$ 的长度。

##### 思路 1：代码

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)
        size2 = len(word2)
        dp = [[0 for _ in range(size2 + 1)] for _ in range(size1 + 1)]

        for i in range(size1 + 1):
            dp[i][0] = i
        for j in range(size2 + 1):
            dp[0][j] = j
        for i in range(1, size1 + 1):
            for j in range(1, size2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[size1][size2]
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$、$m$ 分别是字符串 $word1$、$word2$ 的长度。两重循环遍历的时间复杂度是 $O(n \times m)$，所以总的时间复杂度为 $O(n \times m)$。
- **空间复杂度**：$O(n \times m)$。用到了二维数组保存状态，所以总体空间复杂度为 $O(n \times m)$。

## 练习题目

- [1143. 最长公共子序列](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1100-1199/longest-common-subsequence.md)

- [双串线性 DP 问题题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8F%8C%E4%B8%B2%E7%BA%BF%E6%80%A7-dp-%E9%97%AE%E9%A2%98)