# [0163. 缺失的区间](https://leetcode.cn/problems/missing-ranges/)

- 标签：数组
- 难度：简单

## 题目链接

- [0163. 缺失的区间 - 力扣](https://leetcode.cn/problems/missing-ranges/)

## 题目大意

**描述**：

给定一个闭区间 $[lower, upper]$ 和一个按从小到大排序的整数数组 $nums$ ，其中元素的范围在闭区间 $[lower, upper]$ 当中。
如果一个数字 $x$ 在 $[lower, upper]$ 区间内，并且 $x$ 不在 $nums$ 中，则认为 $x$ 缺失。

**要求**：

返回「准确涵盖所有缺失数字」的「最小排序」区间列表。也就是说，$nums$ 的任何元素都不在任何区间内，并且每个缺失的数字都在其中一个区间内。

**说明**：

- $-10^{9} \le lower \le upper \le 10^{9}$。
- $0 \le nums.length \le 10^{3}$。
- $lower \le nums[i] \le upper$。
- nums 中的所有值 互不相同。

**示例**：

- 示例 1：

```python
输入: nums = [0, 1, 3, 50, 75], lower = 0 , upper = 99
输出: [[2,2],[4,49],[51,74],[76,99]]
解释：返回的区间是：
[2,2]
[4,49]
[51,74]
[76,99]
```

- 示例 2：

```python
输入： nums = [-1], lower = -1, upper = -1
输出： []
解释： 没有缺失的区间，因为没有缺失的数字。
```

## 解题思路

### 思路 1：线性扫描

我们可以通过线性扫描数组来找到所有缺失的区间。具体思路如下：

1. **初始化边界**：从 $lower$ 开始，到 $upper$ 结束。
2. **遍历数组**：对于数组中的每个元素 $nums[i]$，检查它与前一个边界之间是否有缺失的区间。
3. **添加缺失区间**：
   - 如果 $prev + 1 < nums[i]$，说明 $[prev + 1, nums[i] - 1]$ 是一个缺失区间。
   - 如果 $prev + 1 = nums[i]$，说明没有缺失。
4. **处理最后一个区间**：遍历完数组后，检查 $nums[n-1]$ 到 $upper$ 之间是否有缺失区间。

**关键点**：

- 使用变量 $prev$ 记录前一个已处理的边界。
- 对于单个数字的区间，表示为 $[x, x]$。
- 需要处理数组为空的情况。

### 思路 1：代码

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        prev = lower - 1  # 前一个边界，初始化为 lower - 1
        
        # 遍历数组中的每个元素
        for num in nums:
            # 如果当前数字与前一个边界之间有间隔，添加缺失区间
            if prev + 1 < num:
                result.append([prev + 1, num - 1])
            prev = num  # 更新前一个边界
        
        # 检查最后一个数字到 upper 之间是否有缺失区间
        if prev < upper:
            result.append([prev + 1, upper])
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。我们需要遍历数组一次。
- **空间复杂度**：$O(1)$，除了返回结果外，只使用了常数额外空间。
