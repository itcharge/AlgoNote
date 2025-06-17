# [0973. 最接近原点的 K 个点](https://leetcode.cn/problems/k-closest-points-to-origin/)

- 标签：几何、数组、数学、分治、快速选择、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0973. 最接近原点的 K 个点 - 力扣](https://leetcode.cn/problems/k-closest-points-to-origin/)

## 题目大意

给定一个由由平面上的点组成的列表 `points`，再给定一个整数 `K`。

要求：从中找出 `K` 个距离原点` (0, 0)` 最近的点。（这里，平面上两点之间的距离是欧几里德距离。）可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

## 解题思路

1. 使用二叉堆构建优先队列，优先级为距离原点的距离。此时堆顶元素即为距离原点最近的元素。
2. 将堆顶元素加入到答案数组中，进行出队操作。时间复杂度 $O(log{n})$。
   - 出队操作：交换堆顶元素与末尾元素，将末尾元素已移出堆。继续调整大顶堆。
3. 不断重复第 2 步，直到 `K` 次结束。

## 代码

```python
class Heapq:
    def compare(self, a, b):
        dist_a = a[0] * a[0] + a[1] * a[1]
        dist_b = b[0] * b[0] + b[1] * b[1]
        if dist_a < dist_b:
            return -1
        elif dist_a == dist_b:
            return 0
        else:
            return 1
    # 堆调整方法：调整为小顶堆
    def heapAdjust(self, nums: [int], index: int, end: int):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子结点
            max_index = index
            if self.compare(nums[left], nums[max_index]) == -1:
                max_index = left
            if right <= end and self.compare(nums[right], nums[max_index]) == -1:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 将数组构建为二叉堆
    def heapify(self, nums: [int]):
        size = len(nums)
        # (size - 2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            # 调用调整堆函数
            self.heapAdjust(nums, i, size - 1)

    # 入队操作
    def heappush(self, nums: list, value):
        nums.append(value)
        size = len(nums)
        i = size - 1
        # 寻找插入位置
        while (i - 1) // 2 >= 0:
            cur_root = (i - 1) // 2
            # value 大于当前根节点，则插入到当前位置
            if self.compare(nums[cur_root], value) == -1:
                break
            # 继续向上查找
            nums[i] = nums[cur_root]
            i = cur_root
        # 找到插入位置或者到达根位置，将其插入
        nums[i] = value

    # 出队操作
    def heappop(self, nums: list) -> int:
        size = len(nums)
        nums[0], nums[-1] = nums[-1], nums[0]
        # 得到最小值（堆顶元素）然后调整堆
        top = nums.pop()
        if size > 0:
            self.heapAdjust(nums, 0, size - 2)

        return top

    # 升序堆排序
    def heapSort(self, nums: [int]):
        self.heapify(nums)
        size = len(nums)
        for i in range(size):
            nums[0], nums[size - i - 1] = nums[size - i - 1], nums[0]
            self.heapAdjust(nums, 0, size - i - 2)
        return nums

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heapq()
        queue = []
        for point in points:
            heap.heappush(queue, point)

        res = []
        for i in range(k):
            res.append(heap.heappop(queue))

        return res
```

