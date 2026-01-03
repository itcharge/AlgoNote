# [0798. 得分最高的最小轮调](https://leetcode.cn/problems/smallest-rotation-with-highest-score/)

- 标签：数组、前缀和
- 难度：困难

## 题目链接

- [0798. 得分最高的最小轮调 - 力扣](https://leetcode.cn/problems/smallest-rotation-with-highest-score/)

## 题目大意

**描述**：

给定一个数组 $nums$，我们可以将它按一个非负整数 $k$ 进行轮调，这样可以使数组变为 $[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]$ 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

- 例如，数组为 $nums = [2,4,1,3,0]$，我们按 $k = 2$ 进行轮调后，它将变成 $[1,3,0,2,4]$。这将记为 $3$ 分，因为 $1 > 0$ [不计分]、$3 > 1$ [不计分]、$0 \le 2$ [计 $1$ 分]、$2 \le 3$ [计 $1$ 分]，$4 \le 4$ [计 $1$ 分]。

**要求**：

在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 $k$。如果有多个答案，返回满足条件的最小的下标 $k$ 。

**说明**：

- $1 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \lt nums.length$。

**示例**：

- 示例 1：

```python
输入：nums = [2,3,1,4,0]
输出：3
解释：
下面列出了每个 k 的得分：
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
所以我们应当选择 k = 3，得分最高。
```

- 示例 2：

```python
输入：nums = [1,3,0,2,4]
输出：0
解释：
nums 无论怎么变化总是有 3 分。
所以我们将选择最小的 k，即 0。
```

## 解题思路

### 思路 1：差分数组

对于每次轮调 $k$，计算得分的变化。使用差分数组优化。

**分析**：

- 对于元素 $nums[i]$，在哪些轮调 $k$ 下能得分？
- 轮调 $k$ 后，$nums[i]$ 移动到位置 $(i - k + n) \% n$。
- 要得分，需要 $nums[i] \le (i - k + n) \% n$。

**计算得分区间**：

- 对于 $nums[i]$，它在轮调 $k$ 时能得分的条件是：
  - 如果 $i \ge nums[i]$：在 $k \in [0, i - nums[i]]$ 和 $k \in [i + 1, n - 1]$ 时得分。
  - 如果 $i < nums[i]$：在 $k \in [i + 1, n - 1 - (nums[i] - i - 1)]$ 时得分（如果该区间有效）。

使用差分数组记录每个 $k$ 的得分变化。

### 思路 1：代码

```python
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * n  # 差分数组
        
        for i in range(n):
            # 计算 nums[i] 不能得分的区间
            # nums[i] 在位置 j 时，如果 nums[i] > j，则不能得分
            # 轮调 k 后，nums[i] 在位置 (i - k + n) % n
            # 不能得分的条件：nums[i] > (i - k + n) % n
            
            # 简化：nums[i] 不能得分的轮调区间为 [(i - nums[i] + 1 + n) % n, i]
            # 使用差分数组标记不能得分的区间
            left = (i - nums[i] + 1 + n) % n
            right = i
            
            if left <= right:
                diff[left] -= 1
                if right + 1 < n:
                    diff[right + 1] += 1
            else:
                # 区间跨越了边界
                diff[0] -= 1
                if right + 1 < n:
                    diff[right + 1] += 1
                diff[left] -= 1
        
        # 计算每个 k 的得分
        max_score = 0
        current_score = n  # 初始得分为 n（假设所有元素都得分）
        result = 0
        
        for k in range(n):
            current_score += diff[k]
            if current_score > max_score:
                max_score = current_score
                result = k
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。
- **空间复杂度**：$O(n)$，差分数组的空间。
