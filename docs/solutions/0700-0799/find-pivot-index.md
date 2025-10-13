# [0724. 寻找数组的中心下标](https://leetcode.cn/problems/find-pivot-index/)

- 标签：数组、前缀和
- 难度：简单

## 题目链接

- [0724. 寻找数组的中心下标 - 力扣](https://leetcode.cn/problems/find-pivot-index/)

## 题目大意

**描述**：给定一个数组 $nums$。

**要求**：找到「左侧元素和」与「右侧元素和相等」的位置，如果找不到，则返回 $-1$。

**说明**：

- $1 \le nums.length \le 10^4$。
- $-1000 \le nums[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11，二者相等。
```

- 示例 2：

```python
输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
```

## 解题思路

### 思路 1：两次遍历

两次遍历，第一次遍历先求出数组全部元素和。第二次遍历找到左侧元素和恰好为全部元素和一半的位置。

### 思路 1：代码

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum * 2 + nums[i] == sum:
                return i
            curr_sum += nums[i]
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。两次遍历的时间复杂度为 $O(2 \times n)$ ，$O(2 \times n) == O(n)$。
- **空间复杂度**：$O(1)$。

