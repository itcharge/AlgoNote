# [1151. 最少交换次数来组合所有的 1](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/)

- 标签：数组、滑动窗口
- 难度：中等

## 题目链接

- [1151. 最少交换次数来组合所有的 1 - 力扣](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/)

## 题目大意

**描述**：给定一个二进制数组 $data$。

**要求**：通过交换位置，将数组中任何位置上的 $1$ 组合到一起，并返回所有可能中所需的最少交换次数。c 

**说明**：

- $1 \le data.length \le 10^5$。
- $data[i] == 0 \text{ or } 1$。

**示例**：

- 示例 1：

```python
输入: data = [1,0,1,0,1]
输出: 1
解释: 
有三种可能的方法可以把所有的 1 组合在一起：
[1,1,1,0,0]，交换 1 次；
[0,1,1,1,0]，交换 2 次；
[0,0,1,1,1]，交换 1 次。
所以最少的交换次数为 1。
```

- 示例 2：

```python
输入：data = [0,0,0,1,0]
输出：0
解释： 
由于数组中只有一个 1，所以不需要交换。
```

## 解题思路

### 思路 1：滑动窗口

将数组中任何位置上的 $1$ 组合到一起，并要求最少的交换次数。也就是说交换之后，某个连续子数组中全是 $1$，数组其他位置全是 $0$。为此，我们可以维护一个固定长度为 $1$ 的个数的滑动窗口，找到滑动窗口中 $0$ 最少的个数，这样最终交换出去的 $0$ 最少，交换次数也最少。

求最少交换次数，也就是求滑动窗口中最少的 $0$ 的个数。具体做法如下：

1. 统计 $1$ 的个数，并设置为窗口长度 $window\_size$。使用 $window\_count$ 维护窗口中 $0$ 的个数。使用 $ans$ 维护窗口中最少的 $0$ 的个数，也可以叫做最少交换次数。
2. 如果 $window\_size$ 为 $0$，则说明不用交换，直接返回 $0$。
3. 使用两个指针 $left$、$right$。$left$、$right$ 都指向数组的第一个元素，即：`left = 0`，`right = 0`。
4. 如果 $data[right] == 0$，则更新窗口中 $0$ 的个数，即 `window_count += 1`。然后向右移动 $right$。
5. 当窗口元素个数为 $window\_size$ 时，即：$right - left + 1 \ge window\_size$ 时，更新窗口中最少的 $0$ 的个数。
6. 然后如果左侧 $data[left] == 0$，则更新窗口中 $0$ 的个数，即 `window_count -= 1`。然后向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $window\_size$。
7. 重复 4 ~ 6 步，直到 $right$ 到达数组末尾。返回答案 $ans$。

### 思路 1：代码

```python
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = 0
        for item in data:
            if item == 1:
                window_size += 1
        if window_size == 0:
            return 0

        left, right = 0, 0
        window_count = 0
        ans = float('inf')
        while right < len(data):
            if data[right] == 0:
                window_count += 1

            if right - left + 1 >= window_size:
                ans = min(ans, window_count)
                if data[left] == 0:
                    window_count -= 1
                left += 1
            right += 1
        return ans if ans != float('inf') else 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $data$ 的长度。
- **空间复杂度**：$O(1)$。

