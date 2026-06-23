# [1477. 找两个和为目标值且不重叠的子数组](https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

- 标签：数组、哈希表、二分查找、动态规划、滑动窗口、前缀和
- 难度：中等

## 题目链接

- [1477. 找两个和为目标值且不重叠的子数组 - 力扣](https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个整数 $target$。

**要求**：找到两个不重叠的子数组，每个子数组的和都等于 $target$，且两个子数组长度之和最小。如果不存在，返回 $-1$。

**说明**：
- $1 \le arr.length \le 10^5$。
- 元素值均为正数。

**示例**：

- 示例 1：

```python
输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
```

- 示例 2：

```python
输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
```

## 解题思路

### 思路 1：前缀和 + 哈希 + 动态规划

#### 1. 核心思想

由于元素都是正数，可以用滑动窗口（或前缀和 + 哈希）找到每个位置结尾的和为 $target$ 的子数组长度。

用 $dp[i]$ 表示前 $i$ 个元素中，和为 $target$ 的子数组的最小长度。然后遍历到 $i$ 时，如果 $arr[j \dots i]$ 的和为 $target$，则候选答案为 $len + dp[j-1]$。

#### 2. 具体步骤

**第 1 步**：用前缀和 + 哈希表记录每个前缀和对应的最新位置。

**第 2 步**：遍历 $i$，维护 $dp[i]$ 表示前 $i$ 个元素中能得到的和为 $target$ 的最小子数组长度。

**第 3 步**：对于位置 $i$，检查是否存在 $j$ 使得 $prefix[i] - prefix[j] = target$（即 $prefix[j] = prefix[i] - target$）。如果存在，记 $len = i - j$，则 $ans = \min(ans, len + dp[j])$。同时 $dp[i] = \min(dp[i-1], len)$。

#### 3. 举例说明

以 $arr = [3,2,2,4,3], target = 3$ 为例：

滑动窗口：
- 位置 0：$[0,0]$ 和 $=3$，$len=1$
- 位置 4：$[3,4]$ 和 $=4+3=7$ 不是

前缀和 + DP：
- $prefix = [0,3,5,7,11,14]$
- 遍历：
  - $i=1$：$target=3$，$len=1$，$ans$ 无法配对（$dp[0]$ 无穷）
  - $i=4$：$prefix[4]-prefix[3]=4$，不是
  - ...

最终两个和为 $3$ 的子数组：$[0,0]$ 长度为 $1$，$[3,4]$ 不可能（和为 $7$）。实际上找不到第二个 → 返回 $-1$。

另一种情况：$arr = [1,2,1,2,1,2,1], target=3$：
- $[0,1]$ 长度 2，$[2,3]$ 长度 2 → 总 $4$

### 思路 1：代码

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        # dp[i] 表示前 i 个元素中，和为 target 的子数组的最小长度
        dp = [INF] * (n + 1)
        ans = INF
        prefix = 0
        sum_to_pos = {0: 0}  # 前缀和 -> 位置

        for i in range(1, n + 1):
            prefix += arr[i - 1]
            # 查找是否有位置 j 使得 arr[j+1...i] 的和为 target
            if prefix - target in sum_to_pos:
                j = sum_to_pos[prefix - target]
                length = i - j
                if dp[j] != INF:
                    ans = min(ans, length + dp[j])
                dp[i] = min(dp[i - 1], length)
            else:
                dp[i] = dp[i - 1]
            sum_to_pos[prefix] = i

        return -1 if ans == INF else ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，一次遍历。
- **空间复杂度**：$O(n)$，哈希表和 DP 数组。
