# [LCR 128. 库存管理 I](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [LCR 128. 库存管理 I - 力扣](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

## 题目大意

给定一个数组 `numbers`，`numbers` 是有升序数组经过「旋转」得到的。但是旋转次数未知。数组中可能存在重复元素。

要求：找出数组中的最小元素。

- 旋转：将数组整体右移。

## 解题思路

数组经过「旋转」之后，会有两种情况，第一种就是原先的升序序列，另一种是两段升序的序列。

第一种的最小值在最左边。第二种最小值在第二段升序序列的第一个元素。

```
          *
        *
      *
    *
  *
*
```



```
    *
  *
*
          *
        *
      *
```

最直接的办法就是遍历一遍，找到最小值。但是还可以有更好的方法。考虑用二分查找来降低算法的时间复杂度。

创建两个指针 left、right，分别指向数组首尾。让后计算出两个指针中间值 mid。将 mid 与右边界进行比较。

1. 如果 `numbers[mid] > numbers[right]`，则最小值不可能在 `mid` 左侧，一定在 `mid` 右侧，则将 `left` 移动到 `mid + 1` 位置，继续查找右侧区间。
2. 如果 `numbers[mid] < numbers[right]`，则最小值一定在 `mid` 左侧，将 `right` 移动到 `mid` 位置上，继续查找左侧区间。
3. 当 `numbers[mid] == numbers[right]`，无法判断在 `mid` 的哪一侧，可以采用 `right = right - 1` 逐步缩小区域。

## 代码

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right = right - 1
        return numbers[left]
```

