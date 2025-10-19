# [0254. 因子的组合](https://leetcode.cn/problems/factor-combinations/)

- 标签：回溯
- 难度：中等

## 题目链接

- [0254. 因子的组合 - 力扣](https://leetcode.cn/problems/factor-combinations/)

## 题目大意

**描述**：

整数可以被看作是其因子的乘积。

例如：$8 = 2 \times 2 \times 2 = 2 \times 4$.

**要求**：

实现一个函数，该函数接收一个整数 $n$ 并返回该整数所有的因子组合。

**说明**：

- 可以假定 $n$ 为永远为正数。
- 因子必须大于 $1$ 并且小于 $n$。
- $1 \le n \le 10^{7}$。

**示例**：

- 示例 1：

```python
输入: 1
输出: []
```

- 示例 2：

```python
输入: 12
输出:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
```

## 解题思路

### 思路 1：

用回溯（DFS）枚举所有按非递减顺序排列的因子组合。核心思想：当我们已经选择了若干因子组成序列 \( path \)，且当前剩余待分解的值为 \( n' \)，那么下一步只需要从上一个因子 \( start \) 开始，尝试所有 \( i \in [start, \lfloor\sqrt{n'}\rfloor] \)。一旦 \( i \mid n' \)：

- 记录组合 \( path + [i, \tfrac{n'}{i}] \)（表示当前选择 \( i \) 后，最后一个因子直接取 \( n'/i \)）。
- 继续递归分解 \( n'/i \)，并将 \( i \) 加入路径，即递归状态为 \( (n'/i,\; start=i,\; path+[i]) \)。

通过将搜索上界限制为 \( \lfloor\sqrt{n'}\rfloor \) 并使用 \( start \) 保持非递减顺序，可以避免重复组合，且有效剪枝，防止超时。

### 思路 1：代码

```python
from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # 回溯搜索：在保持非递减顺序的前提下，枚举 n 的因子组合
        results: List[List[int]] = []

        def dfs(remain: int, start: int, path: List[int]) -> None:
            # 只需要尝试到 sqrt(remain)，其余因子由成对的大因子补齐
            i = start
            # 使用整数平方根作为上界，减少无效枚举
            upper = int(remain ** 0.5)
            while i <= upper:
                if remain % i == 0:
                    # 形成一组合法解：path + [i, remain // i]
                    results.append(path + [i, remain // i])
                    # 继续分解 remain // i，保证非递减（起点仍为 i）
                    dfs(remain // i, i, path + [i])
                i += 1

        # 按题意，因子需严格在 (1, n) 内，n <= 3 时无解
        if n <= 3:
            return results

        dfs(n, 2, [])
        return results
```

### 思路 1：复杂度分析

- **时间复杂度**：输出敏感（output-sensitive）。搜索过程中，每个状态仅尝试到 \( \sqrt{n'} \) 的因子，并通过 \( start \) 约束为非递减顺序，极大减少重复。总体上与因子分解树的规模相关，上界可视为与 \( n \) 的素因子个数指数相关；平均情况下远小于枚举 \( 2^{\log n} \) 的粗略上界。
- **空间复杂度**：\( O(k) \)，其中 \( k \) 为结果中最长组合的长度（等于 \( n \) 的素因子重数之和），用于递归栈与路径存储；结果集另算。
