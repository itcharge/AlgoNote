# [LCR 119. 最长连续序列](https://leetcode.cn/problems/WhsWhI/)

- 标签：并查集、数组、哈希表
- 难度：中等

## 题目链接

- [LCR 119. 最长连续序列 - 力扣](https://leetcode.cn/problems/WhsWhI/)

## 题目大意

给定一个未排序的整数数组 `nums`。

要求：找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。并且要用时间复杂度为 $O(n)$ 的算法解决此问题。

## 解题思路

暴力做法有两种思路。第 1 种思路是先排序再依次判断，这种做法时间复杂度最少是 $O(n \log n)$。第 2 种思路是枚举数组中的每个数 `num`，考虑以其为起点，不断尝试匹配 `num + 1`、`num + 2`、`...` 是否存在，最长匹配次数为 `len(nums)`。这样下来时间复杂度为 $O(n^2)$。但是可以使用集合或哈希表优化这个步骤。

- 先将数组存储到集合中进行去重，然后使用 `curr_streak` 维护当前连续序列长度，使用 `ans` 维护最长连续序列长度。
- 遍历集合中的元素，对每个元素进行判断，如果该元素不是序列的开始（即 `num - 1` 在集合中），则跳过。
- 如果 `num - 1` 不在集合中，说明 `num` 是序列的开始，判断 `num + 1` 、`nums + 2`、`...` 是否在哈希表中，并不断更新当前连续序列长度 `curr_streak`。并在遍历结束之后更新最长序列的长度。
- 最后输出最长序列长度。

将数组存储到集合中进行去重的操作的时间复杂度是 $O(n)$。查询每个数是否在集合中的时间复杂度是 $O(1)$ ，并且跳过了所有不是起点的元素。更新当前连续序列长度 `curr_streak` 的时间复杂度是 $O(n)$，所以最终的时间复杂度是 $O(n)$。符合题意要求。

## 代码

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                ans = max(ans, curr_streak)

        return ans
```

