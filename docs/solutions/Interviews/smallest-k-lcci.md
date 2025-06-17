# [面试题 17.14. 最小K个数](https://leetcode.cn/problems/smallest-k-lcci/)

- 标签：数组、分治、快速选择、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [面试题 17.14. 最小K个数 - 力扣](https://leetcode.cn/problems/smallest-k-lcci/)

## 题目大意

给定整数数组 `arr`，再给定一个整数 `k`。

要求：返回数组 `arr` 中最小的 `k` 个数。

## 解题思路

直接可以想到的思路是：排序后输出数组上对应的最小的 k 个数。所以问题关键在于排序方法的复杂度。

冒泡排序、选择排序、插入排序时间复杂度 $O(n^2)$ 太高了，解答会超时。

可考虑堆排序、归并排序、快速排序。本题使用堆排序。具体做法如下：

1. 利用数组前 `k` 个元素，建立大小为 `k` 的大顶堆。
2. 遍历数组 `[k, size - 1]` 的元素，判断其与堆顶元素关系，如果比堆顶元素小，则将其赋值给堆顶元素，再对大顶堆进行调整。
3. 最后输出前调整过后的大顶堆的前 `k` 个元素。

## 代码

```python
class Solution:
    def heapify(self, nums: [int], index: int, end: int):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子节点
            max_index = index
            if nums[left] > nums[max_index]:
                max_index = left
            if right <= end and nums[right] > nums[max_index]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 初始化大顶堆
    def buildMaxHeap(self, nums: [int], k: int):
        # (k-2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((k - 2) // 2, -1, -1):
            self.heapify(nums, i, k - 1)
        return nums

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        size = len(arr)
        if k <= 0 or not arr:
            return []
        if size <= k:
            return arr

        self.buildMaxHeap(arr, k)
        for i in range(k, size):
            if arr[i] < arr[0]:
                arr[i], arr[0] = arr[0], arr[i]
                self.heapify(arr, 0, k - 1)

        return arr[:k]
```

