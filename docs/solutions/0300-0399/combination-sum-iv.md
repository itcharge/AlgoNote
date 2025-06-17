# [0377. 组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/)

- 标签：数组、动态规划
- 难度：中等

## 题目链接

- [0377. 组合总和 Ⅳ - 力扣](https://leetcode.cn/problems/combination-sum-iv/)

## 题目大意

**描述**：给定一个由不同整数组成的数组 $nums$ 和一个目标整数 $target$。

**要求**：从 $nums$ 中找出并返回总和为 $target$ 的元素组合个数。

**说明**：

- 题目数据保证答案符合 32 位整数范围。
- $1 \le nums.length \le 200$。
- $1 \le nums[i] \le 1000$。
- $nums$ 中的所有元素互不相同。
- $1 \le target \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
```

- 示例 2：

```python
输入：nums = [9], target = 3
输出：0
```

## 解题思路

### 思路 1：动态规划

「完全背包问题求方案数」的变形。本题与「完全背包问题求方案数」不同点在于：方案中不同的物品顺序代表不同方案。

比如「完全背包问题求方案数」中，凑成总和为 $4$ 的方案 $[1, 3]$  算 $1$ 种方案，但是在本题中 $[1, 3]$、$[3, 1]$ 算 $2$ 种方案数。

我们需要在考虑某一总和 $w$ 时，需要将 $nums$ 中所有元素都考虑到。对应到循环关系时，即将总和 $w$ 的遍历放到外侧循环，将 $nums$ 数组元素的遍历放到内侧循环，即：

```python
for w in range(target + 1):
    for i in range(1, len(nums) + 1):
        xxxx
```

###### 1. 划分阶段

按照总和进行阶段划分。

###### 2. 定义状态

定义状态 $dp[w]$ 表示为：凑成总和 $w$ 的组合数。

###### 3. 状态转移方程

凑成总和为 $w$ 的组合数 = 「不使用当前 $nums[i - 1]$，只使用之前整数凑成和为 $w$ 的组合数」+「使用当前 $nums[i - 1]$ 凑成和为 $w - nums[i - 1]$ 的方案数」。即状态转移方程为：$dp[w] = dp[w] + dp[w - nums[i - 1]]$。

###### 4. 初始条件

- 凑成总和 $0$ 的组合数为 $1$，即 $dp[0] = 1$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[w]$ 表示为：凑成总和 $w$ 的组合数。 所以最终结果为 $dp[target]$。

### 思路 1：代码

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        size = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for w in range(target + 1):
            for i in range(1, size + 1):
                if w >= nums[i - 1]:
                    dp[w] = dp[w] + dp[w - nums[i - 1]]
            
        return dp[target]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times target)$，其中 $n$ 为数组 $nums$ 的元素个数，$target$ 为目标整数。
- **空间复杂度**：$O(target)$。

