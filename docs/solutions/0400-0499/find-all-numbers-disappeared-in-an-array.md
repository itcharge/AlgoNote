# [0448. 找到所有数组中消失的数字](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [0448. 找到所有数组中消失的数字 - 力扣](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)

## 题目大意

**描述**：

给定一个含 $n$ 个整数的数组 $nums$，其中 $nums[i]$ 在区间 $[1, n]$ 内。

**要求**：

请你找出所有在 $[1, n]$ 范围内但没有出现在 $nums$ 中的数字，并以数组的形式返回结果。

**说明**：

- $n == nums.length$。
- $1 \le n \le 10^{5}$。
- $1 \le nums[i] \le n$。

- 进阶：你能在不使用额外空间且时间复杂度为 $O(n)$ 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

**示例**：

- 示例 1：

```python
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
```

- 示例 2：

```python
输入：nums = [1,1]
输出：[2]
```

## 解题思路

### 思路 1：正负号标记法

由于数组中的所有数字都在范围 $[1, n]$ 内，且数组长度为 $n$，我们可以利用数组本身作为哈希表来标记数字是否出现。

具体思路：
1. 遍历数组 $nums$，对于每个元素 $nums[i]$，计算 $abs(nums[i]) - 1$ 作为索引。
2. 将对应位置 $nums[abs(nums[i]) - 1]$ 的数变为负数，作为标记，表示该数字已经出现过。
3. 再次遍历数组，如果某个位置 $i$ 的数 $nums[i]$ 还是正数，说明 $i + 1$ 这个数字没有出现过，将其加入结果数组。

算法步骤：
- 遍历数组 $nums$，对于每个元素 $nums[i]$：
  - 计算 $abs(nums[i]) - 1$ 作为索引 $index$。
  - 如果 $nums[index] > 0$，将 $nums[index]$ 标记为负数，即 $nums[index] = -nums[index]$。
- 遍历结束后的数组，对于每个位置 $i$：
  - 如果 $nums[i] > 0$，说明 $i + 1$ 没有出现过，将 $i + 1$ 加入结果数组 $res$。
- 返回结果数组 $res$。

### 思路 1：代码

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 使用正负号标记法，标记出现过的数字
        for i in range(len(nums)):
            # 计算索引位置（因为数组中的数字在 [1, n] 范围内）
            index = abs(nums[i]) - 1
            
            # 如果该位置的数大于 0，将其标记为负数
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # 收集结果：所有仍然是正数的位置对应的数字就是消失的数字
        res = []
        for i in range(len(nums)):
            # 如果该位置的数仍然是正数，说明 i + 1 没有出现过
            if nums[i] > 0:
                res.append(i + 1)
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组长度。需要遍历两次数组，每次遍历的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(1)$。除了返回结果数组，只使用了常数额外空间。
