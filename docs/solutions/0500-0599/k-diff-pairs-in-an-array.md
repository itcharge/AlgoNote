# [0532. 数组中的 k-diff 数对](https://leetcode.cn/problems/k-diff-pairs-in-an-array/)

- 标签：数组、哈希表、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [0532. 数组中的 k-diff 数对 - 力扣](https://leetcode.cn/problems/k-diff-pairs-in-an-array/)

## 题目大意

**描述**：

给定一个整数数组 $nums$ 和一个整数 $k$。

**要求**：

请你在数组中找出 不同的 $k - diff$ 数对，并返回不同的 $k - diff$ 数对的数目。

**说明**：

- $k - diff$ 数对定义为一个整数对 ($nums[i], nums[j]$) ，并满足下述全部条件：
   - $0 \le i, j < nums.length$
   - $i \ne j$
   - $|nums[i] - nums[j]| == k$
- 注意，$|val|$ 表示 $val$ 的绝对值。
- $1 \le nums.length \le 10^{4}$。
- $-10^{7} \le nums[i] \le 10^{7}$。
- $0 \le k \le 10^{7}$。

**示例**：

- 示例 1：

```python
输入：nums = [3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
```

- 示例 2：

```python
输入：nums = [1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
```

## 解题思路

### 思路 1：哈希表

对于 $k-diff$ 数对，需要满足 $|nums[i] - nums[j]| = k$，即 $nums[i] = nums[j] + k$ 或 $nums[i] = nums[j] - k$。

使用哈希表统计每个数字出现的次数。对于每个数字 $num$：
- 如果 $k = 0$，需要 $num$ 出现至少 2 次才能形成数对
- 如果 $k > 0$，检查 $num + k$ 是否存在（避免重复，只检查 $num + k$）

使用集合记录已经处理过的数对，避免重复计数。

### 思路 1：代码

```python
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        result = 0
        
        if k == 0:
            # k = 0 时，需要数字出现至少 2 次
            for num, cnt in count.items():
                if cnt >= 2:
                    result += 1
        else:
            # k > 0 时，检查 num + k 是否存在
            for num in count:
                if num + k in count:
                    result += 1
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度，需要遍历数组统计频率，然后遍历哈希表。
- **空间复杂度**：$O(n)$，哈希表最多存储 $n$ 个不同的数字。
