# [0398. 随机数索引](https://leetcode.cn/problems/random-pick-index/)

- 标签：水塘抽样、哈希表、数学、随机化
- 难度：中等

## 题目链接

- [0398. 随机数索引 - 力扣](https://leetcode.cn/problems/random-pick-index/)

## 题目大意

**描述**：

给定一个可能含有「重复元素」的整数数组 $nums$。

**要求**：

请你随机输出给定的目标数字 $target$ 的索引。你可以假设给定的数字一定存在于数组中。

实现 `Solution` 类：

- `Solution(int[] nums)` 用数组 $nums$ 初始化对象。
- `int pick(int target)` 从 $nums$ 中选出一个满足 $nums[i] == target$ 的随机索引 $i$。如果存在多个有效的索引，则每个索引的返回概率应当相等。

**说明**：

- $1 \le nums.length \le 2 \times 10^{4}$。
- $-2^{31} \le nums[i] \le 2^{31} - 1$。
- $target$ 是 $nums$ 中的一个整数。
- 最多调用 $pick$ 函数 $10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
输出
[null, 4, 0, 2]

解释
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
```

## 解题思路

### 思路 1：哈希表预处理

**算法思路**：

由于题目中 `pick` 函数会被频繁调用，如果每次调用都遍历整个数组，时间复杂度为 $O(n)$，在大量调用时会导致超时。我们可以使用哈希表预处理的方法来优化：

1. **预处理阶段**：在构造函数中，遍历数组 $nums$，将每个值对应的所有索引存储在哈希表中。
2. **查询阶段**：在 `pick` 函数中，直接从哈希表中获取目标值的所有索引，然后随机选择一个。

**具体实现**：

1. **初始化**：
   - 创建哈希表 $index\_map$，键为数组中的值，值为该值对应的所有索引列表。
   - 遍历数组 $nums$，将每个 $nums[i]$ 的索引 $i$ 添加到对应的列表中。

2. **随机选择**：
   - 从哈希表中获取 $target$ 对应的索引列表。
   - 使用 `random.choice()` 从列表中随机选择一个索引返回。

### 思路 1：代码

```python
import random
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        """预处理：构建值到索引列表的映射"""
        self.index_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        """从预处理的索引列表中随机选择一个"""
        return random.choice(self.index_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 构造函数：$O(n)$，其中 $n$ 是数组的长度。需要遍历数组一次构建哈希表。
  - `pick` 函数：$O(1)$，直接从哈希表中获取索引列表并随机选择。
- **空间复杂度**：$O(n)$，其中 $n$ 是数组的长度。哈希表最多存储 $n$ 个索引。