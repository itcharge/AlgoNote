# [1218. 最长定差子序列](https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/)

- 标签：数组、哈希表、动态规划
- 难度：中等

## 题目链接

- [1218. 最长定差子序列 - 力扣](https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/)

## 题目大意

**描述**：给你一个整数数组 $arr$ 和一个整数 $difference$。

**要求**：找出并返回 $arr$ 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 $difference$。子序列是指在不改变其余元素顺序的情况下，通过删除一些元素派生出来的序列。

**说明**：

- $1 \le arr.length \le 10^{5}$。
- $-10^{4} \le arr[i], difference \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
```

- 示例 2：

```python
输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
```

- 示例 3：

```python
输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
```

## 解题思路

### 思路 1：哈希表 + 动态规划

###### 1. 阶段划分

按遍历数组的顺序划分阶段。每遇到一个新元素 $num$，我们考虑把它接在之前某个以 $num - difference$ 结尾的子序列后面。

###### 2. 定义状态

定义 $dp[num]$ 表示以数字 $num$ 结尾的最长定差子序列的长度。

###### 3. 状态转移方程

对于当前数字 $num$，它前面一个数应该是 $prev = num - difference$。如果 $prev$ 出现过，就可以把当前数字接到以 $prev$ 结尾的最长子序列后面：

$$dp[num] = dp[prev] + 1 \quad (\text{如果 } prev \text{ 存在})$$

如果 $prev$ 没出现过，那么以 $num$ 结尾的最长子序列就是它自己，长度为 $1$：

$$dp[num] = 1$$

合并成一个简洁的写法（利用字典的 $get$ 方法，键不存在时返回 $0$）：

$$dp[num] = dp.get(prev, 0) + 1$$

###### 4. 初始条件

$dp$ 初始为空字典，在遍历过程中逐步填充。

###### 5. 最终结果

所有 $dp$ 值中的最大值。

需要注意的是：为什么不直接用数组 $dp$？因为 $arr[i]$ 的范围是 $-10^{4} \le arr[i] \le 10^{4}$，但通过加 $difference$ 后数值可能超出这个范围（示例 3 中 $difference=-2$，序列从 $7$ 一路到 $1$），所以用哈希表更灵活。

**结合示例 3 走一遍：**

$arr = [1,5,7,8,5,3,4,2,1], difference = -2$

遍历过程：
- $num=1$：$prev=3$ 不存在 → $dp[1]=1$
- $num=5$：$prev=7$ 不存在 → $dp[5]=1$
- $num=7$：$prev=9$ 不存在 → $dp[7]=1$
- $num=8$：$prev=10$ 不存在 → $dp[8]=1$
- $num=5$：$prev=7$ → $dp[5]=dp[7]+1=2$
- $num=3$：$prev=5$ → $dp[3]=dp[5]+1=3$
- $num=4$：$prev=6$ 不存在 → $dp[4]=1$
- $num=2$：$prev=4$ → $dp[2]=dp[4]+1=2$
- $num=1$：$prev=3$ → $dp[1]=dp[3]+1=4$

最大值是 $4$，对应子序列 $[7,5,3,1]$。

### 思路 1：代码

```python
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp[num] 表示以 num 结尾的最长定差子序列的长度
        dp = {}
        for num in arr:
            prev = num - difference
            # 如果 prev 存在就接在后面，否则长度为 1
            dp[num] = dp.get(prev, 0) + 1
        return max(dp.values())
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $arr$ 的长度。只需一次遍历，每次进行 $O(1)$ 的哈希表操作。
- **空间复杂度**：$O(n)$，哈希表在最坏情况下需要存储 $n$ 个不同的数字。
