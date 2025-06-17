# [0374. 猜数字大小](https://leetcode.cn/problems/guess-number-higher-or-lower/)

- 标签：二分查找、交互
- 难度：简单

## 题目链接

- [0374. 猜数字大小 - 力扣](https://leetcode.cn/problems/guess-number-higher-or-lower/)

## 题目大意

**描述**：猜数字游戏。给定一个整数 $n$ 和一个接口 `def guess(num: int) -> int:`，题目会从 $1 \sim n$ 中随机选取一个数 $x$。我们只能通过调用接口来判断自己猜测的数是否正确。

**要求**：要求返回题目选取的数字 $x$。

**说明**：

- `def guess(num: int) -> int:` 返回值：
  - $-1$：我选出的数字比你猜的数字小，即 $pick < num$；
  - $1$：我选出的数字比你猜的数字大 $pick > num$；
  - $0$：我选出的数字和你猜的数字一样。恭喜！你猜对了！$pick == num$。

**示例**：

- 示例 1：

```python
输入：n = 10, pick = 6
输出：6
```

- 示例 2：

```python
输入：n = 1, pick = 1
输出：1
```

## 解题思路

### 思路 1：二分查找

利用两个指针 $left$、$right$。$left$ 指向数字 $1$，$right$ 指向数字 $n$。每次从中间开始调用接口猜测是否正确。

- 如果猜测的数比选中的数大，则将 $right$ 向左移，令 `right = mid - 1`，继续从中间调用接口猜测；
- 如果猜测的数比选中的数小，则将 $left$ 向右移，令 `left = mid + 1`，继续从中间调用的接口猜测；
- 如果猜测正确，则直接返回该数。

### 思路 1：二分查找代码

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ans = guess(mid)
            if ans == 1:
                left = mid + 1
            elif ans == -1:
                right = mid - 1
            else:
                return mid
        return 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。二分查找算法的时间复杂度为 $O(\log n)$。
- **空间复杂度**：$O(1)$。只用到了常数空间存放若干变量。
