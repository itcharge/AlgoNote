# [0945. 使数组唯一的最小增量](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/)

- 标签：贪心、数组、计数、排序
- 难度：中等

## 题目链接

- [0945. 使数组唯一的最小增量 - 力扣](https://leetcode.cn/problems/minimum-increment-to-make-array-unique/)

## 题目大意

**描述**：

给定一个整数数组 $nums$。每次 $move$ 操作将会选择任意一个满足 $0 \le i < nums.length$ 的下标 $i$，并将 $nums[i]$ 递增 1。

**要求**：

返回使 $nums$ 中的每个值都变成唯一的所需要的最少操作次数。

**说明**：

- 生成的测试用例保证答案在 32 位整数范围内。
- $1 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
```

- 示例 2：

```python
输入：nums = [3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
```

## 解题思路

### 思路 1：贪心 + 排序

要使数组中的每个值都唯一，我们可以先排序，然后从左到右遍历，确保每个元素都大于前一个元素。

1. **排序**：首先对数组进行排序。
2. **贪心策略**：从左到右遍历，对于每个元素：
   - 如果当前元素小于或等于前一个元素，需要将其增加到 $\text{prev} + 1$
   - 累加操作次数
3. **维护最大值**：使用变量 $\text{need}$ 记录当前位置需要的最小值。

### 思路 1：代码

```python
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        need = 0  # 当前位置需要的最小值
        
        for num in nums:
            # 如果当前数字小于需要的最小值，需要增加
            if num < need:
                moves += need - num
                need += 1
            else:
                # 当前数字已经足够大，更新需要的最小值
                need = num + 1
        
        return moves
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组长度，主要是排序的时间复杂度。
- **空间复杂度**：$O(\log n)$，排序所需的栈空间。
