# [1217. 玩筹码](https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/)

- 标签：贪心、数组、数学
- 难度：简单

## 题目链接

- [1217. 玩筹码 - 力扣](https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/)

## 题目大意

**描述**：给定一个数组 $position$ 代表 $n$ 个筹码的位置，其中 $position[i]$ 代表第 $i$ 个筹码的位置。现在需要把所有筹码移到同一个位置。在一步中，我们可以将第 $i$ 个芯片的位置从 $position[i]$ 改变为:

- $position[i] + 2$ 或 $position[i] - 2$，此时 $cost = 0$；
- $position[i] + 1$ 或 $position[i] - 1$，此时 $cost = 1$。

即移动偶数位长度的代价为 $0$，移动奇数位长度的代价为 $1$。

**要求**：返回将所有筹码移动到同一位置上所需要的 最小代价 。

**说明**：

- $1 \le chips.length \le 100$。
- $1 \le chips[i] \le 10^9$。

**示例**：

- 示例 1：

```python
输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个芯片移到位置 2。每一步的成本为 1。总成本 = 2。
```

## 解题思路

### 思路 1：贪心算法

题目中移动偶数位长度是不需要代价的，所以奇数位移动到奇数位不需要代价，偶数位移动到偶数位也不需要代价。

则我们可以想将所有偶数位都移动到下标为 $0$ 的位置，奇数位都移动到下标为 $1$ 的位置。

这样，所有的奇数位、偶数位上的人都到相同或相邻位置了。

我们只需要统计一下奇数位和偶数位的数字个数。将少的数移动到多的数上边就是最小代价。

则这道题就可以通过以下步骤求解：

- 遍历数组，统计数组中奇数个数和偶数个数。
- 返回奇数个数和偶数个数中较小的数即为答案。

### 思路 1：贪心算法代码

```python
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for p in position:
            if p & 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $poition$ 的长度。
- **空间复杂度**：$O(1)$。
