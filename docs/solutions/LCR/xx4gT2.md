# [LCR 076. 数组中的第 K 个最大元素](https://leetcode.cn/problems/xx4gT2/)

- 标签：数组、分治、快速选择、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [LCR 076. 数组中的第 K 个最大元素 - 力扣](https://leetcode.cn/problems/xx4gT2/)

## 题目大意

给定一个未排序的数组 `nums`，从中找到第 `k` 个最大的数字。

## 解题思路

很不错的一道题，面试常考。

直接可以想到的思路是：排序后输出数组上对应第 k 位大的数。所以问题关键在于排序方法的复杂度。

冒泡排序、选择排序、插入排序时间复杂度 $O(n^2)$ 太高了，解答会超时。

可考虑堆排序、归并排序、快速排序。

这道题的要求是找到第 k 大的元素，使用归并排序只有到最后排序完毕才能返回第 k 大的数。而堆排序每次排序之后，就会确定一个元素的准确排名，同理快速排序也是如此。

### 1. 堆排序

升序堆排序的思路如下：

1. 先建立大顶堆

2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值

3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值

4. 以此类推，直到最后一个元素交换之后完毕。

这道题我们只需进行 1 次建立大顶堆， k-1 次调整即可得到第 k 大的数。

时间复杂度：$O(n^2)$

### 2. 快速排序

快速排序每次调整，都会确定一个元素的最终位置，且以该元素为界限，将数组分成了两个数组，前一个数组元素都比该元素小，后一个元素都比该元素大。

这样，只要某次划分的元素恰好是第 k 个下标就找到了答案。并且我们只需关注 k 元素所在区间的排序情况，与 k 元素无关的区间排序都可以忽略。这样进一步减少了执行步骤。

### 3. 借用标准库（不建议）

提交代码中的最快代码是调用了 Python 的 heapq 库，或者 sort 方法。
这样的确可以通过，但是不建议这样做。借用标准库实现，只能说对这个库的 API 和相关数据结构的用途相对熟悉，而不代表着掌握了这个数据结构。可以问问自己，如果换一种语言，自己还能不能实现对应的数据结构？刷题的本质目的是为了把算法学会学透，而不仅仅是调 API。

## 代码

1. 堆排序

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 调整为大顶堆
        def heapify(nums, index, end):
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
        def buildMaxHeap(nums):
            size = len(nums)
            # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
            for i in range((size - 2) // 2, -1, -1):
                heapify(nums, i, size - 1)
            return nums

        buildMaxHeap(nums)
        size = len(nums)
        for i in range(k-1):
            nums[0], nums[size-i-1] = nums[size-i-1], nums[0]
            heapify(nums, 0, size-i-2)
        return nums[0]
```

2. 快速排序

```python
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def randomPartition(nums, low, high):
            i = random.randint(low, high)
            nums[i], nums[high] = nums[high], nums[i]
            return partition(nums, low, high)

        def partition(nums, low, high):
            x = nums[high]
            i = low-1
            for j in range(low, high):
                if nums[j] <= nums[high]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1

        def quickSort(nums, low, high, k):
            n = len(nums)
            if low < high:
                pi = randomPartition(nums, low, high)
                if pi == n-k:
                    return nums[len(nums)-k]
                if pi > n-k:
                    quickSort(nums, low, pi-1, k)
                if pi < n-k:
                    quickSort(nums, pi+1, high, k)

            return nums[len(nums)-k]

        return quickSort(nums, 0, len(nums)-1, k)
```

3. 借用标准库

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
```

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for n in nums:
            if len(res) < k:
                heapq.heappush(res, n)
            elif n > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, n)
        return heapq.heappop(res)
```



