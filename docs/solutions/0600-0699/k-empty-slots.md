# [0683. K 个关闭的灯泡](https://leetcode.cn/problems/k-empty-slots/)

- 标签：树状数组、数组、有序集合、滑动窗口
- 难度：困难

## 题目链接

- [0683. K 个关闭的灯泡 - 力扣](https://leetcode.cn/problems/k-empty-slots/)

## 题目大意

**描述**：$n$ 个灯泡排成一行，编号从 $1$ 到 $n$。最初，所有灯泡都关闭。每天只打开一个灯泡，直到 $n$ 天后所有灯泡都打开。

给定一个长度为 $n$ 的灯泡数组 $blubs$，其中 `bulls[i] = x` 意味着在第 $i + 1$ 天，我们会把在位置 $x$ 的灯泡打开，其中 $i$ 从 $0$ 开始，$x$ 从 $1$ 开始。

再给定一个整数 $k$。

**要求**：输出在第几天恰好有两个打开的灯泡，使得它们中间正好有 $k$ 个灯泡且这些灯泡全部是关闭的 。如果不存在这种情况，则返回 $-1$。如果有多天都出现这种情况，请返回最小的天数 。

**说明**：

- $n == bulbs.length$。
- $1 \le n \le 2 \times 10^4$。
- $1 \le bulbs[i] \le n$。
- $bulbs$ 是一个由从 $1$ 到 $n$ 的数字构成的排列。
- $0 \le k \le 2 \times 10^4$。

**示例**：

- 示例 1：

```python
输入：
bulbs = [1,3,2]，k = 1
输出：2
解释：
第一天 bulbs[0] = 1，打开第一个灯泡 [1,0,0]
第二天 bulbs[1] = 3，打开第三个灯泡 [1,0,1]
第三天 bulbs[2] = 2，打开第二个灯泡 [1,1,1]
返回2，因为在第二天，两个打开的灯泡之间恰好有一个关闭的灯泡。
```

- 示例 2：

```python
输入：bulbs = [1,2,3]，k = 1
输出：-1
```

## 解题思路

### 思路 1：滑动窗口

$blubs[i]$ 记录的是第 $i + 1$ 天开灯的位置。我们将其转换一下，使用另一个数组 $days$ 来存储每个灯泡的开灯时间，其中 $days[i]$ 表示第 $i$ 个位置上的灯泡的开灯时间。

- 使用 $ans$ 记录最小满足条件的天数。维护一个窗口 $left$、$right$。其中 `right = left + k + 1`。使得区间 $(left, right)$ 中所有灯泡（总共为 $k$ 个）开灯时间都晚于 $days[left]$ 和 $days[right]$。
- 对于区间 $[left, right]$，$left < i < right$：
  - 如果出现 $days[i] < days[left]$ 或者 $days[i] < days[right]$，说明不符合要求。将 $left$、$right$ 移动到 $[i, i + k + 1]$，继续进行判断。
  - 如果对于 $left < i < right$ 中所有的 $i$，都满足 $days[i] \ge days[left]$ 并且 $days[i] \ge days[right]$，说明此时满足要求。将当前答案与 $days[left]$ 和 $days[right]$ 中的较大值作比较。如果比当前答案更小，则更新答案。同时将窗口向右移动 $k $位。继续检测新的不相交间隔 $[right, right + k + 1]$。
    - 注意：之所以检测新的不相交间隔，是因为如果检测的是相交间隔，原来的 $right$ 位置元素仍在区间中，肯定会出现 $days[right] < days[right_new]$，不满足要求。所以此时相交的区间可以直接跳过，直接检测不相交的间隔。
- 直到 $right \ge len(days)$ 时跳出循环，判断是否有符合要求的答案，并返回答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        size = len(bulbs)
        days = [0 for _ in range(size)]
        for i in range(size):
            days[bulbs[i] - 1] = i + 1

        left, right = 0, k + 1
        ans = float('inf')
        while right < size:
            check_flag = True
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    check_flag = False
                    break
            if check_flag:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right + k + 1

        if ans != float('inf'):
            return ans
        else:
            return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $bulbs$ 的长度。
- **空间复杂度**：$O(n)$。

