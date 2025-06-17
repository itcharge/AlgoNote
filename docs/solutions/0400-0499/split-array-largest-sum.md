# [0410. 分割数组的最大值](https://leetcode.cn/problems/split-array-largest-sum/)

- 标签：贪心、数组、二分查找、动态规划、前缀和
- 难度：困难

## 题目链接

- [0410. 分割数组的最大值 - 力扣](https://leetcode.cn/problems/split-array-largest-sum/)

## 题目大意

**描述**：给定一个非负整数数组 $nums$ 和一个整数 $k$，将数组分成 $m$ 个非空的连续子数组。

**要求**：使 $m$ 个子数组各自和的最大值最小，并求出子数组各自和的最大值。

**说明**：

- $1 \le nums.length \le 1000$。
- $0 \le nums[i] \le 10^6$。
- $1 \le k \le min(50, nums.length)$。

**示例**：

- 示例 1：

```python
输入：nums = [7,2,5,10,8], k = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
```

- 示例 2：

```python
输入：nums = [1,2,3,4,5], k = 2
输出：9
```

## 解题思路

### 思路 1：二分查找算法

先来理解清楚题意。题目的目的是使得 $m$ 个连续子数组各自和的最大值最小。意思是将数组按顺序分成 $m$ 个子数组，然后计算每个子数组的和，然后找出 $m$ 个和中的最大值，要求使这个最大值尽可能小。最后输出这个尽可能小的和最大值。

可以用二分查找来找这个子数组和的最大值，我们用 $ans$ 来表示这个值。$ans$ 最小为数组 $nums$ 所有元素的最大值，最大为数组 $nums$ 所有元素的和。即 $ans$ 范围是 $[max(nums), sum(nums)]$。

所以就确定了二分查找的两个指针位置。$left$ 指向 $max(nums)$，$right$ 指向 $sum(nums)$。然后取中间值 $mid$，计算当子数组和的最大值为 mid 时，所需要分割的子数组最少个数。

- 如果需要分割的子数组最少个数大于 $m$ 个，则说明子数组和的最大值取小了，不满足条件，应该继续调大，将 $left$ 右移，从右区间继续查找。
- 如果需要分割的子数组最少个数小于或等于 $m$ 个，则说明子数组和的最大值满足条件，并且还可以继续调小，将 $right$ 左移，从左区间继续查找，看是否有更小的数组和满足条件。
- 最终，返回符合条件的最小值即可。

### 思路 1：代码

```python
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def get_count(x):
            total = 0
            count = 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num
                else:
                    total += num
            return count

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if get_count(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log (\sum nums))$，其中 $n$ 为数组中的元素个数。
- **空间复杂度**：$O(1)$。

