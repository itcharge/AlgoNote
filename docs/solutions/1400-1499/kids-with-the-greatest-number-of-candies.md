# [1431. 拥有最多糖果的孩子](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/)

- 标签：数组
- 难度：简单

## 题目链接

- [1431. 拥有最多糖果的孩子 - 力扣](https://leetcode.cn/problems/kids-with-the-greatest-number-of-candies/)

## 题目大意

**描述**：给定一个数组 $candies$ 和一个整数 $extraCandies$，其中 $candies[i]$ 表示第 $i$ 个孩子拥有的糖果数。

**要求**：返回一个布尔数组 $result$，$result[i]$ 表示给第 $i$ 个孩子额外 $extraCandies$ 颗糖后，他是否拥有最多的糖果（即是否 $\ge$ 其他所有孩子拥有的最大糖果数）。

**说明**：
- $2 \le candies.length \le 100$。
- $1 \le candies[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true] 
解释：如果你把额外的糖果全部给：
孩子 1，将有 2 + 3 = 5 个糖果，是孩子中最多的。
孩子 2，将有 3 + 3 = 6 个糖果，是孩子中最多的。
孩子 3，将有 5 + 3 = 8 个糖果，是孩子中最多的。
孩子 4，将有 1 + 3 = 4 个糖果，不是孩子中最多的。
孩子 5，将有 3 + 3 = 6 个糖果，是孩子中最多的。
```

- 示例 2：

```python
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false] 
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
```

## 解题思路

### 思路 1：一次遍历

#### 1. 核心思想

先找出所有孩子中糖果数的最大值 $max\_candy$。然后对于每个孩子，检查 $candies[i] + extraCandies \ge max\_candy$。

#### 2. 具体步骤

**第 1 步**：计算 $max\_candy = \max(candies)$。

**第 2 步**：遍历 $candies$，对每个 $candies[i]$，将 $candies[i] + extraCandies \ge max\_candy$ 的结果加入结果列表。

#### 3. 举例说明

以 $candies = [2,3,5,1,3], extraCandies = 3$ 为例：

$max\_candy = 5$

- $2+3=5 \ge 5$ → True
- $3+3=6 \ge 5$ → True
- $5+3=8 \ge 5$ → True
- $1+3=4 < 5$ → False
- $3+3=6 \ge 5$ → True

结果：$[True, True, True, False, True]$。

### 思路 1：代码

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [c + extraCandies >= max_candy for c in candies]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$（不包含返回值）。
