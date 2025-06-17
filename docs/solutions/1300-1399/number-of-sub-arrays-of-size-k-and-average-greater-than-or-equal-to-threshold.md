# [1343. 大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

- 标签：数组、滑动窗口
- 难度：中等

## 题目链接

- [1343. 大小为 K 且平均值大于等于阈值的子数组数目 - 力扣](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和两个整数 $k$ 和 $threshold$。

**要求**：返回长度为 $k$ 且平均值大于等于 $threshold$ 的子数组数目。

**说明**：

- $1 \le arr.length \le 10^5$。
- $1 \le arr[i] \le 10^4$。
- $1 \le k \le arr.length$。
- $0 \le threshold \le 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
```

- 示例 2：

```python
输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
```

## 解题思路

### 思路 1：滑动窗口（固定长度）

这道题目是典型的固定窗口大小的滑动窗口题目。窗口大小为 `k`。具体做法如下：

1. `ans` 用来维护答案数目。`window_sum` 用来维护窗口中元素的和。
2. `left` 、`right` 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
3. 向右移动 `right`，先将 `k` 个元素填入窗口中。
4. 当窗口元素个数为 `k` 时，即：`right - left + 1 >= k` 时，判断窗口内的元素和平均值是否大于等于阈值 `threshold`。
   1. 如果满足，则答案数目 + 1。
   2. 然后向右移动 `left`，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 `k`。
5. 重复 3 ~ 4 步，直到 `right` 到达数组末尾。
6. 最后输出答案数目。

### 思路 1：代码

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        window_sum = 0
        ans = 0

        while right < len(arr):
            window_sum += arr[right]
            
            if right - left + 1 >= k:
                if window_sum >= k * threshold:
                    ans += 1
                window_sum -= arr[left]
                left += 1

            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

