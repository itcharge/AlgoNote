# [1672. 最富有客户的资产总量](https://leetcode.cn/problems/richest-customer-wealth/)

- 标签：数组、矩阵
- 难度：简单

## 题目链接

- [1672. 最富有客户的资产总量 - 力扣](https://leetcode.cn/problems/richest-customer-wealth/)

## 题目大意

**描述**：给定一个 $m \times n$ 的整数网格 $accounts$，其中 $accounts[i][j]$ 是第 $i$ 位客户在第 $j$ 家银行托管的资产数量。

**要求**：返回最富有客户所拥有的资产总量。

**说明**：

- 客户的资产总量：指的是他们在各家银行托管的资产数量之和。
- 最富有客户：资产总量最大的客户。
- $m == accounts.length$。
- $n == accounts[i].length$。
- $1 \le m, n \le 50$。
- $1 \le accounts[i][j] \le 100$。

**示例**：

- 示例 1：

```python
输入：accounts = [[1,2,3],[3,2,1]]
输出：6
解释：
第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
两位客户都是最富有的，资产总量都是 6 ，所以返回 6。
```

- 示例 2：

```python
输入：accounts = [[1,5],[7,3],[3,5]]
输出：10
解释：
第 1 位客户的资产总量 = 6
第 2 位客户的资产总量 = 10 
第 3 位客户的资产总量 = 8
第 2 位客户是最富有的，资产总量是 10，随意返回 10。
```

## 解题思路

### 思路 1：直接模拟

1. 使用变量 $max\_ans$ 存储最富有客户所拥有的资产总量。
2. 遍历所有客户，对于当前客户 $accounts[i]$，统计其拥有的资产总量。
3. 将当前客户的资产总量与 $max\_ans$ 进行比较，如果大于 $max\_ans$，则更新 $max\_ans$ 的值。
4. 遍历完所有客户，最终返回 $max\_ans$ 作为结果。

### 思路 1：代码

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ans = 0
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total += accounts[i][j]
            if total > max_ans:
                max_ans = total
        return max_ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$。其中 $m$ 和 $n$ 分别为二维数组 $accounts$ 的行数和列数。两重循环遍历的时间复杂度为 $O(m * n)$ 。
- **空间复杂度**：$O(1)$。
