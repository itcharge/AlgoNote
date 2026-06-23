# [1470. 重新排列数组](https://leetcode.cn/problems/shuffle-the-array/)

- 标签：数组
- 难度：简单

## 题目链接

- [1470. 重新排列数组 - 力扣](https://leetcode.cn/problems/shuffle-the-array/)

## 题目大意

**描述**：给定一个长度为 $2n$ 的数组 $nums$，按 $[x_1, x_2, \dots, x_n, y_1, y_2, \dots, y_n]$ 的顺序排列。

**要求**：返回 $[x_1, y_1, x_2, y_2, \dots, x_n, y_n]$ 格式的数组。

**说明**：
- $1 \le n \le 500$。
- $nums.length = 2n$。

**示例**：

- 示例 1：

```python
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
```

- 示例 2：

```python
输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
```

## 解题思路

### 思路 1：一次遍历

#### 1. 核心思想

前 $n$ 个是 $x$ 部分，后 $n$ 个是 $y$ 部分。遍历 $i = 0 \to n-1$，依次取 $nums[i]$ 和 $nums[n+i]$。

#### 2. 具体步骤

**第 1 步**：初始化结果数组。

**第 2 步**：遍历 $i = 0 \to n-1$：$ans.append(nums[i])$，$ans.append(nums[n+i])$。

**第 3 步**：返回 $ans$。

#### 3. 举例说明

以 $nums = [2,5,1,3,4,7], n = 3$ 为例：

- $i=0$：取 $nums[0]=2, nums[3]=3$ → $[2,3]$
- $i=1$：取 $nums[1]=5, nums[4]=4$ → $[2,3,5,4]$
- $i=2$：取 $nums[2]=1, nums[5]=7$ → $[2,3,5,4,1,7]$

### 思路 1：代码

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$（不包含返回值）。
