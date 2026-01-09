# [0952. 按公因数计算最大组件大小](https://leetcode.cn/problems/largest-component-size-by-common-factor/)

- 标签：并查集、数组、哈希表、数学、数论
- 难度：困难

## 题目链接

- [0952. 按公因数计算最大组件大小 - 力扣](https://leetcode.cn/problems/largest-component-size-by-common-factor/)

## 题目大意

**描述**：

给定一个由不同正整数的组成的非空数组 $nums$，考虑下面的图：

- 有 $nums.length$ 个节点，按从 $nums[0]$ 到 $nums[nums.length - 1]$ 标记；
- 只有当 $nums[i]$ 和 $nums[j]$ 共用一个大于 1 的公因数时，$nums[i]$ 和 $nums[j]$ 之间才有一条边。

**要求**：

返回「图中最大连通组件的大小」。

**说明**：

- $1 \le nums.length \le 2 * 10^{4}$。
- $1 \le nums[i] \le 10^{5}$。
- $nums$ 中所有值都不同。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2018/12/01/ex1.png)

```python
输入：nums = [4,6,15,35]
输出：4
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2018/12/01/ex2.png)

```python
输入：nums = [20,50,9,63]
输出：2
```

## 解题思路

### 思路 1：并查集

#### 思路

这道题要求找到图中最大连通组件的大小，其中两个数如果有大于 $1$ 的公因数，则它们之间有边。

直接判断两两之间的公因数会超时。我们可以通过 **质因数分解** 来优化：
- 如果两个数有公因数 $p$，那么它们都能被 $p$ 整除。
- 我们可以将每个数分解为质因数，然后将所有包含相同质因数的数连接起来。

使用并查集：

1. 对每个数进行质因数分解。
2. 将每个数与其所有质因数连接（使用并查集的 $union$ 操作）。
3. 统计每个连通分量的大小，返回最大值。

为了避免直接连接数字和质因数（范围不同），我们可以用一个哈希表记录每个质因数第一次出现时对应的数字，后续出现相同质因数的数字都与这个数字连接。

#### 代码

```python
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # 并查集
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # 质因数分解
        def get_prime_factors(n):
            factors = []
            # 处理因子 2
            if n % 2 == 0:
                factors.append(2)
                while n % 2 == 0:
                    n //= 2
            # 处理奇数因子
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors.append(i)
                    while n % i == 0:
                        n //= i
                i += 2
            # 如果 n 是质数
            if n > 2:
                factors.append(n)
            return factors
        
        # prime_to_num[p] 记录质因数 p 第一次出现时对应的数字
        prime_to_num = {}
        
        # 对每个数进行质因数分解，并连接
        for num in nums:
            primes = get_prime_factors(num)
            for prime in primes:
                if prime in prime_to_num:
                    union(num, prime_to_num[prime])
                else:
                    prime_to_num[prime] = num
        
        # 统计每个连通分量的大小
        from collections import Counter
        count = Counter(find(num) for num in nums)
        return max(count.values())
```

#### 复杂度分析

- **时间复杂度**：$O(n \sqrt{m})$，其中 $n$ 是数组长度，$m$ 是数组中的最大值。每个数的质因数分解需要 $O(\sqrt{m})$ 时间。
- **空间复杂度**：$O(n + k)$，其中 $k$ 是不同质因数的数量。需要并查集和哈希表存储。
