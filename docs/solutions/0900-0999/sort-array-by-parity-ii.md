# [0922. 按奇偶排序数组 II](https://leetcode.cn/problems/sort-array-by-parity-ii/)

- 标签：数组、双指针、排序
- 难度：简单

## 题目链接

- [0922. 按奇偶排序数组 II - 力扣](https://leetcode.cn/problems/sort-array-by-parity-ii/)

## 题目大意

**描述**：

给定一个非负整数数组 $nums$，$nums$ 中一半整数是「奇数」，一半整数是「偶数」。

对数组进行排序，以便当 $nums[i]$ 为奇数时，i 也是「奇数」；当 $nums[i]$ 为偶数时， $i$ 也是「偶数」。

**要求**：

你可以返回「任何满足上述条件的数组作为答案」。

**说明**：

- $2 \le nums.length \le 2 * 10^{4}$。
- $nums.length$ 是偶数。
- $nums$ 中一半是偶数。
- $0 \le nums[i] \le 10^{3}$。

- 进阶：可以不使用额外空间解决问题吗？

**示例**：

- 示例 1：

```python
输入：nums = [4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
```

- 示例 2：

```python
输入：nums = [2,3]
输出：[2,3]
```

## 解题思路

### 思路 1：双指针

使用两个指针 $even$ 和 $odd$，分别指向偶数索引和奇数索引。

1. $even$ 指针从 $0$ 开始，每次移动 $2$ 步，寻找偶数索引上的奇数。
2. $odd$ 指针从 $1$ 开始，每次移动 $2$ 步，寻找奇数索引上的偶数。
3. 当 $even$ 指向奇数且 $odd$ 指向偶数时，交换两个元素。
4. 重复上述过程，直到遍历完整个数组。

### 思路 1：代码

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even, odd = 0, 1  # even 指向偶数索引，odd 指向奇数索引
        
        while even < n and odd < n:
            # 偶数索引找到奇数
            while even < n and nums[even] % 2 == 0:
                even += 2
            # 奇数索引找到偶数
            while odd < n and nums[odd] % 2 == 1:
                odd += 2
            # 交换位置不对的元素
            if even < n and odd < n:
                nums[even], nums[odd] = nums[odd], nums[even]
        
        return nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。
- **空间复杂度**：$O(1)$，只使用了常数级别的额外空间。
