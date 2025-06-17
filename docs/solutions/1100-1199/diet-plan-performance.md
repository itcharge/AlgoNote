# [1176. 健身计划评估](https://leetcode.cn/problems/diet-plan-performance/)

- 标签：数组、滑动窗口
- 难度：简单

## 题目链接

- [1176. 健身计划评估 - 力扣](https://leetcode.cn/problems/diet-plan-performance/)

## 题目大意

**描述**：好友给自己制定了一份健身计划。想请你帮他评估一下这份计划是否合理。

给定一个数组 $calories$，其中 $calories[i]$ 代表好友第 $i$ 天需要消耗的卡路里总量。再给定 $lower$ 代表较低消耗的卡路里，$upper$ 代表较高消耗的卡路里。再给定一个整数 $k$，代表连续 $k$ 天。

- 如果你的好友在这一天以及之后连续 $k$ 天内消耗的总卡路里 $T$ 小于 $lower$，则这一天的计划相对糟糕，并失去 $1$ 分。
- 如果你的好友在这一天以及之后连续 $k$ 天内消耗的总卡路里 $T$ 高于 $upper$，则这一天的计划相对优秀，并得到 $1$ 分。
- 如果你的好友在这一天以及之后连续 $k$ 天内消耗的总卡路里 $T$ 大于等于 $lower$，并且小于等于 $upper$，则这份计划普普通通，分值不做变动。

**要求**：输出最后评估的得分情况。

**说明**：

- $1 \le k \le calories.length \le 10^5$。
- $0 \le calories[i] \le 20000$。
- $0 \le lower \le upper$。 

**示例**：

- 示例 1：

```python
输入：calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
输出：0
解释：calories[0], calories[1] < lower 而 calories[3], calories[4] > upper, 总分 = 0.
```

- 示例 2：

```python
输入：calories = [3,2], k = 2, lower = 0, upper = 1
输出：1
解释：calories[0] + calories[1] > upper, 总分 = 1.
```

## 解题思路

### 思路 1：滑动窗口

固定长度为 $k$ 的滑动窗口题目。具体做法如下：

1. $score$ 用来维护得分情况，初始值为 $0$。$window\underline{\hspace{0.5em}}sum$ 用来维护窗口中卡路里总量。
2. $left$ 、$right$ 都指向数组的第一个元素，即：`left = 0`，`right = 0`。
3. 向右移动 $right$，先将 $k$ 个元素填入窗口中。
4. 当窗口元素个数为 $k$ 时，即：$right - left + 1 \ge k$ 时，计算窗口内的卡路里总量，并判断和 $upper$、$lower$ 的关系。同时维护得分情况。
5. 然后向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $k$。
6. 重复 $4 \sim 5$ 步，直到 $right$ 到达数组末尾。

最后输出得分情况 $score$。

### 思路 1：代码

```python
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left, right = 0, 0
        window_sum = 0
        score = 0
        while right < len(calories):
            window_sum += calories[right]

            if right - left + 1 >= k:
                if window_sum < lower:
                    score -= 1
                elif window_sum > upper:
                    score += 1
                window_sum -= calories[left]
                left += 1

            right += 1
        return score
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $calories$ 的长度。
- **空间复杂度**：$O(1)$。

