# [0396. 旋转函数](https://leetcode.cn/problems/rotate-function/)

- 标签：数组、数学、动态规划
- 难度：中等

## 题目链接

- [0396. 旋转函数 - 力扣](https://leetcode.cn/problems/rotate-function/)

## 题目大意

**描述**：

给定一个长度为 $n$ 的整数数组 $nums$。

假设 $arrk$ 是数组 $nums$ 顺时针旋转 $k$ 个位置后的数组，我们定义 $nums$ 的 旋转函数  $F$ 为：
- $F(k) = 0 \times arrk[0] + 1 \times arrk[1] + ... + (n - 1) \times arrk[n - 1]$

**要求**：

返回 $F(0), F(1), ..., F(n-1)$ 中的最大值。

**说明**：

- 生成的测试用例让答案符合 $32$ 位整数。
- $n == nums.length$。
- $1 \le n \le 10^{5}$。
- $-10^{3} \le nums[i] \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
```

- 示例 2：

```python
输入: nums = [100]
输出: 0
```

## 解题思路

### 思路 1：数学推导

通过观察旋转函数的计算规律，我们可以发现相邻旋转函数值之间存在递推关系。

设数组长度为 $n$，数组元素为 $nums[0], nums[1], ..., nums[n-1]$。

对于旋转函数 $F(k)$：

- $F(0) = 0 \times nums[0] + 1 \times nums[1] + 2 \times nums[2] + ... + (n-1) \times nums[n-1]$
- $F(1) = 0 \times nums[n-1] + 1 \times nums[0] + 2 \times nums[1] + ... + (n-1) \times nums[n-2]$

通过数学推导，我们可以得到递推公式：

$$F(k) = F(k-1) + sum - n \times nums[n-k]$$

其中 $sum$ 是数组所有元素的和。

**算法步骤**：

1. 计算 $F(0)$ 的值和数组元素总和 $sum$。
2. 使用递推公式依次计算 $F(1), F(2), ..., F(n-1)$。
3. 返回所有 $F(k)$ 值中的最大值。

### 思路 1：代码

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        # 计算 F(0) 和数组元素总和
        f0 = 0
        total_sum = 0
        for i in range(n):
            f0 += i * nums[i]
            total_sum += nums[i]
        
        # 初始化最大值为 F(0)
        max_val = f0
        current_f = f0
        
        # 使用递推公式计算 F(1) 到 F(n-1)
        for k in range(1, n):
            # F(k) = F(k-1) + sum - n * nums[n-k]
            current_f = current_f + total_sum - n * nums[n - k]
            max_val = max(max_val, current_f)
        
        return max_val
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。需要遍历数组两次：一次计算 $F(0)$ 和总和，一次使用递推公式计算所有旋转函数值。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
