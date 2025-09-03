# [1300. 转变数组后最接近目标值的数组和](https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/)

- 标签：数组、二分查找、排序
- 难度：中等

## 题目链接

- [1300. 转变数组后最接近目标值的数组和 - 力扣](https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个目标值 $target$。

**要求**：返回一个整数 $value$，使得将数组中所有大于 $value$ 的值变成 $value$ 后，数组的和最接近 $target$（最接近表示两者之差的绝对值最小）。如果有多种使得和最接近 $target$ 的方案，请你返回这些整数中的最小值。

**说明**：

- 答案 $value$ 不一定是 $arr$ 中的数字。
- $1 \le arr.length \le 10^4$。
- $1 \le arr[i], target \le 10^5$。

**示例**：

- 示例 1：

```python
输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
```

- 示例 2：

```python
输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
```

## 解题思路

### 思路 1：二分查找

题目可以理解为：在 $[0, max(arr)]$ 的区间中，查找一个值 $value$。使得「转变后的数组和」与 $target$ 最接近。

- 转变规则：将数组中大于 $value$ 的值变为 $value$。

在 $[0, max(arr)]$ 的区间中，查找一个值 $value$ 可以使用二分查找答案的方式减少时间复杂度。但是这个最接近 $target$ 应该怎么理解，或者说怎么衡量接近程度。

最接近 $target$ 的肯定是数组和等于 $target$ 的时候。不过更可能是出现数组和恰好比 $target$ 大一点，或数组和恰好比 $target$ 小一点。我们可以将 $target$ 上下两个值相对应的数组和与 $target$ 进行比较，输出差值更小的那一个 $value$。

在根据查找的值 $value$ 计算数组和时，也可以通过二分查找方法查找出数组刚好大于等于 $value$ 元素下标。还可以根据事先处理过的前缀和数组，快速得到转变后的数组和。

最后输出使得数组和与 $target$ 差值更小的 $value$。

整个算法步骤如下：

- 先对数组排序，并计算数组的前缀和 $pre\_sum$。
- 通过二分查找在 $[0, arr[-1]]$ 中查找使得转变后数组和刚好大于等于 $target$ 的值 $value$。
- 计算 $value$ 对应的数组和 $sum\_1$，以及 $value - 1$ 对应的数组和 $sum\_2$。并分别计算与 $target$ 的差值 $diff\_1$、$diff\_2$。
- 输出差值小的那个值。

### 思路 1：代码

```python
class Solution:
    # 计算 value 对应的转变后的数组
    def calc_sum(self, arr, value, pre_sum):
        size = len(arr)
        left, right = 0, size - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid

        return pre_sum[left] + (size - left) * value

    # 查找使得转变后的数组和刚好大于等于 target 的 value
    def binarySearchValue(self, arr, target, pre_sum):
        left, right = 0, arr[-1]
        while left < right:
            mid = left + (right - left) // 2
            if self.calc_sum(arr, mid, pre_sum) < target:
                left = mid + 1
            else:
                right = mid
        return left

    def findBestValue(self, arr: List[int], target: int) -> int:
        size = len(arr)
        arr.sort()
        pre_sum = [0 for _ in range(size + 1)]

        for i in range(size):
            pre_sum[i + 1] = pre_sum[i] + arr[i]

        value = self.binarySearchValue(arr, target, pre_sum)

        sum_1 = self.calc_sum(arr, value, pre_sum)
        sum_2 = self.calc_sum(arr, value - 1, pre_sum)
        diff_1 = abs(sum_1 - target)
        diff_2 = abs(sum_2 - target)

        return value if diff_1 < diff_2 else value - 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((n + k) \times \log n)$。其中 $n$ 是数组 $arr$ 的长度，$k$ 是数组 $arr$ 中的最大值。
- **空间复杂度**：$O(n)$。

