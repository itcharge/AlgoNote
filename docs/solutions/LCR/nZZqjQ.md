# [LCR 073. 爱吃香蕉的狒狒](https://leetcode.cn/problems/nZZqjQ/)

- 标签：数组、二分查找
- 难度：中等

## 题目链接

- [LCR 073. 爱吃香蕉的狒狒 - 力扣](https://leetcode.cn/problems/nZZqjQ/)

## 题目大意

给定一个数组 `piles` 代表 `n` 堆香蕉。其中 `piles[i]` 表示第 `i` 堆香蕉的个数。再给定一个整数 `h` ，表示最多可以在 `h` 小时内吃完所有香蕉。狒狒决定以速度每小时 `k`（未知）根的速度吃香蕉。每一个小时，她将选择其中一堆香蕉，从中吃掉 `k` 根。如果这堆香蕉少于 `k` 根，狒狒将在这一小时吃掉这堆的所有香蕉，并且这一小时不会再吃其他堆的香蕉。  

要求：返回狒狒可以在 `h` 小时内吃掉所有香蕉的最小速度 `k`（`k` 为整数）。

## 解题思路

先来看 `k` 的取值范围，因为 `k` 是整数，且速度肯定不能为 `0` 吧，为 `0` 的话就永远吃不完了。所以`k` 的最小值可以取 `1`。`k` 的最大值根香蕉中最大堆的香蕉个数有关，因为 `1` 个小时内只能选择一堆吃，不能再吃其他堆的香蕉，则 `k` 的最大值取香蕉堆的最大值即可。即 `k` 的最大值为 `max(piles)`。

我们的目标是求出 `h` 小时内吃掉所有香蕉的最小速度 `k`。现在有了区间「`[1, max(piles)]`」，有了目标「最小速度 `k`」。接下来使用二分查找算法来查找「最小速度 `k`」。至于计算 `h` 小时内能否以 `k` 的速度吃完香蕉，我们可以再写一个方法 `canEat` 用于判断。如果能吃完就返回 `True`，不能吃完则返回 `False`。下面说一下算法的具体步骤。

- 使用两个指针 `left`、`right`。令 `left` 指向 `1`，`right` 指向 `max(piles)`。代表待查找区间为 `[left, right]`

- 取两个节点中心位置 `mid`，判断是否能在 `h` 小时内以 `k` 的速度吃完香蕉。
  - 如果不能吃完，则将区间 `[left, mid]` 排除掉，继续在区间 `[mid + 1, right]` 中查找。
  - 如果能吃完，说明 `k` 还可以继续减小，则继续在区间 `[left, mid]` 中查找。
- 当 `left == right` 时跳出循环，返回 `left`。

## 代码

```python
class Solution:
    def canEat(self, piles, hour, speed):
        time = 0
        for pile in piles:
            time += (pile + speed - 1) // speed
        return time <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canEat(piles, h, mid):
                left = mid + 1
            else:
                right = mid

        return left
```

