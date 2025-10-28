# [0477. 汉明距离总和](https://leetcode.cn/problems/total-hamming-distance/)

- 标签：位运算、数组、数学
- 难度：中等

## 题目链接

- [0477. 汉明距离总和 - 力扣](https://leetcode.cn/problems/total-hamming-distance/)

## 题目大意

**描述**：

两个整数的「汉明距离」指的是这两个数字的二进制数对应位不同的数量。

给你一个整数数组 $nums$。

**要求**：

请你计算并返回 $nums$ 中任意两个数之间「汉明距离的总和」。

**说明**：

- $1 \le nums.length \le 10^{4}$。
- $0 \le nums[i] \le 10^{9}$。
- 给定输入的对应答案符合 32-bit 整数范围。

**示例**：

- 示例 1：

```python
输入：nums = [4,14,2]
输出：6
解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6
```

- 示例 2：

```python
输入：nums = [4,14,4]
输出：4
```

## 解题思路

### 思路 1：按位统计

**核心思想**：对于每一位（bit），统计该位上 $1$ 的个数 $count_1$ 和 $0$ 的个数 $count_0$，则该位对总和的贡献为 $count_1 \times count_0$（即配对 $1$ 和 $0$ 的数量）。

**算法步骤**：

1. 初始化总和 $res = 0$。
2. 遍历 32 位整数中的每一位（从第 $0$ 位到第 $31$ 位）：
   - 统计在当前位 $i$ 上，数组中 $1$ 的个数 $count_1$。
   - 计算 $0$ 的个数 $count_0 = len(nums) - count_1$。
   - 当前位的贡献为 $count_1 \times count_0$，累加到 $res$。
3. 返回总汉明距离 $res$。

**关键点**：将问题转换为按位统计，每一对数字的汉明距离等于它们在每一位上不同的位数的总和。对于每一位，不同位的数量等于该位上 $1$ 的个数乘以 $0$ 的个数。

### 思路 1：代码

```python
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 初始化总汉明距离
        res = 0
        
        # 遍历 32 位整数的每一位
        for i in range(32):
            # 统计当前位上 1 的个数
            count_1 = 0
            for num in nums:
                # 获取当前位的值（0 或 1）
                if (num >> i) & 1:
                    count_1 += 1
            
            # 计算当前位上 0 的个数
            count_0 = len(nums) - count_1
            
            # 当前位的贡献：配对 1 和 0 的数量
            res += count_1 * count_0
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 32)$。其中 $n$ 是数组 $nums$ 的长度。需要遍历 32 位，每一位都需要遍历整个数组统计。
- **空间复杂度**：$O(1)$。只使用常数额外空间。
