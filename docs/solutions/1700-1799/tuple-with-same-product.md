# [1726. 同积元组](https://leetcode.cn/problems/tuple-with-same-product/)

- 标签：数组、哈希表
- 难度：中等

## 题目链接

- [1726. 同积元组 - 力扣](https://leetcode.cn/problems/tuple-with-same-product/)

## 题目大意

**描述**：给定一个由不同正整数组成的数组 $nums$。

**要求**：返回满足 $a \times b = c \times d$ 的元组 $(a, b, c, d)$ 的数量。其中 $a$、$b$、$c$ 和 $d$ 都是 $nums$ 中的元素，且 $a \ne b \ne c \ne d$。

**说明**：

- $1 \le nums.length \le 1000$。
- $1 \le nums[i] \le 10^4$。
- $nums$ 中的所有元素互不相同。

**示例**：

- 示例 1：

```python
输入：nums = [2,3,4,6]
输出：8
解释：存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
```

- 示例 2：

```python
输入：nums = [1,2,4,5,10]
输出：16
解释：存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
```

## 解题思路

### 思路 1：哈希表 + 数学

1. 二重循环遍历数组 $nums$，使用哈希表 $cnts$ 记录下所有不同 $nums[i] \times nums[j]$ 的结果。
2. 因为满足 $a \times b = c \times d$ 的元组 $(a, b, c, d)$ 可以按照不同顺序进行组和，所以对于 $x$ 个 $nums[i] \times nums[j]$，就有 $C_x^2$ 种组和方法。
3. 遍历哈希表 $cnts$ 中所有值 $value$，将不同组和的方法数累积到答案 $ans$ 中。
4. 遍历完返回答案 $ans$。

### 思路 1：代码

```Python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnts = Counter()
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                product = nums[i] * nums[j]
                cnts[product] += 1
        
        ans = 0
        for key, value in cnts.items():
            ans += value * (value - 1) * 4
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 表示数组 $nums$ 的长度。
- **空间复杂度**：$O(n^2)$。

