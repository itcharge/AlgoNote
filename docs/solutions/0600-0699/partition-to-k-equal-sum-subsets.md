# [0698. 划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)

- 标签：位运算、记忆化搜索、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [0698. 划分为k个相等的子集 - 力扣](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/)

## 题目大意

**描述**：给定一个整数数组 $nums$ 和一个正整数 $k$。

**要求**：找出是否有可能把这个数组分成 $k$ 个非空子集，其总和都相等。

**说明**：

- $1 \le k \le len(nums) \le 16$。
- $0 < nums[i] < 10000$。
- 每个元素的频率在 $[1, 4]$ 范围内。

**示例**：

- 示例 1：

```python
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
```

- 示例 2：

```python
输入: nums = [1,2,3,4], k = 3
输出: False
```

## 解题思路

### 思路 1：状态压缩 DP

根据题目要求，我们可以将几种明显不符合要求的情况过滤掉，比如：元素个数小于 $k$、元素总和不是 $k$ 的倍数、数组 $nums$ 中最大元素超过 $k$ 等分的目标和这几种情况。

然后再来考虑一般情况下，如何判断是否符合要求。

因为题目给定数组 $nums$ 的长度最多为 $16$，所以我们可以使用一个长度为 $16$ 位的二进制数来表示数组子集的选择状态。我们可以定义 $dp[state]$ 表示为当前选择状态下，是否可行。如果 $dp[state] == True$，表示可行；如果 $dp[state] == False$，则表示不可行。

接下来使用动态规划方法，进行求解。具体步骤如下：

###### 1. 阶段划分

按照数组元素选择情况进行阶段划分。

###### 2. 定义状态

定义状态 $dp[state]$ 表示为：当数组元素选择情况为 $state$ 时，是否存在一种方案，使得方案中的数字必定能分割成 $p(0 \le p \le k)$ 组恰好数字和等于目标和 $target$ 的集合和至多 $1$ 组数字和小于目标和 $target$ 的集合。

###### 3. 状态转移方程

对于当前状态 $state$，如果：

1. 当数组元素选择情况为 $state$ 时可行，即 $dp[state] == True$；
2. 第 $i$ 位数字没有被使用；
3. 加上第 $i$ 位元素后的状态为 $next\_state$；
4. 加上第 $i$ 位元素后没有超出目标和。

则：$dp[next\_state] = True$。

###### 4. 初始条件

- 当不选择任何元素时，可按照题目要求

###### 5. 最终结果

根据我们之前定义的状态，$dp[state]$ 表示为：当数组元素选择情况为 $state$ 时，是否存在一种方案，使得方案中的数字必定能分割成 $p(0 \le p \le k)$ 组恰好数字和等于目标和 $target$ 的集合和至多 $1$ 组数字和小于目标和 $target$ 的集合。

所以当 $state == 1 << n - 1$ 时，状态就变为了：当数组元素都选上的情况下，是否存在一种方案，使得方案中的数字必定能分割成 $k$ 组恰好数字和等于目标和 $target$ 的集合。

这里之所以是 $k$ 组恰好数字和等于目标和 $target$ 的集合，是因为一开我们就限定了 $total \mod k == 0$ 这个条件，所以只能是 $k$ 组恰好数字和等于目标和 $target$ 的集合。

所以最终结果为 $dp[states - 1]$，其中 $states = 1 << n$。

### 思路 1：代码

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        if size < k:            # 元素个数小于 k
            return False

        total = sum(nums)
        if total % k != 0:      # 元素总和不是 k 的倍数
            return False

        target = total // k
        if nums[-1] > target:   # 最大元素超过 k 等分的目标和
            return False

        nums.sort()
        states = 1 << size      # 子集选择状态总数
        cur_sum = [0 for _ in range(states)]
        dp = [False for _ in range(states)]
        dp[0] = True

        for state in range(states):
            if not dp[state]:                   # 基于 dp[state] == True 前提下进行转移        
                continue
            for i in range(size):
                if state & (1 << i) != 0:       # 当前数字已被使用
                    continue
                
                if cur_sum[state] % target + nums[i] > target:
                    break                       # 如果加入当前数字超出目标和，则后续不用继续遍历

                next_state = state | (1 << i)   # 加入当前数字
                if dp[next_state]:              # 如果新状态能划分，则跳过继续
                    continue
                
                cur_sum[next_state] = cur_sum[state] + nums[i]  # 更新新状态下子集和
                dp[next_state] = True           # 更新新状态
                if dp[states - 1]:              # 找到一个符合要求的划分方案，提前返回
                    return True
                
        return dp[states - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(2^n)$。

## 参考资料

- 【题解】[状态压缩的定义理解 - 划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/zhuang-tai-ya-suo-de-ding-yi-li-jie-by-c-fo1b/)
