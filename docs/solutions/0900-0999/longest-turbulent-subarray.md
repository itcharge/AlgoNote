# [0978. 最长湍流子数组](https://leetcode.cn/problems/longest-turbulent-subarray/)

- 标签：数组、动态规划、滑动窗口
- 难度：中等

## 题目链接

- [0978. 最长湍流子数组 - 力扣](https://leetcode.cn/problems/longest-turbulent-subarray/)

## 题目大意

**描述**：给定一个数组 $arr$。当 $arr$ 的子数组 $arr[i]$，$arr[i + 1]$，$...$， $arr[j]$ 满足下列条件时，我们称其为湍流子数组：

- 如果 $i \le k < j$，当 $k$ 为奇数时， $arr[k] > arr[k + 1]$，且当 $k$ 为偶数时，$arr[k] < arr[k + 1]$；
- 或如果 $i \le k < j$，当 $k$ 为偶数时，$arr[k] > arr[k + 1]$ ，且当 $k$ 为奇数时，$arr[k] < arr[k + 1]$。
- 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

**要求**：返回给定数组 $arr$ 的最大湍流子数组的长度。

**说明**：

- $1 \le arr.length \le 4 \times 10^4$。
- $0 \le arr[i] \le 10^9$。

**示例**：

- 示例 1：

```python
输入：arr = [9,4,2,10,7,8,8,1,9]
输出：5
解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```

- 示例 2：

```python
输入：arr = [4,8,12,16]
输出：2
```

## 解题思路

### 思路 1：快慢指针

湍流子数组实际上像波浪一样，比如 $arr[i - 2] > arr[i - 1] < arr[i] > arr[i + 1] < arr[i + 2]$。所以我们可以使用双指针的做法。具体做法如下：

- 使用两个指针 $left$、$right$。$left$ 指向湍流子数组的左端，$right$ 指向湍流子数组的右端。
- 如果 $arr[right - 1] == arr[right]$，则更新 `left = right`，重新开始计算最长湍流子数组大小。
- 如果 $arr[right - 2] < arr[right - 1] < arr[right]$，此时为递增数组，则 $left$ 从 $right - 1$ 开始重新计算最长湍流子数组大小。
- 如果 $arr[right - 2] > arr[right - 1] > arr[right]$，此时为递减数组，则 $left$ 从 $right - 1$ 开始重新计算最长湍流子数组大小。
- 其他情况（即 $arr[right - 2] < arr[right - 1] > arr[right]$ 或 $arr[right - 2] > arr[right - 1] < arr[right]$）时，不用更新 $left$值。
- 更新最大湍流子数组的长度，并向右移动 $right$。直到 $right \ge len(arr)$ 时，返回答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        ans = 1

        while right < len(arr):
            if arr[right - 1] == arr[right]:
                left = right
            elif right != 1 and arr[right - 2] < arr[right - 1] and arr[right - 1] < arr[right]:
                left = right - 1
            elif right != 1 and arr[right - 2] > arr[right - 1] and arr[right - 1] > arr[right]:
                left = right - 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $arr$ 中的元素数量。
- **空间复杂度**：$O(1)$。

