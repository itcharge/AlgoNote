# [0646. 最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/)

- 标签：贪心、数组、动态规划、排序
- 难度：中等

## 题目链接

- [0646. 最长数对链 - 力扣](https://leetcode.cn/problems/maximum-length-of-pair-chain/)

## 题目大意

**描述**：

给定一个由 $n$ 个数对组成的数对数组 $pairs$ ，其中 $pairs[i] = [left_i, right_i]$ 且 $left_i < right_i$ 。

现在，我们定义一种「跟随」关系，当且仅当 $b < c$ 时，数对 $p2 = [c, d]$ 才可以跟在 $p1 = [a, b]$ 后面。我们用这种形式来构造「数对链」。

**要求**：

找出并返回能够形成的 最长数对链的长度 。
你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

**说明**：

- $n == pairs.length$。
- $1 \le n \le 10^{3}$。
- $-10^{3} \le left_i \lt right_i \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入：pairs = [[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4] 。
```

- 示例 2：

```python
输入：pairs = [[1,2],[7,8],[4,5]]
输出：3
解释：最长的数对链是 [1,2] -> [4,5] -> [7,8] 。
```

## 解题思路

### 思路 1：贪心

这道题目要求找到最长的数对链。可以使用贪心策略：按照数对的右端点排序，然后依次选择不冲突的数对。

1. 将数对按照右端点从小到大排序。
2. 初始化链的长度 $count = 1$，当前链的末尾为第一个数对的右端点 $curr\underline{~}end = pairs[0][1]$。
3. 从第二个数对开始遍历：
   - 如果当前数对的左端点大于 $curr\underline{~}end$，说明可以将当前数对加入链中。
   - 更新 $curr\underline{~}end$ 为当前数对的右端点，$count$ 加 1。
4. 返回 $count$。

### 思路 1：代码

```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 按照右端点排序
        pairs.sort(key=lambda x: x[1])
        
        count = 1
        curr_end = pairs[0][1]
        
        for i in range(1, len(pairs)):
            # 如果当前数对的左端点大于链的末尾，可以加入链中
            if pairs[i][0] > curr_end:
                count += 1
                curr_end = pairs[i][1]
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数对的数量。主要时间消耗在排序上。
- **空间复杂度**：$O(\log n)$，排序所需的栈空间。
