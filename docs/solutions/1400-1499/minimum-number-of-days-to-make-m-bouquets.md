# [1482. 制作 m 束花所需的最少天数](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [1482. 制作 m 束花所需的最少天数 - 力扣](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/)

## 题目大意

**描述**：给定一个整数数组 $bloomDay$，以及两个整数 $m$ 和 $k$。$bloomDay$ 代表花朵盛开的时间，$bloomDay[i]$ 表示第 $i$ 朵花的盛开时间。盛开后就可以用于一束花中。

现在需要制作 $m$ 束花。制作花束时，需要使用花园中相邻的 $k$ 朵花 。

**要求**：返回从花园中摘 $m$ 束花需要等待的最少的天数。如果不能摘到 $m$ 束花则返回 $-1$。

**说明**：

- $bloomDay.length == n$。
- $1 \le n \le 10^5$。
- $1 \le bloomDay[i] \le 10^9$。
- $1 \le m \le 10^6$。
- $1 \le k \le n$。

**示例**：

- 示例 1：

```python
输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
输出：3
解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
现在需要制作 3 束花，每束只需要 1 朵。
1 天后：[x, _, _, _, _]   // 只能制作 1 束花
2 天后：[x, _, _, _, x]   // 只能制作 2 束花
3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
```

- 示例 2：

```python
输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
输出：-1
解释：要制作 3 束花，每束需要 2 朵花，也就是一共需要 6 朵花。而花园中只有 5 朵花，无法满足制作要求，返回 -1。
```

## 解题思路

### 思路 1：二分查找算法

这道题跟「[0875. 爱吃香蕉的珂珂](https://leetcode.cn/problems/koko-eating-bananas/)」、「[1011. 在 D 天内送达包裹的能力](https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/)」有点相似。

根据题目可知：

- 制作花束最少使用时间跟花朵开花最短时间有关系，即 $min(bloomDay)$。
- 制作花束最多使用时间跟花朵开花最长时间有关系，即 $max(bloomDay)$。
- 则制作花束所需要的天数就变成了一个区间 $[min(bloomDay), max(bloomDay)]$。

那么，我们就可以根据这个区间，利用二分查找算法找到一个符合题意的最少天数。而判断某个天数下能否摘到 $m$ 束花则可以写个方法判断。具体步骤如下：

-  遍历数组 $bloomDay$。
   - 如果 $bloomDay[i] \le days$。就将花朵数量加 $1$。
     - 当能摘的花朵数等于 $k$ 时，能摘的花束数目加 $1$，花朵数量置为 $0$。
   - 如果 $bloomDay[i] > days$。就将花朵数置为 $0$。
-  最后判断能摘的花束数目是否大于等于 $m$。

整个算法的步骤如下：

- 如果 $m \times k > len(bloomDay)$，说明无法满足要求，直接返回 $-1$。
- 使用两个指针 $left$、$right$。令 $left$ 指向 $min(bloomDay)$，$right$ 指向 $max(bloomDay)$。代表待查找区间为 $[left, right]$。
- 取两个节点中心位置 $mid$，判断是否能在 $mid$ 天制作 $m$ 束花。
  - 如果不能，则将区间 $[left, mid]$ 排除掉，继续在区间 $[mid + 1, right]$ 中查找。
  - 如果能，说明天数还可以继续减少，则继续在区间 $[left, mid]$ 中查找。
- 当 $left == right$ 时跳出循环，返回 $left$。

### 思路 1：代码

```python
class Solution:
    def canMake(self, bloomDay, days, m, k):
        count = 0
        flower = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                flower += 1
                if flower == k:
                    count += 1
                    flower = 0
            else:
                flower = 0
        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canMake(bloomDay, mid, m, k):
                left = mid + 1
            else:
                right = mid

        return left
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log (max(bloomDay) - min(bloomDay)))$。
- **空间复杂度**：$O(1)$。

## 参考资料

- 【题解】[【赤小豆】为什么是二分法，思路及模板 python - 制作 m 束花所需的最少天数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/solution/chi-xiao-dou-python-wei-shi-yao-shi-er-f-24p7/)

