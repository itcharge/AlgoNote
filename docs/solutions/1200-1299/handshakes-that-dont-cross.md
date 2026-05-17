# [1259. 不相交的握手](https://leetcode.cn/problems/handshakes-that-dont-cross/)

- 标签：数学、动态规划
- 难度：困难

## 题目链接

- [1259. 不相交的握手 - 力扣](https://leetcode.cn/problems/handshakes-that-dont-cross/)

## 题目大意

**描述**：偶数个人站成一个圆，总人数为 $numPeople$。每个人与除自己外的一个人握手，总共会有 $numPeople / 2$ 次握手。将握手的人之间连线，要求连线不会相交。

**要求**：返回连线不会相交的握手方案数，结果模 $10^9 + 7$。

**说明**：

- $2 \le numPeople \le 1000$。
- $numPeople \bmod 2 == 0$。

**示例**：

- 示例 1：

```python
输入：num_people = 2
输出：1
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/5125_example_2.png)

```python
输入：num_people = 4
输出：2
解释：总共有两种方案，第一种方案是 [(1,2),(3,4)]，第二种方案是 [(2,3),(4,1)]。
```

## 解题思路

### 思路 1：卡特兰数 + 动态规划

###### 1. 阶段划分

按照总人数 $i$（$i$ 为偶数）来划分阶段。每次固定一个人，让他和另一个人握手，将圆分割成两个独立的子问题。

###### 2. 定义状态

定义 $dp[i]$ 表示 $i$ 个人（$i$ 为偶数）站成一个圆时，不相交握手的方案数。

###### 3. 状态转移方程

在圆上任选一个人（比如编号 $0$）。他要和另一个人握手，握手后连线将圆分成左右两部分。关键要求是：左右两部分的人数都必须为偶数，否则内部的人无法两两握手而不穿过这条连线。

假设编号 $0$ 的人与编号 $2k+1$ 的人握手（中间有 $2k$ 个人，右边有 $i - 2k - 2$ 个人），那么：

$$dp[i] = \sum_{k=0}^{(i/2)-1} dp[2k] \times dp[i - 2k - 2]$$

其中 $dp[0] = 1$（$0$ 个人只有 $1$ 种握手方式——什么都不做）。

这个递推式实际上就是**卡特兰数（Catalan number）**的递推形式。卡特兰数 $C_n$ 的递推公式为 $C_0 = 1$，$C_{n+1} = \sum_{i=0}^{n} C_i \times C_{n-i}$。

###### 4. 初始条件

- $dp[0] = 1$（边界条件，空集只有一种方案）。

###### 5. 最终结果

返回 $dp[numPeople]$。

**结合示例走一遍：**

- $numPeople = 2$（$i=2$）：
  - $k=0$：$dp[0] \times dp[0] = 1 \times 1 = 1$
  - $dp[2] = 1$

- $numPeople = 4$（$i=4$）：
  - $k=0$：$dp[0] \times dp[2] = 1 \times 1 = 1$
  - $k=1$：$dp[2] \times dp[0] = 1 \times 1 = 1$
  - $dp[4] = 2$

与题目示例一致。

### 思路 1：代码

```python
class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[i] 表示 i 个人（i 为偶数）的不相交握手方案数
        dp = [0] * (numPeople + 1)
        dp[0] = 1

        for i in range(2, numPeople + 1, 2):
            # 枚举第一个人和谁握手
            for k in range(0, i, 2):
                dp[i] = (dp[i] + dp[k] * dp[i - k - 2]) % MOD

        return dp[numPeople]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是 $numPeople$。外层循环遍历所有偶数人数（约 $n/2$ 次），内层循环枚举握手对象（最多约 $n/2$ 次），总计算量约为 $O(n^2/4)$。
- **空间复杂度**：$O(n)$，需要长度为 $numPeople + 1$ 的 $dp$ 数组。
