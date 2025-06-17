# [1296. 划分数组为连续数字的集合](https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/)

- 标签：贪心、数组、哈希表、排序
- 难度：中等

## 题目链接

- [1296. 划分数组为连续数字的集合 - 力扣](https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/)

## 题目大意

**描述**：给定一个整数数组 `nums` 和一个正整数 `k`。

**要求**：判断是否可以把这个数组划分成一些由 `k` 个连续数字组成的集合。如果可以，则返回 `True`；否则，返回 `False`。

**说明**：

- $1 \le k \le nums.length \le 10^5$。
- $1 \le nums[i] \le 10^9$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：True
解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
```

## 解题思路

### 思路 1：哈希表 + 排序

1. 使用哈希表存储每个数出现的次数。
2. 将哈希表中每个键从小到大排序。
3. 从哈希表中最小的数开始，以它作为当前连续数字的开头，然后依次判断连续的 `k` 个数是否在哈希表中，如果在的话，则将哈希表中对应数的数量减 `1`。不在的话，说明无法满足题目要求，直接返回 `False`。
4. 重复执行 2 ~ 3 步，直到哈希表为空。最后返回 `True`。

### 思路 1：哈希表 + 排序代码

```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        hand_map = collections.defaultdict(int)
        for i in range(len(nums)):
            hand_map[nums[i]] += 1
        for key in sorted(hand_map.keys()):
            value = hand_map[key]
            if value == 0:
                continue
            count = 0
            for i in range(k):
                hand_map[key + count] -= value
                if hand_map[key + count] < 0:
                    return False
                count += 1
        return True
```
