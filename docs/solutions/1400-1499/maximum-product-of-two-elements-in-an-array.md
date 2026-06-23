# [1464. 数组中两元素的最大乘积](https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [1464. 数组中两元素的最大乘积 - 力扣](https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/)

## 题目大意

**描述**：给定一个整数数组 $nums$，选择两个不同下标 $i$ 和 $j$。

**要求**：返回 $(nums[i] - 1) \times (nums[j] - 1)$ 的最大值。

**说明**：
- $2 \le nums.length \le 500$。
- $1 \le nums[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums = [3,4,5,2]
输出：12 
解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。
```

- 示例 2：

```python
输入：nums = [1,5,4,5]
输出：16
解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
```

## 解题思路

### 思路 1：排序或找最大两个

#### 1. 核心思想

$(nums[i] - 1) \times (nums[j] - 1)$ 最大，需要 $nums[i]$ 和 $nums[j]$ 尽可能大。因此找数组中的最大两个值和即可。

#### 2. 具体步骤

**第 1 步**：对 $nums$ 降序排序。

**第 2 步**：取前两个元素，返回 $(nums[0] - 1) \times (nums[1] - 1)$。

#### 3. 举例说明

以 $nums = [3,4,5,2]$ 为例：

排序：$[5,4,3,2]$，取前两个 $5$ 和 $4$。

$(5-1) \times (4-1) = 4 \times 3 = 12$。

### 思路 1：代码

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$。
- **空间复杂度**：$O(1)$。

---

### 思路 2：一次遍历找最大和次大

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
        return (max1 - 1) * (max2 - 1)
```

$O(n)$ 时间，$O(1)$ 空间。
