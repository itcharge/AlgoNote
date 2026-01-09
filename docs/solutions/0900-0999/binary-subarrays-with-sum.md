# [0930. 和相同的二元子数组](https://leetcode.cn/problems/binary-subarrays-with-sum/)

- 标签：数组、哈希表、前缀和、滑动窗口
- 难度：中等

## 题目链接

- [0930. 和相同的二元子数组 - 力扣](https://leetcode.cn/problems/binary-subarrays-with-sum/)

## 题目大意

**描述**：

给定一个二元数组 $nums$，和一个整数 $goal$。

**要求**：

请你统计并返回有多少个和为 $goal$ 的「非空」子数组。

**说明**：

- 「子数组」是数组的一段连续部分。
- $1 \le nums.length \le 3 * 10^{4}$。
- $nums[i]$ 不是 0 就是 1。
- $0 \le goal \le nums.length$。

**示例**：

- 示例 1：

```python
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
```

- 示例 2：

```python
输入：nums = [0,0,0,0,0], goal = 0
输出：15
```

## 解题思路

### 思路 1：前缀和 + 哈希表

#### 思路

这道题要求统计和为 $goal$ 的非空子数组数量。我们可以使用前缀和的思想：

1. **前缀和**：定义 $preSum[i]$ 为数组前 $i$ 个元素的和。
2. **子数组和**：子数组 $[i, j]$ 的和为 $preSum[j] - preSum[i - 1]$。
3. **转化问题**：要找满足 $preSum[j] - preSum[i - 1] = goal$ 的 $(i, j)$ 对数，即找满足 $preSum[i - 1] = preSum[j] - goal$ 的数量。
4. **哈希表优化**：使用哈希表 $count$ 记录每个前缀和出现的次数，遍历数组时：
   - 如果 $preSum - goal$ 在哈希表中，说明存在以当前位置为结尾、和为 $goal$ 的子数组，累加对应的次数。
   - 将当前前缀和加入哈希表。

#### 代码

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        
        # 哈希表记录前缀和出现的次数
        count = defaultdict(int)
        count[0] = 1  # 前缀和为 0 的情况，初始化为 1
        
        preSum = 0  # 当前前缀和
        res = 0  # 结果
        
        for num in nums:
            preSum += num
            # 如果 preSum - goal 存在，说明存在和为 goal 的子数组
            if preSum - goal in count:
                res += count[preSum - goal]
            # 记录当前前缀和
            count[preSum] += 1
        
        return res
```

#### 复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。只需要遍历一次数组。
- **空间复杂度**：$O(n)$，哈希表最多存储 $n$ 个不同的前缀和。
