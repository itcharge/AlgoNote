# [1498. 满足条件的子序列数目](https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

- 标签：数组、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [1498. 满足条件的子序列数目 - 力扣](https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

## 题目大意

**描述**：给定一个整数数组 $nums$ 和一个整数 $target$。

**要求**：返回 $nums$ 中满足子序列中最大值与最小值之和 $\le target$ 的非空子序列数目。结果对 $10^9 + 7$ 取模。

**说明**：
- $1 \le nums.length \le 10^5$。
- $1 \le nums[i] \le 10^6$。

**示例**：

- 示例 1：

```python
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
```

- 示例 2：

```python
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
```

## 解题思路

### 思路 1：排序 + 双指针

#### 1. 核心思想

子序列的极值只取最大值和最小值，与元素顺序无关。因此可以先排序。

排序后，对于每个左指针 $i$（作为最小值），找到满足 $nums[i] + nums[j] \le target$ 的最大 $j$（作为最大值）。那么 $[i+1, j]$ 之间的元素可以任选加入或不加入子序列（不改变最小值和最大值），方案数为 $2^{j-i}$。

#### 2. 具体步骤

**第 1 步**：排序 $nums$。

**第 2 步**：预处理 $2$ 的幂次 $pow2[i] = 2^i \mod MOD$。

**第 3 步**：双指针 $i=0, j=n-1$。当 $i \le j$：
- 如果 $nums[i] + nums[j] \le target$：$ans = (ans + pow2[j-i]) \mod MOD$，$i++$。
- 否则 $j--$。

**第 4 步**：返回 $ans$。

#### 3. 正确性证明

排序后，固定最小值 $nums[i]$，找到满足条件的最大的 $nums[j]$。在 $[i+1, j]$ 之间的元素（共 $j-i$ 个），每个可以选择加入或不加入子序列，都不会改变最小值（仍然是 $nums[i]$）和最大值（仍然是 $nums[j]$）。因此方案数为 $2^{j-i}$。

双指针遍历不重复不遗漏。

#### 4. 举例说明

以 $nums = [3,5,6,7], target = 9$ 为例：

排序后：$[3,5,6,7]$
$i=0, j=3$：$3+7=10>9$ → $j=2$
$i=0, j=2$：$3+6=9\le9$ → $ans += 2^{2-0}=4$，$i=1$
$i=1, j=2$：$5+6=11>9$ → $j=1$
$i=1, j=1$：$5+5=10>9$ → $j=0$，结束

$ans=4$。

子序列：$[3], [3,5], [3,6], [3,5,6]$。

### 思路 1：代码

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # 预处理 2 的幂次
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans = (ans + pow2[j - i]) % MOD
                i += 1
            else:
                j -= 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序为主。
- **空间复杂度**：$O(n)$，$pow2$ 数组。
