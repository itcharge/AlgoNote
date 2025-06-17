# [1011. 在 D 天内送达包裹的能力](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [1011. 在 D 天内送达包裹的能力 - 力扣](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/)

## 题目大意

**描述**：传送带上的包裹必须在 $D$ 天内从一个港口运送到另一个港口。给定所有包裹的重量数组 $weights$，货物必须按照给定的顺序装运。且每天船上装载的重量不会超过船的最大运载重量。

**要求**：求能在 $D$ 天内将所有包裹送达的船的最低运载量。

**说明**：

- $1 \le days \le weights.length \le 5 * 10^4$。
- $1 \le weights[i] \le 500$。

**示例**：

- 示例 1：

```python
输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10
请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
```

- 示例 2：

```python
输入：weights = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
```

## 解题思路

### 思路 1：二分查找

船最小的运载能力，最少也要等于或大于最重的那件包裹，即 $max(weights)$。最多的话，可以一次性将所有包裹运完，即 $sum(weights)$。船的运载能力介于 $[max(weights), sum(weights)]$ 之间。

我们现在要做的就是从这个区间内，找到满足可以在 $D$ 天内运送完所有包裹的最小载重量。

可以通过二分查找的方式，找到满足要求的最小载重量。

### 思路 1：代码

```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) >> 1
            days = 1
            cur = 0
            for weight in weights:
                if cur + weight > mid:
                    days += 1
                    cur = 0
                cur += weight

            if days <= D:
                right = mid
            else:
                left = mid + 1
        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。二分查找算法的时间复杂度为 $O(\log n)$。
- **空间复杂度**：$O(1)$。只用到了常数空间存放若干变量。

