# [0540. 有序数组中的单一元素](https://leetcode.cn/problems/single-element-in-a-sorted-array/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [0540. 有序数组中的单一元素 - 力扣](https://leetcode.cn/problems/single-element-in-a-sorted-array/)

## 题目大意

**描述**：

给定一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

**要求**：

找出并返回只出现一次的那个数。

**说明**：

- 设计的解决方案必须满足 $O(\log n)$ 时间复杂度和 $O(1)$ 空间复杂度。
- $1 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
```

- 示例 2：

```python
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
```

## 解题思路

### 思路 1：二分查找

由于数组是有序的，且除了一个元素外，其他元素都出现两次，我们可以使用二分查找。

关键观察：在单一元素之前，所有成对出现的元素中，第一个元素出现在偶数索引，第二个元素出现在奇数索引；在单一元素之后，这个规律会反转。

具体算法：

- 使用二分查找，维护区间 $[left, right]$
- 计算中点 $mid = (left + right) // 2$
- 如果 $mid$ 是偶数，检查 $nums[mid]$ 是否等于 $nums[mid+1]$：
  - 如果相等，说明单一元素在右半部分，$left = mid + 2$
  - 否则，单一元素在左半部分，$right = mid$
- 如果 $mid$ 是奇数，检查 $nums[mid]$ 是否等于 $nums[mid-1]$：
  - 如果相等，说明单一元素在右半部分，$left = mid + 1$
  - 否则，单一元素在左半部分，$right = mid - 1$

### 思路 1：代码

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 如果 mid 是偶数，应该和 mid+1 配对
            # 如果 mid 是奇数，应该和 mid-1 配对
            if mid % 2 == 0:
                # 偶数索引，检查是否和下一个元素相等
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    # 单一元素在右半部分
                    left = mid + 2
                else:
                    # 单一元素在左半部分（包括 mid）
                    right = mid
            else:
                # 奇数索引，检查是否和前一个元素相等
                if nums[mid] == nums[mid - 1]:
                    # 单一元素在右半部分
                    left = mid + 1
                else:
                    # 单一元素在左半部分（包括 mid）
                    right = mid - 1
        
        return nums[left]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$，其中 $n$ 是数组长度，二分查找的时间复杂度。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
