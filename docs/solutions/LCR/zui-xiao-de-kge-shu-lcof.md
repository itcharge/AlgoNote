# [LCR 159. 库存管理 III](https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/)

- 标签：数组、分治、快速选择、排序、堆（优先队列）
- 难度：简单

## 题目链接

- [LCR 159. 库存管理 III - 力扣](https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/)

## 题目大意

**描述**：给定整数数组 $arr$，再给定一个整数 $k$。

**要求**：返回数组 $arr$ 中最小的 $k$ 个数。

**说明**：

- $0 \le k \le arr.length \le 10000$。
- $0 \le arr[i] \le 10000$。

**示例**：

- 示例 1：

```python
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
```

- 示例 2：

```python
输入：arr = [0,1,2,1], k = 1
输出：[0]
```

## 解题思路

直接可以想到的思路是：排序后输出数组上对应的最小的 k 个数。所以问题关键在于排序方法的复杂度。

冒泡排序、选择排序、插入排序时间复杂度 $O(n^2)$ 太高了，解答会超时。

可考虑堆排序、归并排序、快速排序。

### 思路 1：堆排序（基于大顶堆）

具体做法如下：

1. 使用数组前 $k$ 个元素，维护一个大小为 $k$ 的大顶堆。
2. 遍历数组 $[k, size - 1]$ 的元素，判断其与堆顶元素关系，如果遇到比堆顶元素小的元素，则将与堆顶元素进行交换。再将这 $k$ 个元素调整为大顶堆。
3. 最后输出大顶堆的 $k$ 个元素。

### 思路 1：代码

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

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
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

### 思路 1：复杂度分析

- **时间复杂度**：$O(n\log_2k)$。
- **空间复杂度**：$O(1)$。

### 思路 2：快速排序

使用快速排序在每次调整时，都会确定一个元素的最终位置，且以该元素为界限，将数组分成了左右两个子数组，左子数组中的元素都比该元素小，右子树组中的元素都比该元素大。

这样，只要某次划分的元素恰好是第 $k$ 个元素下标，就找到了数组中最小的 $k$ 个数所对应的区间，即 $[0, k - 1]$。 并且我们只需关注第 $k$ 个最小元素所在区间的排序情况，与第 $k$ 个最小元素无关的区间排序都可以忽略。这样进一步减少了执行步骤。

### 思路 2：代码

```python
import random

class Solution:
    # 从 arr[low: high + 1] 中随机挑选一个基准数，并进行移动排序
    def randomPartition(self, arr: [int], low: int, high: int):
        # 随机挑选一个基准数
        i = random.randint(low, high)
        # 将基准数与最低位互换
        arr[i], arr[low] = arr[low], arr[i]
        # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
        return self.partition(arr, low, high)
    
    # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
    def partition(self, arr: [int], low: int, high: int):
        pivot = arr[low]            # 以第 1 为为基准数
        i = low + 1                 # 从基准数后 1 位开始遍历，保证位置 i 之前的元素都小于基准数
        
        for j in range(i, high + 1):
            # 发现一个小于基准数的元素
            if arr[j] < pivot:
                # 将小于基准数的元素 arr[j] 与当前 arr[i] 进行换位，保证位置 i 之前的元素都小于基准数
                arr[i], arr[j] = arr[j], arr[i]
                # i 之前的元素都小于基准数，所以 i 向右移动一位
                i += 1
        # 将基准节点放到正确位置上
        arr[i - 1], arr[low] = arr[low], arr[i - 1]
        # 返回基准数位置
        return i - 1

    def quickSort(self, arr, low, high, k):
        size = len(arr)
        if low < high:
            # 按照基准数的位置，将序列划分为左右两个子序列
            pi = self.randomPartition(arr, low, high)
            if pi == k:
                return arr[:k]
            if pi > k:
                # 对左子序列进行递归快速排序
                self.quickSort(arr, low, pi - 1, k)
            if pi < k:
                # 对右子序列进行递归快速排序
                self.quickSort(arr, pi + 1, high, k)

        return arr[:k]

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        size = len(arr)
        if k >= size:
            return arr
        return self.quickSort(arr, 0, size - 1, k)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。证明过程可参考「算法导论 9.2：期望为线性的选择算法」。
- **空间复杂度**：$O(\log n)$。递归使用栈空间的空间代价期望为 $O(\log n)$。

