# [1423. 可获得的最大点数](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/)

- 标签：数组、前缀和、滑动窗口
- 难度：中等

## 题目链接

- [1423. 可获得的最大点数 - 力扣](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/)

## 题目大意

**描述**：将卡牌排成一行，给定每张卡片的点数数组 $cardPoints$，其中 $cardPoints[i]$ 表示第 $i$ 张卡牌对应点数。

每次行动，可以从行的开头或者末尾拿一张卡牌，最终保证正好拿到了 $k$ 张卡牌。所得点数就是你拿到手中的所有卡牌的点数之和。

现在给定一个整数数组 $cardPoints$ 和整数 $k$。

**要求**：返回可以获得的最大点数。

**说明**：

- $1 \le cardPoints.length \le 10^5$。
- $1 \le cardPoints[i] \le 10^4$
- $1 \le k \le cardPoints.length$。

**示例**：

- 示例 1：

```python
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12。
```

- 示例 2：

```python
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4。
```

## 解题思路

### 思路 1：滑动窗口

可以用固定长度的滑动窗口来做。

由于只能从开头或末尾位置拿 $k$ 张牌，则最后剩下的肯定是连续的 $len(cardPoints) - k$ 张牌。要求求出 $k$ 张牌可以获得的最大收益，我们可以反向先求出连续 $len(cardPoints) - k$ 张牌的最小点数。则答案为 $sum(cardPoints) - min\underline{\hspace{0.5em}}sum$。维护一个固定长度为 $len(cardPoints) - k$ 的滑动窗口，求最小和。具体做法如下：

1. $window\underline{\hspace{0.5em}}sum$ 用来维护窗口内的元素和，初始值为 $0$。$min\underline{\hspace{0.5em}}sum$ 用来维护滑动窗口元素的最小和。初始值为 $sum(cardPoints)$。滑动窗口的长度为 $window\underline{\hspace{0.5em}}size$，值为 $len(cardPoints) - k$。
2. 使用双指针 $left$、$right$。$left$ 、$right$ 都指向序列的第一个元素，即：`left = 0`，`right = 0`。
3. 向右移动 $right$，先将 $window\underline{\hspace{0.5em}}size$ 个元素填入窗口中。
4. 当窗口元素个数为 $window\underline{\hspace{0.5em}}size$ 时，即：$right - left + 1 \ge window\underline{\hspace{0.5em}}size$ 时，计算窗口内的元素和，并维护子数组最小和 $min\underline{\hspace{0.5em}}sum$。
5. 然后向右移动 $left$，从而缩小窗口长度，即 `left += 1`，使得窗口大小始终保持为 $k$。
6. 重复 4 ~ 5 步，直到 $right$ 到达数组末尾。
7. 最后输出 $sum(cardPoints) - min\underline{\hspace{0.5em}}sum$ 即为答案。

注意：如果 $window\underline{\hspace{0.5em}}size$ 为 $0$ 时需要特殊判断，此时答案为数组和 $sum(cardPoints)$。

### 思路 1：代码

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        window_sum = 0
        cards_sum = sum(cardPoints)
        min_sum = cards_sum

        left, right = 0, 0
        if window_size == 0:
            return cards_sum

        while right < len(cardPoints):
            window_sum += cardPoints[right]

            if right - left + 1 >= window_size:
                min_sum = min(window_sum, min_sum)
                window_sum -= cardPoints[left]
                left += 1

            right += 1

        return cards_sum - min_sum
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $cardPoints$ 中的元素数量。
- **空间复杂度**：$O(1)$。

