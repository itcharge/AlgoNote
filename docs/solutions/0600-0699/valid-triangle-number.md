# [0611. 有效三角形的个数](https://leetcode.cn/problems/valid-triangle-number/)

- 标签：贪心、数组、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [0611. 有效三角形的个数 - 力扣](https://leetcode.cn/problems/valid-triangle-number/)

## 题目大意

**描述**：给定一个包含非负整数的数组 $nums$，其中 $nums[i]$ 表示第 $i$ 条边的边长。

**要求**：统计数组中可以组成三角形三条边的三元组个数。

**说明**：

- $1 \le nums.length \le 1000$。
- $0 \le nums[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
```

- 示例 2：

```python
输入: nums = [4,2,3,4]
输出: 4
```

## 解题思路

### 思路 1：对撞指针

构成三角形的条件为：任意两边和大于第三边，或者任意两边差小于第三边。只要满足这两个条件之一就可以构成三角形。以任意两边和大于第三边为例，如果用 $a$、$b$、$c$ 来表示的话，应该同时满足 $a + b > c$、$a + c > b$、$b + c > a$。如果我们将三条边升序排序，假设 $a \le b \le c$，则如果满足 $a + b > c$，则 $a + c > b$ 和 $b + c > a$ 一定成立。

所以我们可以先对 $nums$ 进行排序。然后固定最大边 $i$，利用对撞指针 $left$、$right$ 查找较小的两条边。然后判断是否构成三角形并统计三元组个数。

为了避免重复计算和漏解，要严格保证三条边的序号关系为：$left < right < i$。具体做法如下：

- 对数组从小到大排序，使用 $ans$ 记录三元组个数。
- 从 $i = 2$ 开始遍历数组的每一条边，$i$ 作为最大边。
- 使用双指针 $left$、$right$。$left$ 指向 $0$，$right$ 指向 $i - 1$。
  - 如果 $nums[left] + nums[right] \le nums[i]$，说明第一条边太短了，可以增加第一条边长度，所以将 $left$ 右移，即 `left += 1`。
  - 如果 $nums[left] + nums[right] > nums[i]$，说明可以构成三角形，并且第二条边固定为 $right$ 边的话，第一条边可以在 $[left, right - 1]$ 中任意选择。所以三元组个数要加上 $right - left$。即 `ans += (right - left)`。
- 直到 $left == right$ 跳出循环，输出三元组个数 $ans$。

### 思路 1：代码

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        ans = 0

        for i in range(2, size):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += (right - left)
                    right -= 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组中的元素个数。
- **空间复杂度**：$O(\log n)$，排序需要 $\log n$ 的栈空间。

