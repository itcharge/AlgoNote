# [1492. n 的第 k 个因子](https://leetcode.cn/problems/the-kth-factor-of-n/)

- 标签：数学、数论
- 难度：中等

## 题目链接

- [1492. n 的第 k 个因子 - 力扣](https://leetcode.cn/problems/the-kth-factor-of-n/)

## 题目大意

**描述**：给定两个整数 $n$ 和 $k$。

**要求**：按递增顺序返回 $n$ 的第 $k$ 个因子。如果因子不足 $k$ 个，返回 $-1$。

**说明**：
- $1 \le n \le 1000$。
- $1 \le k \le 1000$。

**示例**：

- 示例 1：

```python
输入：n = 12, k = 3
输出：3
解释：因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。
```

- 示例 2：

```python
输入：n = 7, k = 2
输出：7
解释：因子列表包括 [1, 7] ，第 2 个因子是 7 。
```

## 解题思路

### 思路 1：枚举

#### 1. 核心思想

$n \le 1000$，可以直接遍历 $1 \to n$，检查每个数是否是 $n$ 的因子，计数到 $k$ 时返回。

#### 2. 具体步骤

**第 1 步**：遍历 $i = 1 \to n$：
- 如果 $n \% i == 0$，计数 $+1$。
- 如果 $count == k$，返回 $i$。

**第 2 步**：如果遍历结束仍未找到，返回 $-1$。

#### 3. 举例说明

以 $n=12, k=3$ 为例：

$12$ 的因子：$1,2,3,4,6,12$

第 $1$ 个：$1$，第 $2$ 个：$2$，第 $3$ 个：$3$。

返回 $3$。

### 思路 1：代码

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

---

### 思路 2：优化（枚举到 $\sqrt{n}$）

因子成对出现，可以枚举到 $\sqrt{n}$，收集所有因子排序后取第 $k$ 个。

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        factors.sort()
        return factors[k - 1] if k <= len(factors) else -1
```

$O(\sqrt{n})$ 时间，在 $n=10^4$ 或更大时更高效。
