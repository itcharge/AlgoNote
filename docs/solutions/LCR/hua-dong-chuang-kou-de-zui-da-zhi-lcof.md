# [LCR 183. 望远镜中最高的海拔](https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)

- 标签：队列、滑动窗口、单调队列、堆（优先队列）
- 难度：困难

## 题目链接

- [LCR 183. 望远镜中最高的海拔 - 力扣](https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/)

## 题目大意

给定一个整数数组 `nums` 和滑动窗口的大小 `k`。表示为大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。我们只能看到滑动窗口内的 `k` 个数字，滑动窗口每次只能向右移动一位。

要求：返回滑动窗口中的最大值。

## 解题思路

暴力求解的话，二重循环，时间复杂度为 $O(n * k)$。

我们可以使用优先队列，每次窗口移动时想优先队列中增加一个节点，并删除一个节点。将窗口中的最大值加入到答案数组中。

## 代码

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return []

        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]

        for i in range(k, size):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res
```

