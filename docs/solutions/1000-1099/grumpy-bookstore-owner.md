# [1052. 爱生气的书店老板](https://leetcode.cn/problems/grumpy-bookstore-owner/)

- 标签：数组、滑动窗口
- 难度：中等

## 题目链接

- [1052. 爱生气的书店老板 - 力扣](https://leetcode.cn/problems/grumpy-bookstore-owner/)

## 题目大意

**描述**：书店老板有一家店打算试营业 $len(customers)$ 分钟。每一分钟都有一些顾客 $customers[i]$ 会进入书店，这些顾客会在这一分钟结束后离开。

在某些时候，书店老板会生气。如果书店老板在第 $i$ 分钟生气，则 `grumpy[i] = 1`，如果第 $i$ 分钟不生气，则 `grumpy[i] = 0`。当书店老板生气时，这一分钟的顾客会不满意。当书店老板不生气时，这一分钟的顾客是满意的。

假设老板知道一个秘密技巧，能保证自己连续 $minutes$ 分钟不生气，但只能使用一次。

现在给定代表每分钟进入书店的顾客数量的数组 $customes$，和代表老板生气状态的数组 $grumpy$，以及老板保证连续不生气的分钟数 $minutes$。

**要求**：计算出试营业下来，最多有多少客户能够感到满意。

**说明**：

- $n == customers.length == grumpy.length$。
- $1 \le minutes \le n \le 2 \times 10^4$。
- $0 \le customers[i] \le 1000$。
- $grumpy[i] == 0 \text{ or } 1$。

**示例**：

- 示例 1：

```python
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

- 示例 2：

```python
输入：customers = [1], grumpy = [0], minutes = 1
输出：1
```

## 解题思路

### 思路 1：滑动窗口

固定长度的滑动窗口题目。我们可以维护一个窗口大小为 $minutes$ 的滑动窗口。使用 $window_count$ 记录当前窗口内生气的顾客人数。然后滑动求出窗口中最大顾客数，然后累加上老板未生气时的顾客数，就是答案。具体做法如下：

1. $ans$ 用来维护答案数目。$window\_count$ 用来维护窗口中生气的顾客人数。
2. $left$ 、$right$ 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
3. 如果书店老板生气，则将这一分钟的顾客数量加入到 $window\_count$ 中，然后向右移动 $right$。
4. 当窗口元素个数大于 $minutes$ 时，即：$right - left + 1 > count$ 时，如果最左侧边界老板处于生气状态，则向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为小于 $minutes$。
5. 重复 $3 \sim 4$ 步，直到 $right$ 到达数组末尾。
6. 然后累加上老板未生气时的顾客数，最后输出答案。

### 思路 1：代码

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        right = 0
        window_count = 0
        ans = 0

        while right < len(customers):
            if grumpy[right] == 1:
                window_count += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_count -= customers[left]
                left += 1

            right += 1
            ans = max(ans, window_count)

        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $coustomer$、$grumpy$ 的长度。
- **空间复杂度**：$O(1)$。

