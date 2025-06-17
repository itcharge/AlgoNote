# [LCR 059. 数据流中的第 K 大元素](https://leetcode.cn/problems/jBjn9C/)

- 标签：树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）
- 难度：简单

## 题目链接

- [LCR 059. 数据流中的第 K 大元素 - 力扣](https://leetcode.cn/problems/jBjn9C/)

## 题目大意

设计一个 ` KthLargest` 类，用于找到数据流中第 `k` 大元素。

- `KthLargest(int k, int[] nums)`：使用整数 `k` 和整数流 `nums` 初始化对象。
- `int add(int val)`：将 `val` 插入数据流 `nums` 后，返回当前数据流中第 `k` 大的元素。

## 解题思路

- 建立大小为 `k` 的大顶堆，堆中元素保证不超过 k 个。
- 每次 `add` 操作时，将新元素压入堆中，如果堆中元素超出了 `k` 个，则将堆中最小元素（堆顶）移除。
- 此时堆中最小元素（堆顶）就是整个数据流中的第 `k` 大元素。

## 代码

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
```

