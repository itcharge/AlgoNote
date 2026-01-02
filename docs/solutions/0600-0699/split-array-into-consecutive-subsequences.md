# [0659. 分割数组为连续子序列](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/)

- 标签：贪心、数组、哈希表、堆（优先队列）
- 难度：中等

## 题目链接

- [0659. 分割数组为连续子序列 - 力扣](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/)

## 题目大意

**描述**：

给定一个按「非递减顺序」排列的整数数组 $nums$。

**要求**：

判断是否能在将 $nums$ 分割成 一个或多个子序列 的同时满足下述两个条件：

- 每个子序列都是一个「连续递增序列」（即，每个整数「恰好」比前一个整数大 $1$）。
- 所有子序列的长度「至少」为 $3$。

如果可以分割 $nums$ 并满足上述条件，则返回 true ；否则，返回 false。

**说明**：

- $1 \le nums.length \le 10^{4}$。
- $-10^{3} \le nums[i] \le 10^{3}$。
- $nums$ 按非递减顺序排列。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,3,4,5]
输出：true
解释：nums 可以分割成以下子序列：
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
```

- 示例 2：

```python
输入：nums = [1,2,3,3,4,4,5,5]
输出：true
解释：nums 可以分割成以下子序列：
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
```

## 解题思路

### 思路 1：贪心 + 哈希表

这道题目要求将数组分割成若干个长度至少为 3 的连续递增子序列。使用贪心策略：优先将当前数字接到已有的子序列后面，如果不能接到已有子序列，则尝试创建新的子序列。

1. 使用哈希表 $freq$ 记录每个数字的剩余可用次数。
2. 使用哈希表 $need$ 记录以某个数字结尾的子序列需要的下一个数字的数量。
3. 遍历数组中的每个数字 $num$：
   - 如果 $freq[num] = 0$，说明该数字已经被使用完，跳过。
   - 如果 $need[num] > 0$，说明存在以 $num - 1$ 结尾的子序列需要 $num$，将 $num$ 接到该子序列后面：
     - $need[num]$ 减 1，$freq[num]$ 减 1。
     - $need[num + 1]$ 加 1（该子序列现在需要 $num + 1$）。
   - 否则，尝试创建新的子序列 $[num, num + 1, num + 2]$：
     - 检查 $freq[num + 1]$ 和 $freq[num + 2]$ 是否大于 0。
     - 如果可以创建，将这三个数字的频率减 1，并将 $need[num + 3]$ 加 1。
     - 如果不能创建，返回 $False$。
4. 如果所有数字都能成功分配，返回 $True$。

### 思路 1：代码

```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import defaultdict
        
        freq = defaultdict(int)  # 记录每个数字的剩余可用次数
        need = defaultdict(int)  # 记录以某个数字结尾的子序列需要的下一个数字的数量
        
        # 统计每个数字的频率
        for num in nums:
            freq[num] += 1
        
        for num in nums:
            if freq[num] == 0:
                continue
            
            # 优先将 num 接到已有的子序列后面
            if need[num] > 0:
                need[num] -= 1
                freq[num] -= 1
                need[num + 1] += 1
            # 尝试创建新的子序列 [num, num+1, num+2]
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            else:
                # 无法分配当前数字
                return False
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组的长度。需要遍历数组两次。
- **空间复杂度**：$O(n)$，需要使用两个哈希表存储频率和需求信息。
