# [0905. 按奇偶排序数组](https://leetcode.cn/problems/sort-array-by-parity/)

- 标签：数组、双指针、排序
- 难度：简单

## 题目链接

- [0905. 按奇偶排序数组 - 力扣](https://leetcode.cn/problems/sort-array-by-parity/)

## 题目大意

**描述**：

给定一个整数数组 $nums$，将 $nums$ 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

**要求**：

返回满足此条件的「任一数组」作为答案。

**说明**：

- $1 \le nums.length \le 5000$。
- $0 \le nums[i] \le 5000$。

**示例**：

- 示例 1：

```python
输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
```

- 示例 2：

```python
输入：nums = [0]
输出：[0]
```

## 解题思路

### 思路 1：双指针

使用双指针法，一个指针 $left$ 指向数组开头，一个指针 $right$ 指向数组末尾。

1. 当 $left$ 指向的元素为偶数时，$left$ 右移。
2. 当 $right$ 指向的元素为奇数时，$right$ 左移。
3. 当 $left$ 指向奇数且 $right$ 指向偶数时，交换两个元素。
4. 重复上述过程，直到 $left \ge right$。

### 思路 1：代码

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        # 双指针，左边放偶数，右边放奇数
        while left < right:
            # 左指针找到奇数
            while left < right and nums[left] % 2 == 0:
                left += 1
            # 右指针找到偶数
            while left < right and nums[right] % 2 == 1:
                right -= 1
            # 交换奇数和偶数
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
