# [1390. 四因数](https://leetcode.cn/problems/four-divisors/)

- 标签：数组、数学
- 难度：中等

## 题目链接

- [1390. 四因数 - 力扣](https://leetcode.cn/problems/four-divisors/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：返回所有恰好有四个因数的数字的因数之和。因数包括 $1$ 和该数字本身。

**示例**：

- 示例 1：

```python
输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。
```

- 示例 2：

```python
输入: nums = [21,21]
输出: 64
```


## 解题思路

### 思路 1：枚举因数

#### 1. 核心思想

对每个 $num$，枚举 $1$ 到 $\sqrt{num}$ 的因数。如果因数个数恰好为 $4$，累加因数之和。

#### 2. 具体步骤

**第 1 步**：遍历 $nums$，对每个 $num$：
- 枚举 $i$ 从 $1$ 到 $\sqrt{num}$。
- 如果 $num \% i == 0$，记录因数 $i$ 和 $num // i$。
- 如果因数个数 $> 4$，提前结束。

**第 2 步**：如果因数个数恰好为 $4$，累加。

### 思路 1：代码

```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            divisors = set()
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ans += sum(divisors)
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \sqrt{M})$，$M$ 是最大数字。
- **空间复杂度**：$O(1)$。
