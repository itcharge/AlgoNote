# [1224. 最大相等频率](https://leetcode.cn/problems/maximum-equal-frequency/)

- 标签：数组、哈希表
- 难度：困难

## 题目链接

- [1224. 最大相等频率 - 力扣](https://leetcode.cn/problems/maximum-equal-frequency/)

## 题目大意

**描述**：给你一个正整数数组 $nums$。

**要求**：找出能满足下面要求的**最长前缀**，并返回该前缀的长度：从前缀中恰好删除一个元素后，剩下每个数字的出现次数都相同。如果删除这个元素后没有剩余元素，仍可认为每个数字都具有相同的出现次数（即 $0$ 次）。

**说明**：

- $2 \le nums.length \le 10^{5}$。
- $1 \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：nums = [2,2,1,1,5,3,3,5]
输出：7
解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，删除 nums[4] = 5，得到 [2,2,1,1,3,3]，每个数字出现两次。
```

- 示例 2：

```python
输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
输出：13
```

## 解题思路

### 思路 1：哈希表 + 频率计数

###### 1. 核心思想

我们需要在遍历数组的过程中，动态判断当前前缀是否满足「删除一个元素后，所有数字出现次数相同」。

为了做到这一点，需要维护两类信息：
1. **每个数字出现的次数** $freq[num]$。
2. **每种出现次数对应多少个数字** $count[freq]$。

同时记录当前出现的最大频率 $maxFreq$。

遍历每个元素后，检查当前前缀是否满足条件。满足条件的情况有三种：

**情况 1：所有数字都只出现 1 次（$maxFreq == 1$）**
此时删除任意一个元素后，剩下的每个数字出现 $0$ 或 $1$ 次，都可以视为相同。例如 $[1,2,3]$。

**情况 2：一个数字出现 $maxFreq$ 次，其他数字都出现 $maxFreq-1$ 次**
这意味着 $count[maxFreq] == 1$，并且出现 $maxFreq-1$ 次的数字个数乘以 $(maxFreq-1)$ 加上出现 $maxFreq$ 次的那个数，正好等于当前前缀长度。
即 $count[maxFreq-1] \times (maxFreq-1) + maxFreq == i+1$。
删除那个出现 $maxFreq$ 次的数字中的一个，就全部变成 $maxFreq-1$ 次。
例如 $[1,1,2,2,3]$：$1$ 出现 $2$ 次，$2$ 出现 $2$ 次，$3$ 出现 $1$ 次。$maxFreq=2$，$count[2]=2$，不满足。

等等让我重新想想条件。

实际上应该这样分析：

条件 1：所有元素都相同（或每种元素出现一次），即 $maxFreq == 1$。
这种情况下删除任意一个元素后，剩余元素出现的次数要么是 $0$（被删除的元素），要么是 $1$（其他元素）。因为「出现 $0$ 次」和「出现 $1$ 次」都可以视为「相同」，所以条件成立。

条件 2：只有一个数字出现 $maxFreq$ 次，其他数字都出现 $maxFreq-1$ 次。
即 $count[maxFreq] == 1$ 且 $count[maxFreq-1] \times (maxFreq-1) + maxFreq == 当前长度$。
这种情况删除那个出现 $maxFreq$ 次的数字中的一个，所有数字就变成 $maxFreq-1$ 次。
例如 $[1,1,2,2,3,3,4]$：$1,2,3$ 各 $2$ 次，$4$ 只有 $1$ 次。$maxFreq=2$，$count[2]=3$，不满足。 
再比如 $[1,1,2,2,3]$：$maxFreq=2$，$count[2]=2$，不满足（有两个数字出现 $2$ 次）。
$[1,1,1,2,2]$：$maxFreq=3$，$count[3]=1$，$count[2]=1$ → $1 \times 2 + 3 = 5$ → 成立。删除一个 $1$ 得 $[1,1,2,2]$。

条件 3：只有一个数字出现 $1$ 次，其他所有数字都出现 $maxFreq$ 次。
即 $count[1] == 1$ 且 $count[maxFreq] \times maxFreq + 1 == 当前长度$。
这种情况删除那个出现 $1$ 次的数字，所有数字就变成 $maxFreq$ 次。
例如 $[1,1,2,2,3]$：$maxFreq=2$，$count[2]=2$，$count[1]=1$ → $2 \times 2 + 1 = 5$ → 成立。

嗯，让我再想想。其实有更简洁的方式处理。

实际上条件有三种：
1. $maxFreq == 1$：所有元素都相同或每个元素只出现一次
2. $count[maxFreq] == 1$ 且 $count[maxFreq-1] \times (maxFreq-1) + maxFreq == 当前长度$
3. $count[maxFreq] \times maxFreq + 1 == 当前长度$（即只有一个数字出现 $1$ 次，其他都是 $maxFreq$ 次）

等等，条件 3 中 $count[maxFreq] \times maxFreq + 1$ 的含义是：所有出现 $maxFreq$ 次的元素加起来，再加上出现 $1$ 次的那个元素。

再想想，其实条件 3 中还有一个隐含条件：那个"出现 $1$ 次"的数字，其实就是 $count[1]$ 代表的元素之一。所以条件 3 等价于：
$count[1] == 1$ 且 $count[maxFreq] \times maxFreq + 1 == 当前长度$

好了，让我把这个写进题解中。

###### 2. 具体步骤

**第 1 步**：初始化 $freq$（数字 → 出现次数）、$count$（出现次数 → 数字个数）、$maxFreq$（当前最大频率）、$ans$（结果）。

**第 2 步**：遍历数组，对每个元素：
- 更新 $freq$：旧频率减 $1$，新频率加 $1$。
- 更新 $count$。
- 更新 $maxFreq$。
- 检查是否满足条件，满足则更新 $ans$。

**第 3 步**：返回 $ans$。

### 思路 1：代码

```python
from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq = defaultdict(int)    # 数字 -> 出现次数
        count = defaultdict(int)   # 出现次数 -> 数字个数
        maxFreq = 0
        ans = 0

        for i, num in enumerate(nums):
            # 更新频率统计
            if freq[num] > 0:
                count[freq[num]] -= 1
            freq[num] += 1
            count[freq[num]] += 1
            maxFreq = max(maxFreq, freq[num])

            # 检查当前前缀是否有效
            length = i + 1
            if (maxFreq == 1 or
                count[maxFreq] == 1 and count[maxFreq - 1] * (maxFreq - 1) + maxFreq == length or
                count[maxFreq] * maxFreq + 1 == length):
                ans = length

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $nums$ 的长度。只需一次遍历，每次进行常数次哈希表操作。
- **空间复杂度**：$O(n)$，需要两个哈希表存储频率和计数信息。
