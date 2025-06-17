# [LCR 191. 按规则计算统计结果](https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/)

- 标签：数组、前缀和
- 难度：中等

## 题目链接

- [LCR 191. 按规则计算统计结果 - 力扣](https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof/)

## 题目大意

给定一个数组 `A`。

要求：构建一个数组 `B`，其中 `B[i]` 为数组 `A` 中除了 `A[i]` 之外的其他所有元素乘积。

要求不能使用除法。

## 解题思路

构造一个答案数组 `B`，长度和数组 `A` 长度一致。先从左到右遍历一遍 `A` 数组，将 `A[i]` 左侧的元素乘积累积起来，存储到 `B` 数组中。再从右到左遍历一遍，将 `A[i]` 右侧的元素乘积累积起来，再乘以原本 `B[i]` 的值，即为 `A` 中除了 `A[i]` 之外的其他所有元素乘积。

## 代码

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        size = len(a)
        b = [1 for _ in range(size)]

        left = 1
        for i in range(size):
            b[i] *= left
            left *= a[i]

        right = 1
        for i in range(size - 1, -1, -1):
            b[i] *= right
            right *= a[i]
        return b
```

