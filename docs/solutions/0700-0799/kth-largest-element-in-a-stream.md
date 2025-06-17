# [0703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)

- 标签：树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）
- 难度：简单

## 题目链接

- [0703. 数据流中的第 K 大元素 - 力扣](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)

## 题目大意

**要求**：设计一个 KthLargest 类，用于找到数据流中第 $k$ 大元素。

实现 KthLargest 类：

- `KthLargest(int k, int[] nums)`：使用整数 $k$ 和整数流 $nums$ 初始化对象。
- `int add(int val)`：将 $val$ 插入数据流 $nums$ 后，返回当前数据流中第 $k$ 大的元素。

**说明**：

- $1 \le k \le 10^4$。
- $0 \le nums.length \le 10^4$。
- $-10^4 \le nums[i] \le 10^4$。
- $-10^4 \le val \le 10^4$。
- 最多调用 `add` 方法 $10^4$ 次。
- 题目数据保证，在查找第 $k$ 大元素时，数组中至少有 $k$ 个元素。

**示例**：

- 示例 1：

```python
输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

## 解题思路

### 思路 1：堆

1. 建立大小为 $k$ 的大顶堆，堆中元素保证不超过 $k$ 个。
2. 每次 `add` 操作时，将新元素压入堆中，如果堆中元素超出了 $k$ 个，则将堆中最小元素（堆顶）移除。

- 此时堆中最小元素（堆顶）就是整个数据流中的第 $k$ 大元素。

### 思路 1：代码

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

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化时间复杂度：$O(n \times \log k)$，其中 $n$ 为 $nums$ 初始化时的元素个数。
  - 单次插入时间复杂度：$O(\log k)$。
- **空间复杂度**：$O(k)$。

