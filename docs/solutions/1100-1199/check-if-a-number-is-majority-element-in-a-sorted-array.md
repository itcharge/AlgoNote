# [1150. 检查一个数是否在数组中占绝大多数](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [1150. 检查一个数是否在数组中占绝大多数 - 力扣](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)

## 题目大意

**描述**：给定一个按**非递减顺序**（也就是从小到大）排列的数组 $nums$，和一个目标值 $target$。

**要求**：判断 $target$ 在数组中的出现次数是否**超过**数组长度的一半。如果是返回 `True`，否则返回 `False`。

**说明**：

- $1 \le nums.length \le 10^3$。
- $1 \le nums[i] \le 10^9$。
- $1 \le target \le 10^9$。

**示例**：

- 示例 1：

```python
输入：nums = [2,4,5,5,5,5,5,6,6], target = 5
输出：true
解释：
5 出现了 5 次，数组长度是 9，5 > 9/2，所以 5 占绝大多数。
```

- 示例 2：

```python
输入：nums = [10,100,101,101], target = 101
输出：false
解释：
101 出现了 2 次，数组长度是 4，2 没有超过 4/2，所以不算绝大多数。
```

## 解题思路

### 思路 1：二分查找

因为数组是排好序的，所以相同的数字会连续出现在一起。比如 `[5,5,5,5,5]` 这些 5 就是一个连续的区间。

要判断 $target$ 是不是占绝大多数，只需要知道它在数组里出现了多少次，然后看次数是否超过数组长度的一半。

**怎么快速知道出现次数？**

在排序数组中找一个数字的出现次数，最有效的方法是用二分查找（可以把它想象成「猜大小」—— 每次猜中间，根据结果排除一半区域）：
1. 用二分查找找到 $target$ **第一次出现的位置**（左边界）。
2. 用二分查找找到 $target$ **最后一次出现的位置**（右边界）。
3. 出现次数 = 右边界 - 左边界 + 1。

Python 内置的 `bisect` 模块提供了现成的二分查找函数：
- `bisect_left(nums, target)`：返回 $target$ 在 $nums$ 中第一次出现的位置。如果 $target$ 不存在，返回它应该插入的位置。
- `bisect_right(nums, target)`：返回 $target$ 在 $nums$ 中最后一次出现的位置 + 1。

**步骤拆解：**

1. 用 `bisect_left` 找 $target$ 的左边界。如果发现 $target$ 根本不在数组中，直接返回 `False`。
2. 用 `bisect_right` 找右边界，减 1 得到最后一次出现的位置。
3. 计算出现次数 = 右边界 - 左边界 + 1。
4. 判断是否超过数组长度的一半。

**为什么不用遍历一遍数一数？**
因为数组可能很长，遍历一次虽然也能解决，但二分查找更快 —— 它每次排除一半的数据，时间复杂度只有 $O(\log n)$。

### 思路 1：代码

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        import bisect
        
        n = len(nums)
        
        # 用二分查找找到 target 第一次出现的位置
        left_idx = bisect.bisect_left(nums, target)
        
        # 如果 target 不在数组中（左边界超出了数组范围，或者该位置的数不是 target）
        if left_idx == n or nums[left_idx] != target:
            return False
        
        # 用二分查找找到 target 最后一次出现的位置
        # bisect_right 返回的是插入点（最后一个 target 的下一个位置），所以要减 1
        right_idx = bisect.bisect_right(nums, target) - 1
        
        # target 出现的次数
        count = right_idx - left_idx + 1
        
        # 判断是否超过数组长度的一半
        return count > n // 2
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。用人话说就是：数组越大，二分查找的优势越明显。100 个数据最多查 7 次，1 万个数据最多查 14 次，非常快。
- **空间复杂度**：$O(1)$。只用了几个固定变量。
