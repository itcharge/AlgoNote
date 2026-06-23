# [1437. 是否所有 1 都至少相隔 k 个元素](https://leetcode.cn/problems/check-if-all-1s-are-at-least-length-k-places-away/)

- 标签：数组
- 难度：简单

## 题目链接

- [1437. 是否所有 1 都至少相隔 k 个元素 - 力扣](https://leetcode.cn/problems/check-if-all-1s-are-at-least-length-k-places-away/)

## 题目大意

**描述**：给定一个由 $0$ 和 $1$ 组成的数组 $nums$ 和一个整数 $k$。

**要求**：检查数组中任意两个 $1$ 之间是否至少相隔 $k$ 个元素（即位置差的绝对值 $> k$）。如果所有相邻的 $1$ 之间都满足条件，返回 $True$，否则 $False$。

**说明**：
- $1 \le nums.length \le 10^5$。
- $0 \le k \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png)

```python
输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png)

```python
输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。
```

## 解题思路

### 思路 1：一次遍历

#### 1. 核心思想

遍历数组，记录上一个 $1$ 出现的位置。当遇到新的 $1$ 时，检查与上一个 $1$ 的距离是否 $\le k$。

#### 2. 具体步骤

**第 1 步**：初始化 $prev = -1$（表示尚未遇到 $1$）。

**第 2 步**：遍历 $i = 0 \to n-1$：

- 如果 $nums[i] == 1$：
  - 如果 $prev \ne -1$ 且 $i - prev - 1 < k$，返回 $False$。
  - 更新 $prev = i$。

**第 3 步**：遍历完成，返回 $True$。

注意：题目要求相隔 $k$ 个元素，即 $i - prev > k$ 等价于 $i - prev - 1 \ge k$。

#### 3. 举例说明

以 $nums = [1,0,0,0,1,0,0,1], k = 2$ 为例：

- $prev = -1$
- $i=0, nums=1: prev=-1$，更新 $prev=0$
- $i=4, nums=1: diff=4-0-1=3 \ge 2$ ✓，更新 $prev=4$
- $i=7, nums=1: diff=7-4-1=2 \ge 2$ ✓，更新 $prev=7$

返回 $True$。

### 思路 1：代码

```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for i, num in enumerate(nums):
            if num == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，一次遍历。
- **空间复杂度**：$O(1)$。
