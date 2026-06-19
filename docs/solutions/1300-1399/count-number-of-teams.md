# [1395. 统计作战单位数](https://leetcode.cn/problems/count-number-of-teams/)

- 标签：树状数组、数组、动态规划
- 难度：中等

## 题目链接

- [1395. 统计作战单位数 - 力扣](https://leetcode.cn/problems/count-number-of-teams/)

## 题目大意

**描述**：给定一个数组 $rating$，表示每个士兵的评分。需要选出 $3$ 个士兵组成作战单位，要求他们的评分严格递增或严格递减。

**要求**：返回能组成的作战单位数。

**说明**：
- $3 \le rating.length \le 200$。
- $1 \le rating[i] \le 10^5$。

**示例**：

- 示例 1：

```python
输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
```

- 示例 2：

```python
输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。
```


## 解题思路

### 思路 1：枚举中间点

#### 1. 核心思想

枚举中间士兵 $j$。统计左边比 $rating[j]$ 小的个数 $left\_small$、比 $rating[j]$ 大的个数 $left\_big$，以及右边比 $rating[j]$ 大的个数 $right\_big$、比 $rating[j]$ 小的个数 $right\_small$。

递增三元组数 = $left\_small \times right\_big$。
递减三元组数 = $left\_big \times right\_small$。

总数为两者之和。

#### 2. 具体步骤

**第 1 步**：遍历 $j$ 从 $1$ 到 $n-2$。

**第 2 步**：统计左边的比他小和大的数，统计右边的比他小和大的数。

**第 3 步**：累加 $left\_small \times right\_big + left\_big \times right\_small$。

### 思路 1：代码

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for j in range(1, n - 1):
            left_small = left_big = 0
            right_small = right_big = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_small += 1
                elif rating[i] > rating[j]:
                    left_big += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_small += 1
                elif rating[k] > rating[j]:
                    right_big += 1
            ans += left_small * right_big + left_big * right_small
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^2)$，$n \le 200$，完全可行。
- **空间复杂度**：$O(1)$。
