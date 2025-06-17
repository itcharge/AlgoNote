# [0977. 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/)

- 标签：数组、双指针、排序
- 难度：简单

## 题目链接

- [0977. 有序数组的平方 - 力扣](https://leetcode.cn/problems/squares-of-a-sorted-array/)

## 题目大意

**描述**：给定一个按「非递减顺序」排序的整数数组 $nums$。

**要求**：返回「每个数字的平方」组成的新数组，要求也按「非递减顺序」排序。

**说明**：

- 要求使用时间复杂度为 $O(n)$ 的算法解决本问题。
- $1 \le nums.length \le 10^4$。
- $-10^4 \le nums[i] \le 10^4$。
- $nums$ 已按非递减顺序排序。

**示例**：

- 示例 1：

```python
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```

- 示例 2：

```python
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
```

## 解题思路

### 思路 1：对撞指针

原数组是按「非递减顺序」排序的，可能会存在负数元素。但是无论是否存在负数，数字的平方最大值一定在原数组的两端。题目要求返回的新数组也要按照「非递减顺序」排序。那么，我们可以利用双指针，从两端向中间移动，然后不断将数的平方最大值填入数组。具体做法如下：

- 使用两个指针 $left$、$right$。$left$ 指向数组第一个元素位置，$right$ 指向数组最后一个元素位置。再定义 $index = len(nums) - 1$ 作为答案数组填入顺序的索引值。$res$ 作为答案数组。

- 比较 $nums[left]$ 与 $nums[right]$ 的绝对值大小。大的就是平方最大的的那个数。

  - 如果 $abs(nums[right])$ 更大，则将其填入答案数组对应位置，并令 `right -= 1`。

  - 如果 $abs(nums[left])$ 更大，则将其填入答案数组对应位置，并令 `left += 1`。

  - 令 $index -= 1$。

- 直到 $left == right$，最后将 $nums[left]$ 填入答案数组对应位置。

返回答案数组 $res$。

### 思路 1：代码

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left, right = 0, size - 1
        index = size - 1
        res = [0 for _ in range(size)]

        while left < right:
            if abs(nums[left]) < abs(nums[right]):
                res[index] = nums[right] * nums[right]
                right -= 1
            else:
                res[index] = nums[left] * nums[left]
                left += 1
            index -= 1
        res[index] = nums[left] * nums[left]

        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 中的元素数量。
- **空间复杂度**：$O(1)$，不考虑最终返回值的空间占用。

### 思路 2：排序算法

可以通过各种排序算法来对平方后的数组进行排序。以快速排序为例，具体步骤如下：

1. 遍历数组，将数组中各个元素变为平方项。
2. 从数组中找到一个基准数。
3. 然后将数组中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧，从而把数组拆分为左右两个部分。
4. 再对左右两个部分分别重复第 2、3 步，直到各个部分只有一个数，则排序结束。

### 思路 2：代码

```python
import random

class Solution:
    def randomPartition(self, arr: [int], low: int, high: int):
        i = random.randint(low, high)
        arr[i], arr[high] = arr[high], arr[i]
        return self.partition(arr, low, high)

    def partition(self, arr: [int], low: int, high: int):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.randomPartition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        return arr

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return self.quickSort(nums, 0, len(nums) - 1)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 为数组 $nums$ 中的元素数量。
- **空间复杂度**：$O(\log n)$。

