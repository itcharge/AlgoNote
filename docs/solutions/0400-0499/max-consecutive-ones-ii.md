# [0487. 最大连续1的个数 II](https://leetcode.cn/problems/max-consecutive-ones-ii/)

- 标签：数组、动态规划、滑动窗口
- 难度：中等

## 题目链接

- [0487. 最大连续1的个数 II - 力扣](https://leetcode.cn/problems/max-consecutive-ones-ii/)

## 题目大意

**描述**：给定一个二进制数组 $nums$，可以最多将 $1$ 个 $0$ 翻转为 $1$。

**要求**：如果最多可以翻转一个 $0$，则返回数组中连续 $1$ 的最大个数。

**说明**：

- 1 <= nums.length <= 105
  nums[i] 不是 0 就是 1.

**示例**：

- 示例 1：

```python
输入：nums = [1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。当翻转以后，最大连续 1 的个数为 4。
```

- 示例 2：

```python
输入：nums = [1,0,1,1,0,1]
输出：4
```

## 解题思路

### 思路 1：滑动窗口

暴力解法是遍历数组，将每一个 $0$ 依次翻转为 $1$，并统计此时连续 $1$ 的最大个数，最终取最大值。但这种做法的时间复杂度较高，不够高效。

我们可以采用滑动窗口的方法来优化。核心思想是维护一个窗口，使得窗口内最多只包含 $1$ 个 $0$。具体步骤如下：

设定两个指针 $left$ 和 $right$，分别表示滑动窗口的左右边界。用 $zero\_count$ 统计当前窗口内 $0$ 的数量，用 $ans$ 记录最大连续 $1$ 的个数。

- 初始时，$left$ 和 $right$ 都指向数组起始位置 $0$。
- 每次将 $right$ 向右移动一位，如果 $nums[right] == 0$，则 $zero\_count$ 加 $1$。
- 当窗口内 $0$ 的数量超过 $1$（即 $zero\_count > 1$）时，不断右移 $left$，并在遇到 $0$ 时将 $zero\_count$ 减 $1$，直到窗口内至多只有 $1$ 个 $0$。
- 每次更新 $ans$，取当前窗口长度 $right - left + 1$ 的最大值。
- 重复上述过程，直到 $right$ 遍历完整个数组。
- 最终返回 $ans$ 即为所求最大连续 $1$ 的个数。

### 思路 1：代码

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        ans = 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(1)$。

