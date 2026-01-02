# [0624. 数组列表中的最大距离](https://leetcode.cn/problems/maximum-distance-in-arrays/)

- 标签：贪心、数组
- 难度：中等

## 题目链接

- [0624. 数组列表中的最大距离 - 力扣](https://leetcode.cn/problems/maximum-distance-in-arrays/)

## 题目大意

**描述**：

给定 $m$ 个数组，每个数组都已经按照升序排好序了。

**要求**：

从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 $a$ 和 $b$ 之间的距离定义为它们差的绝对值 $|a-b|$。

返回最大距离。

**说明**：

- $m == arrays.length$。
- $2 \le m \le 10^{5}$。
- $1 \le arrays[i].length \le 500$。
- $-10^{4} \le arrays[i][j] \le 10^{4}$。
- $arrays[i]$ 以升序排序。
- 所有数组中最多有 $10^{5}$ 个整数。

**示例**：

- 示例 1：

```python
输入：[[1,2,3],[4,5],[1,2,3]]
输出：4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
```

- 示例 2：

```python
输入：arrays = [[1],[1]]
输出：0
```

## 解题思路

### 思路 1：贪心

这道题目要求从不同数组中选择两个数，使得它们的距离最大。由于每个数组都是升序排列的，最大距离一定是某个数组的最大值减去另一个数组的最小值。

1. 初始化 $min\_val$ 为第一个数组的最小值，$max\_val$ 为第一个数组的最大值。
2. 初始化结果 $result = 0$。
3. 从第二个数组开始遍历：
   - 计算当前数组的最大值与之前所有数组的最小值的差值。
   - 计算之前所有数组的最大值与当前数组的最小值的差值。
   - 更新结果为这两个差值的最大值。
   - 更新 $min\_val$ 和 $max\_val$。
4. 返回结果。

### 思路 1：代码

```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 初始化为第一个数组的最小值和最大值
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        
        # 从第二个数组开始遍历
        for i in range(1, len(arrays)):
            # 当前数组的最小值和最大值
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            # 计算当前数组与之前数组的最大距离
            result = max(result, abs(curr_max - min_val), abs(max_val - curr_min))
            
            # 更新全局最小值和最大值
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m)$，其中 $m$ 是数组的个数。只需要遍历所有数组一次。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
