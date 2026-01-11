# [0465. 最优账单平衡](https://leetcode.cn/problems/optimal-account-balancing/)

- 标签：位运算、数组、动态规划、回溯、状态压缩
- 难度：困难

## 题目链接

- [0465. 最优账单平衡 - 力扣](https://leetcode.cn/problems/optimal-account-balancing/)

## 题目大意

**描述**：

给定一组交易记录 $transactions$，其中 $transactions[i] = [from_i, to_i, amount_i]$ 表示 ID 为 $from_i$ 的人给 ID 为 $to_i$ 的人转账 $amount_i$ 元。

**要求**：

返回清偿所有债务所需的最少交易次数。

**说明**：

- $1 \le transactions.length \le 8$。
- $transactions[i].length = 3$。
- $0 \le from_i, to_i < 12$。
- $from_i \ne to_i$。
- $1 \le amount_i \le 100$。

**示例**：

- 示例 1：

```python
输入：transactions = [[0,1,10],[2,0,5]]
输出：2
解释：
人 0 给人 1 转账 10 元。
人 2 给人 0 转账 5 元。
需要两次交易：
1. 人 0 给人 2 转账 5 元。
2. 人 0 给人 1 转账 5 元。
```

- 示例 2：

```python
输入：transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
输出：1
解释：
人 0 净收支：-10 + 1 + 5 = -4
人 1 净收支：10 - 1 - 5 = 4
人 2 净收支：5 - 5 = 0
只需一次交易：人 0 给人 1 转账 4 元。
```

## 解题思路

### 思路 1：回溯 + 剪枝

给定一组交易记录，需要找到最少的交易次数使所有账户平衡。

**核心思路**：

- 首先计算每个人的净收支（收入 - 支出）。
- 净收支为 0 的人不需要参与后续交易。
- 问题转化为：将所有正数（债权人）和负数（债务人）通过最少的交易次数归零。
- 使用回溯尝试所有可能的交易组合。

**解题步骤**：

1. 计算每个人的净收支，过滤掉为 0 的账户。
2. 使用回溯：
   - 找到第一个非零账户。
   - 尝试与其他相反符号的账户进行交易。
   - 递归处理剩余账户，记录最少交易次数。
3. 剪枝：如果两个账户的净收支相加为 0，可以直接抵消。

### 思路 1：代码

```python
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # 计算每个人的净收支
        balance = defaultdict(int)
        for u, v, amount in transactions:
            balance[u] -= amount
            balance[v] += amount
        
        # 过滤掉净收支为 0 的账户
        debts = [amount for amount in balance.values() if amount != 0]
        n = len(debts)
        
        def dfs(start):
            # 跳过已经平衡的账户
            while start < n and debts[start] == 0:
                start += 1
            
            # 所有账户都已平衡
            if start == n:
                return 0
            
            min_transactions = float('inf')
            
            # 尝试与其他账户交易
            for i in range(start + 1, n):
                # 只与相反符号的账户交易
                if debts[start] * debts[i] < 0:
                    # 进行交易
                    debts[i] += debts[start]
                    # 递归处理剩余账户
                    min_transactions = min(min_transactions, 1 + dfs(start + 1))
                    # 回溯
                    debts[i] -= debts[start]
            
            return min_transactions
        
        return dfs(0)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n!)$，其中 $n$ 是非零账户的数量。最坏情况下需要尝试所有交易组合。
- **空间复杂度**：$O(n)$，递归栈的深度。
