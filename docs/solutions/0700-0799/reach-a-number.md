# [0754. 到达终点数字](https://leetcode.cn/problems/reach-a-number/)

- 标签：数学、二分查找
- 难度：中等

## 题目链接

- [0754. 到达终点数字 - 力扣](https://leetcode.cn/problems/reach-a-number/)

## 题目大意

**描述**：

在一根无限长的数轴上，你站在 $0$ 的位置。终点在 $target$ 的位置。

你可以做一些数量的移动 $numMoves$:

- 每次你可以选择向左或向右移动。
- 第 $i$ 次移动（从 $i == 1$ 开始，到 $i == numMoves$），在选择的方向上走 $i$ 步。

给定整数 $target$。

**要求**：

返回 到达目标所需的 最小 移动次数(即最小 $numMoves$ ) 。


**说明**：

- $-10^{9} \le target \le 10^{9}$。
- target != 0。

**示例**：

- 示例 1：

```python
示例 1:


输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：数学

在数轴上，从 $0$ 开始，第 $i$ 步可以向左或向右移动 $i$ 步。要到达 $target$，需要找到最小的移动次数。

**分析**：

- 如果一直向右移动，第 $n$ 步后位置为 $1 + 2 + ... + n = \frac{n(n+1)}{2}$。
- 如果某些步向左移动，相当于从总和中减去这些步的两倍。
- 设向右移动的步为正，向左移动的步为负，则：$sum - 2 \times neg = target$。
- 即：$neg = \frac{sum - target}{2}$。

**步骤**：

1. 由于对称性，可以只考虑 $target$ 的绝对值。
2. 找到最小的 $n$，使得 $sum = \frac{n(n+1)}{2} \ge |target|$。
3. 如果 $sum - |target|$ 是偶数，则可以通过翻转某些步到达 $target$，返回 $n$。
4. 否则，继续增加步数，直到差值为偶数。

### 思路 1：代码

```python
class Solution:
    def reachNumber(self, target: int) -> int:
        # 由于对称性，只考虑绝对值
        target = abs(target)
        
        n = 0
        sum_n = 0
        
        # 找到最小的 n，使得 sum >= target
        while sum_n < target:
            n += 1
            sum_n += n
        
        # 如果差值是偶数，可以直接到达
        diff = sum_n - target
        if diff % 2 == 0:
            return n
        
        # 否则，继续增加步数
        # 如果 n 是奇数，再走 2 步（n+1 和 n+2），差值增加 2n+3（奇数）
        # 如果 n 是偶数，再走 1 步（n+1），差值增加 n+1（奇数）
        # 总之，最多再走 2 步就能使差值为偶数
        while diff % 2 != 0:
            n += 1
            sum_n += n
            diff = sum_n - target
        
        return n
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\sqrt{target})$，需要找到 $n$ 使得 $\frac{n(n+1)}{2} \ge target$。
- **空间复杂度**：$O(1)$。
