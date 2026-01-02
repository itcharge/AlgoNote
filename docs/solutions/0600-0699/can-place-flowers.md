# [0605. 种花问题](https://leetcode.cn/problems/can-place-flowers/)

- 标签：贪心、数组
- 难度：简单

## 题目链接

- [0605. 种花问题 - 力扣](https://leetcode.cn/problems/can-place-flowers/)

## 题目大意

**描述**：

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个整数数组 $flowerbed$ 表示花坛，由若干 $0$ 和 $1$ 组成，其中 $0$ 表示没种植花，$1$ 表示种植了花。另给定一个数 $n$。

**要求**：

能否在不打破种植规则的情况下种入 $n$ 朵花？能则返回 true，不能则返回 false 。

**说明**：

- $1 \le flowerbed.length \le 2 \times 10^{4}$。
- $flowerbed[i]$ 为 $0$ 或 $1$。
- $flowerbed$ 中不存在相邻的两朵花。
- $0 \le n \le flowerbed.length$。

**示例**：

- 示例 1：

```python
输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
```

- 示例 2：

```python
输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
```

## 解题思路

### 思路 1：贪心算法

#### 思路 1：算法描述

这道题目要求在不违反种植规则的情况下，判断能否种入 $n$ 朵花。种植规则是：花不能种植在相邻的地块上。

我们可以使用贪心算法，从左到右遍历花坛，只要当前位置和相邻位置都没有花，就尽可能地种花。

具体步骤如下：

1. 遍历花坛数组 $flowerbed$，对于每个位置 $i$：
   - 如果 $flowerbed[i] = 0$（当前位置没有花）。
   - 并且 $i = 0$ 或 $flowerbed[i - 1] = 0$（左边没有花或者是边界）。
   - 并且 $i = len(flowerbed) - 1$ 或 $flowerbed[i + 1] = 0$（右边没有花或者是边界）。
   - 则在当前位置种花，将 $flowerbed[i]$ 设置为 $1$，并将计数器 $n$ 减 $1$。
2. 如果 $n \le 0$，说明已经种够了 $n$ 朵花，返回 $True$。
3. 遍历结束后，如果 $n > 0$，说明无法种够 $n$ 朵花，返回 $False$。

#### 思路 1：代码

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 遍历花坛
        for i in range(len(flowerbed)):
            # 当前位置没有花，且左右两边都没有花（或者是边界）
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # 在当前位置种花
                flowerbed[i] = 1
                n -= 1
                # 如果已经种够了，直接返回 True
                if n <= 0:
                    return True
        # 遍历结束后，判断是否种够了
        return n <= 0
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(m)$，其中 $m$ 是花坛的长度。只需要遍历一次花坛数组。
- **空间复杂度**：$O(1)$。只使用了常数级别的额外空间。
