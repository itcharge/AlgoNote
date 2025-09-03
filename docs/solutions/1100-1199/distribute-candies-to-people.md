# [1103. 分糖果 II](https://leetcode.cn/problems/distribute-candies-to-people/)

- 标签：数学、模拟
- 难度：简单

## 题目链接

- [1103. 分糖果 II - 力扣](https://leetcode.cn/problems/distribute-candies-to-people/)

## 题目大意

**描述**：给定一个整数 $candies$，代表糖果的数量。再给定一个整数 $num\_people$，代表小朋友的数量。

现在开始分糖果，给第 $1$ 个小朋友分 $1$ 颗糖果，第 $2$ 个小朋友分 $2$ 颗糖果，以此类推，直到最后一个小朋友分 $n$ 颗糖果。

然后回到第 $1$ 个小朋友，给第 $1$ 个小朋友分 $n + 1$ 颗糖果，第 $2$ 个小朋友分 $n + 2$ 颗糖果，一次类推，直到最后一个小朋友分 $n + n$ 颗糖果。

重复上述过程（每次都比上一次多给出 $1$ 颗糖果，当分完第 $n$ 个小朋友时回到第 $1$ 个小朋友），直到我们分完所有的糖果。

> 注意：如果我们手中剩下的糖果数不够（小于等于前一次发的糖果数），则将剩下的糖果全部发给当前的小朋友。

**要求**：返回一个长度为 $num\_people$、元素之和为 $candies$ 的数组，以表示糖果的最终分发情况（即 $ans[i]$ 表示第 $i$ 个小朋友分到的糖果数）。

**说明**：

- $1 \le candies \le 10^9$。
- $1 \le num\_people \le 1000$。

**示例**：

- 示例 1：

```python
输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
```

- 示例 2：

```python
输入：candies = 10, num_people = 3
输出：[5,2,3]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0]。
第三次，ans[2] += 3，数组变为 [1,2,3]。
第四次，ans[0] += 4，最终数组变为 [5,2,3]。
```

## 解题思路

### 思路 1：暴力模拟

不断遍历数组，将对应糖果数分给当前小朋友，直到糖果数为 $0$ 时停止。

### 思路 1：代码

```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        idx = 0
        while candies:
            ans[idx % num_people] += min(idx + 1, candies)
            candies -= min(idx + 1, candies)
            idx += 1
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(max(\sqrt{m}, n))$，其中 $m$ 为糖果数量，$n$ 为小朋友数量。
- **空间复杂度**：$O(1)$。

