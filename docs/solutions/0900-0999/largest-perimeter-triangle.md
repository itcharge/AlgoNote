# [0976. 三角形的最大周长](https://leetcode.cn/problems/largest-perimeter-triangle/)

- 标签：贪心、数组、数学、排序
- 难度：简单

## 题目链接

- [0976. 三角形的最大周长 - 力扣](https://leetcode.cn/problems/largest-perimeter-triangle/)

## 题目大意

**描述**：给定一些由正数（代表长度）组成的数组 `nums`。

**要求**：返回由其中 `3` 个长度组成的、面积不为 `0` 的三角形的最大周长。如果不能形成任何面积不为 `0` 的三角形，则返回 `0`。

**说明**：

- $3 \le nums.length \le 10^4$。
- $1 \le nums[i] \le 10^6$。

**示例**：

- 示例 1：

```python
输入：nums = [2,1,2]
输出：5
解释：长度为 2, 1, 2 的边组成的三角形周长为 5，为最大周长
```

## 解题思路

### 思路 1：

要想三角形的周长最大，则每一条边都要尽可能的长，并且还要满足三角形的边长条件，即 `a + b > c`，其中 `a`、`b`、`c` 分别是三角形的 `3` 条边长。

所以，我们可以先对所有边长进行排序。然后倒序枚举最长边 `nums[i]`，判断前两个边长相加是否大于最长边，即 `nums[i - 2] + nums[i - 1] > nums[i]`。如果满足，则返回 `3` 条边长的和，否则的话继续枚举最长边。

## 代码

### 思路 1 代码：

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0
```

