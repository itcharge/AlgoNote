# [1493. 删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)

- 标签：数组、动态规划、滑动窗口
- 难度：中等

## 题目链接

- [1493. 删掉一个元素以后全为 1 的最长子数组 - 力扣](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/)

## 题目大意

**描述**：给定一个二进制数组 $nums$，需要从数组中删掉一个元素。

**要求**：返回最长的且只包含 $1$ 的非空子数组的长度。如果不存在这样的子数组，请返回 $0$。

**说明**：

- $1 \le nums.length \le 10^5$。
- $nums[i]$ 要么是 $0$ 要么是 $1$。

**示例**：

- 示例 1：

```python
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1。
```

- 示例 2：

```python
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1]。
```

## 解题思路

### 思路 1：滑动窗口

维护一个元素值为 $0$ 的元素数量少于 $1$ 个的滑动窗口。则答案为滑动窗口长度减去窗口内 $0$ 的个数求最大值。具体做法如下：

设定两个指针：$left$、$right$，分别指向滑动窗口的左右边界，保证窗口 $0$ 的个数小于 $1$ 个。使用 $window\_count$ 记录窗口中 $0$ 的个数，使用 $ans$ 记录删除一个元素后，最长的只包含 $1$ 的非空子数组长度。

- 一开始，$left$、$right$ 都指向 $0$。

- 如果最右侧元素等于 $0$，则 `window_count += 1` 。

- 如果 $window\_count > 1$ ，则不断右移 $left$，缩小滑动窗口长度。并更新当前窗口中 $0$ 的个数，直到 $window\_count \le 1$。
- 更新答案值，然后向右移动 $right$，直到 $right \ge len(nums)$ 结束。
- 输出答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        window_count = 0
        ans = 0

        while right < len(nums):
            if nums[right] == 0:
                window_count += 1

            while window_count > 1:
                if nums[left] == 0:
                    window_count -= 1
                left += 1
            ans = max(ans, right - left + 1 - window_count)
            right += 1

        if ans == len(nums):
            return len(nums) - 1
        else:
            return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(1)$。

