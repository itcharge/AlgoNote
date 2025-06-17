# [1095. 山脉数组中查找目标值](https://leetcode.cn/problems/find-in-mountain-array/)

- 标签：数组、二分查找、交互
- 难度：困难

## 题目链接

- [1095. 山脉数组中查找目标值 - 力扣](https://leetcode.cn/problems/find-in-mountain-array/)

## 题目大意

**描述**：给定一个山脉数组 $mountainArr$。

**要求**：返回能够使得 `mountainArr.get(index)` 等于 $target$ 最小的下标 $index$ 值。如果不存在这样的下标 $index$，就请返回 $-1$。

**说明**：

- 山脉数组：满足以下属性的数组：

  - $len(arr) \ge 3$；
  - 存在 $i$（$0 < i < len(arr) - 1$），使得：
    - $arr[0] < arr[1] < ... arr[i-1] < arr[i]$;
    - $arr[i] > arr[i+1] > ... > arr[len(arr) - 1]$。
- 不能直接访问该山脉数组，必须通过 `MountainArray` 接口来获取数据：

  - `MountainArray.get(index)`：会返回数组中索引为 $k$ 的元素（下标从 $0$ 开始）。

  - `MountainArray.length()`：会返回该数组的长度。
- 对 `MountainArray.get` 发起超过 $100$ 次调用的提交将被视为错误答案。
- $3 \le mountain_arr.length() \le 10000$。
- $0 \le target \le 10^9$。
- $0 \le mountain_arr.get(index) \le 10^9$。

**示例**：

- 示例 1：

```python
输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
```

- 示例 2：

```python
输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
```

## 解题思路

### 思路 1：二分查找

因为题目要求不能对 `MountainArray.get` 发起超过 $100$ 次调用。所以遍历数组进行查找是不可行的。

根据山脉数组的性质，我们可以把山脉数组分为两部分：「前半部分的升序数组」和「后半部分的降序数组」。在有序数组中查找目标值可以使用二分查找来减少查找次数。

而山脉的峰顶元素索引也可以通过二分查找来做。所以这道题我们可以分为三步：

1. 通过二分查找找到山脉数组的峰顶元素索引。
2. 通过二分查找在前半部分的升序数组中查找目标元素。
3. 通过二分查找在后半部分的降序数组中查找目标元素。

最后，通过对查找结果的判断来输出最终答案。

### 思路 1：代码

```python
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearchPeak(self, mountain_arr) -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearchAscending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def binarySearchDescending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        peek_i = self.binarySearchPeak(mountain_arr)

        res_left = self.binarySearchAscending(mountain_arr, 0, peek_i, target)
        res_right = self.binarySearchDescending(mountain_arr, peek_i + 1, size - 1, target)
        
        return res_left if res_left != -1 else res_right
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$。
