# [0846. 一手顺子](https://leetcode.cn/problems/hand-of-straights/)

- 标签：贪心、数组、哈希表、排序
- 难度：中等

## 题目链接

- [0846. 一手顺子 - 力扣](https://leetcode.cn/problems/hand-of-straights/)

## 题目大意

**描述**：`Alice` 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌都是顺子（即由连续的牌构成），并且每一组的牌数都是 `groupSize`。现在给定一个整数数组 `hand`，其中 `hand[i]` 是表示第 `i` 张牌的数值，和一个整数 `groupSize`。

**要求**：如果 `Alice` 能将这些牌重新排列成若干组、并且每组都是 `goupSize` 张牌的顺子，则返回 `True`；否则，返回 `False`。

**说明**：

- $1 \le hand.length \le 10^4$。
- $0 \le hand[i] \le 10^9$。
- $1 \le groupSize \le hand.length$。

**示例**：

- 示例 1：

```python
输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：True
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
```

## 解题思路

### 思路 1：哈希表 + 排序

1. 使用哈希表存储每个数出现的次数。
2. 将哈希表中每个键从小到大排序。
3. 从哈希表中最小的数开始，以它作为当前顺子的开头，然后依次判断顺子里的数是否在哈希表中，如果在的话，则将哈希表中对应数的数量减 `1`。不在的话，说明无法满足题目要求，直接返回 `False`。
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
