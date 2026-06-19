# [1187. 使数组严格递增](https://leetcode.cn/problems/make-array-strictly-increasing/)

- 标签：数组、二分查找、动态规划、排序
- 难度：困难

## 题目链接

- [1187. 使数组严格递增 - 力扣](https://leetcode.cn/problems/make-array-strictly-increasing/)

## 题目大意

**描述**：给定两个整数数组 $arr1$ 和 $arr2$。每次操作可以从 $arr2$ 中选一个数替换 $arr1$ 中的某个数。

**要求**：使 $arr1$ 变成严格递增（每个数都比前一个数大）所需的最小操作次数。如果做不到，返回 $-1$。

**说明**：

- $1 \le arr1.length, arr2.length \le 2000$。
- $0 \le arr1[i], arr2[i] \le 10^9$。

**示例**：

```python
输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 替换 5，得到 [1,2,3,6,7]。
```

## 解题思路

### 思路 1：动态规划 + 二分查找

这道题的难点在于每次替换时要选 $arr2$ 中合适的数，而 $arr2$ 很长，不能暴力一个个去试。

**核心思路**：用字典 $dp$ 记录状态，$dp[val]$ 表示「当前位置的值是 $val$ 时，所需的最小操作次数」。然后从前往后逐个位置处理，每个位置有两种选择：

1. **不替换**：保留 $arr1[i]$。要求它比前一个位置的终值大。
2. **替换**：从 $arr2$ 中选一个比前一个位置的终值大的最小数来替换。操作次数加 1。

**步骤拆解：**

1. 对 $arr2$ 排序去重，方便二分查找。
2. 初始化 $dp = \{-1: 0\}$，表示位置 -1（虚拟位置）值为 -1，操作 0 次。
3. 遍历 $arr1$ 的每个数字：
   - 对于 $dp$ 中的每个状态 $(\text{前一个值}, \text{操作次数})$：
     - **不替换：** 如果当前数字 > 前一个值，可以保留。
     - **替换：** 在 $arr2$ 中二分查找第一个比前一个值大的数来替换。
   - 更新 $dp$。
4. 如果最后 $dp$ 不为空，返回最小操作次数；否则返回 $-1$。

**为什么用二分查找？** 因为 $arr2$ 排好序后，找「第一个大于 $x$ 的数」只需要 $\log n$ 时间。

### 思路 1：代码

```python
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        import bisect
        
        # 对 arr2 排序并去重，方便二分查找
        arr2 = sorted(set(arr2))
        
        # dp[val] 表示当前位置值为 val 时的最小操作次数
        dp = {-1: 0}
        
        for num in arr1:
            new_dp = {}
            
            for prev_val, ops in dp.items():
                # 选择 1：不替换当前值
                if num > prev_val:
                    new_dp[num] = min(new_dp.get(num, float('inf')), ops)
                
                # 选择 2：从 arr2 中找一个比 prev_val 大的最小数来替换
                idx = bisect.bisect_right(arr2, prev_val)
                if idx < len(arr2):
                    new_val = arr2[idx]
                    new_dp[new_val] = min(new_dp.get(new_val, float('inf')), ops + 1)
            
            dp = new_dp
            if not dp:  # 当前没有可行的状态
                return -1
        
        return min(dp.values())
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m \log m)$。$n$ 是 $arr1$ 长度，$m$ 是 $arr2$ 去重后的长度。每个位置都可能处理多个状态。
- **空间复杂度**：$O(m)$。状态字典最多存 $m$ 个不同的值。
