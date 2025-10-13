# [0912. 排序数组](https://leetcode.cn/problems/sort-an-array/)

- 标签：数组、分治、桶排序、计数排序、基数排序、排序、堆（优先队列）、归并排序
- 难度：中等

## 题目链接

- [0912. 排序数组 - 力扣](https://leetcode.cn/problems/sort-an-array/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：将该数组升序排列。

**说明**：

- $1 \le nums.length \le 5 * 10^4$。
- $-5 * 10^4 \le nums[i] \le 5 * 10^4$。

**示例**：

- 示例 1：

```python
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
```

- 示例 2：

```python
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
```

## 解题思路

这道题是一道用来复习排序算法，测试算法时间复杂度的好题。我试过了十种排序算法。得到了如下结论：

- 超时算法（时间复杂度为 $O(n^2)$）：冒泡排序、选择排序、插入排序。
- 通过算法（时间复杂度为 $O(n \times \log n)$）：希尔排序、归并排序、快速排序、堆排序。
- 通过算法（时间复杂度为 $O(n)$）：计数排序、桶排序。
- 解答错误算法（普通基数排序只适合非负数）：基数排序。

### 思路 1：冒泡排序（超时）

> **冒泡排序（Bubble Sort）基本思想**：经过多次迭代，通过相邻元素之间的比较与交换，使值较小的元素逐步从后面移到前面，值较大的元素从前面移到后面。

假设数组的元素个数为 $n$ 个，则冒泡排序的算法步骤如下：

1. 第 $1$ 趟「冒泡」：对前 $n$ 个元素执行「冒泡」，从而使第 $1$ 个值最大的元素放置在正确位置上。
	1. 先将序列中第 $1$ 个元素与第 $2$ 个元素进行比较，如果前者大于后者，则两者交换位置，否则不交换。
	2. 然后将第 $2$ 个元素与第 $3$ 个元素比较，如果前者大于后者，则两者交换位置，否则不交换。
	3. 依次类推，直到第 $n - 1$ 个元素与第 $n$ 个元素比较（或交换）为止。
	4. 经过第 $1$ 趟排序，使得 $n$ 个元素中第 $i$ 个值最大元素被安置在第 $n$ 个位置上。
2. 第 $2$ 趟「冒泡」：对前 $n - 1$ 个元素执行「冒泡」，从而使第 $2$ 个值最大的元素放置在正确位置上。
	1. 先将序列中第 $1$ 个元素与第 $2$ 个元素进行比较，如果前者大于后者，则两者交换位置，否则不交换。
	2. 然后将第 $2$ 个元素与第 $3$ 个元素比较，如果前者大于后者，则两者交换位置，否则不交换。
	3. 依次类推，直到第 $n - 2$ 个元素与第 $n - 1$ 个元素比较（或交换）为止。
	4. 经过第 $2$ 趟排序，使得数组中第 $2$ 个值最大元素被安置在第 $n$ 个位置上。
3. 依次类推，重复上述「冒泡」过程，直到某一趟排序过程中不出现元素交换位置的动作，则排序结束。

### 思路 1：代码

```python
class Solution:
    def bubbleSort(self, nums: [int]) -> [int]:
        # 第 i 趟「冒泡」
        for i in range(len(nums) - 1):
            flag = False    # 是否发生交换的标志位
            # 对数组未排序区间 [0, n - i - 1] 的元素执行「冒泡」
            for j in range(len(nums) - i - 1):
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:    # 此趟遍历未交换任何元素，直接跳出
                break
        
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

### 思路 2：选择排序（超时）

>**选择排序（Selection Sort）基本思想**：将数组分为两个区间，左侧为已排序区间，右侧为未排序区间。每趟从未排序区间中选择一个值最小的元素，放到已排序区间的末尾，从而将该元素划分到已排序区间。

假设数组的元素个数为 $n$ 个，则选择排序的算法步骤如下：

1. 初始状态下，无已排序区间，未排序区间为 $[0, n - 1]$。
2. 第 $1$ 趟选择：
	1. 遍历未排序区间 $[0, n - 1]$，使用变量 $min\_i$ 记录区间中值最小的元素位置。
	2. 将 $min\_i$ 与下标为 $0$ 处的元素交换位置。如果下标为 $0$ 处元素就是值最小的元素位置，则不用交换。
	3. 此时，$[0, 0]$ 为已排序区间，$[1, n - 1]$（总共 $n - 1$ 个元素）为未排序区间。
3. 第 $2$ 趟选择：
	1. 遍历未排序区间 $[1, n - 1]$，使用变量 $min\_i$ 记录区间中值最小的元素位置。
	2. 将 $min\_i$ 与下标为 $1$ 处的元素交换位置。如果下标为 $1$ 处元素就是值最小的元素位置，则不用交换。
	3. 此时，$[0, 1]$ 为已排序区间，$[2, n - 1]$（总共 $n - 2$ 个元素）为未排序区间。
4. 依次类推，对剩余未排序区间重复上述选择过程，直到所有元素都划分到已排序区间，排序结束。

### 思路 2：代码

```python
class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        for i in range(len(nums) - 1):
            # 记录未排序区间中最小值的位置
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.selectionSort(nums)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

### 思路 3：插入排序（超时）

>**插入排序（Insertion Sort）基本思想**：将数组分为两个区间，左侧为有序区间，右侧为无序区间。每趟从无序区间取出一个元素，然后将其插入到有序区间的适当位置。

假设数组的元素个数为 $n$ 个，则插入排序的算法步骤如下：

1. 初始状态下，有序区间为 $[0, 0]$，无序区间为 $[1, n - 1]$。
2. 第 $1$ 趟插入：
	1. 取出无序区间 $[1, n - 1]$ 中的第 $1$ 个元素，即 $nums[1]$。
	2. 从右到左遍历有序区间中的元素，将比 $nums[1]$ 小的元素向后移动 $1$ 位。
	3. 如果遇到大于或等于 $nums[1]$ 的元素时，说明找到了插入位置，将 $nums[1]$ 插入到该位置。
	4. 插入元素后有序区间变为 $[0, 1]$，无序区间变为 $[2, n - 1]$。
3. 第 $2$ 趟插入：
	1. 取出无序区间 $[2, n - 1]$ 中的第 $1$ 个元素，即 $nums[2]$。
	2. 从右到左遍历有序区间中的元素，将比 $nums[2]$ 小的元素向后移动 $1$ 位。
	3. 如果遇到大于或等于 $nums[2]$ 的元素时，说明找到了插入位置，将 $nums[2]$ 插入到该位置。
	4. 插入元素后有序区间变为 $[0, 2]$，无序区间变为 $[3, n - 1]$。
4. 依次类推，对剩余无序区间中的元素重复上述插入过程，直到所有元素都插入到有序区间中，排序结束。

### 思路 3：代码

```python
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的所有元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp

        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.insertionSort(nums)
```

### 思路 3：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

### 思路 4：希尔排序（通过）

> **希尔排序（Shell Sort）基本思想**：将整个数组切按照一定的间隔取值划分为若干个子数组，每个子数组分别进行插入排序。然后逐渐缩小间隔进行下一轮划分子数组和对子数组进行插入排序。直至最后一轮排序间隔为 $1$，对整个数组进行插入排序。

假设数组的元素个数为 $n$ 个，则希尔排序的算法步骤如下：

1. 确定一个元素间隔数 $gap$。
2. 将参加排序的数组按此间隔数从第 $1$ 个元素开始一次分成若干个子数组，即分别将所有位置相隔为 $gap$ 的元素视为一个子数组。
3. 在各个子数组中采用某种排序算法（例如插入排序算法）进行排序。
4. 减少间隔数，并重新将整个数组按新的间隔数分成若干个子数组，再分别对各个子数组进行排序。
5. 依次类推，直到间隔数 $gap$ 值为 $1$，最后进行一次排序，排序结束。

### 思路 4：代码

```python
class Solution:
    def shellSort(self, nums: [int]) -> [int]:
        size = len(nums)
        gap = size // 2
        # 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序数组第 1 个元素
                temp = nums[i]
                j = i
                # 从右至左遍历每组中的有序数组元素
                while j >= gap and nums[j - gap] > temp:
                    # 将每组有序数组中插入位置右侧的元素依次在组中右移一位
                    nums[j] = nums[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                nums[j] = temp
            # 缩小 gap 间隔
            gap = gap // 2
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.shellSort(nums)
```

### 思路 4：复杂度分析

- **时间复杂度**：介于 $O(n \times \log n)$ 与 $O(n^2)$ 之间。
- **空间复杂度**：$O(1)$。

### 思路 5：归并排序（通过）

> **归并排序（Merge Sort）基本思想**：采用经典的分治策略，先递归地将当前数组平均分成两半，然后将有序数组两两合并，最终合并成一个有序数组。

假设数组的元素个数为 $n$ 个，则归并排序的算法步骤如下：

1. **分解过程**：先递归地将当前数组平均分成两半，直到子数组长度为 $1$。
	1. 找到数组中心位置 $mid$，从中心位置将数组分成左右两个子数组 $left\_nums$、$right\_nums$。
	2. 对左右两个子数组 $left\_nums$、$right\_nums$ 分别进行递归分解。
	3. 最终将数组分解为 $n$ 个长度均为 $1$ 的有序子数组。
2. **归并过程**：从长度为 $1$ 的有序子数组开始，依次将有序数组两两合并，直到合并成一个长度为 $n$ 的有序数组。
	1. 使用数组变量 $nums$ 存放合并后的有序数组。
	2. 使用两个指针 $left\_i$、$right\_i$ 分别指向两个有序子数组 $left\_nums$、$right\_nums$ 的开始位置。
	3. 比较两个指针指向的元素，将两个有序子数组中较小元素依次存入到结果数组 $nums$ 中，并将指针移动到下一位置。
	4. 重复步骤 $3$，直到某一指针到达子数组末尾。
	5. 将另一个子数组中的剩余元素存入到结果数组 $nums$ 中。
	6. 返回合并后的有序数组 $nums$。

### 思路 5：代码

```python
class Solution:
    # 合并过程
    def merge(self, left_nums: [int], right_nums: [int]):
        nums = []
        left_i, right_i = 0, 0
        while left_i < len(left_nums) and right_i < len(right_nums):
            # 将两个有序子数组中较小元素依次插入到结果数组中
            if left_nums[left_i] < right_nums[right_i]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_i])
                right_i += 1
        
        # 如果左子数组有剩余元素，则将其插入到结果数组中
        while left_i < len(left_nums):
            nums.append(left_nums[left_i])
            left_i += 1
        
        # 如果右子数组有剩余元素，则将其插入到结果数组中
        while right_i < len(right_nums):
            nums.append(right_nums[right_i])
            right_i += 1
        
        # 返回合并后的结果数组
        return nums

    # 分解过程
    def mergeSort(self, nums: [int]) -> [int]:
        # 数组元素个数小于等于 1 时，直接返回原数组
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2                        # 将数组从中间位置分为左右两个数组
        left_nums = self.mergeSort(nums[0: mid])    # 递归将左子数组进行分解和排序
        right_nums =  self.mergeSort(nums[mid:])    # 递归将右子数组进行分解和排序
        return self.merge(left_nums, right_nums)    # 把当前数组组中有序子数组逐层向上，进行两两合并

    def sortArray(self, nums: [int]) -> [int]:
        return self.mergeSort(nums)
```

### 思路 5：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(n)$。

### 思路 6：快速排序（通过）

> **快速排序（Quick Sort）基本思想**：采用经典的分治策略，选择数组中某个元素作为基准数，通过一趟排序将数组分为独立的两个子数组，一个子数组中所有元素值都比基准数小，另一个子数组中所有元素值都比基准数大。然后再按照同样的方式递归的对两个子数组分别进行快速排序，以达到整个数组有序。

假设数组的元素个数为 $n$ 个，则快速排序的算法步骤如下：

1. **哨兵划分**：选取一个基准数，将数组中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。
	1. 从当前数组中找到一个基准数 $pivot$（这里以当前数组第 $1$ 个元素作为基准数，即 $pivot = nums[low]$）。
	2. 使用指针 $i$ 指向数组开始位置，指针 $j$  指向数组末尾位置。
	3. 从右向左移动指针 $j$，找到第 $1$ 个小于基准值的元素。
	4. 从左向右移动指针 $i$，找到第 $1$ 个大于基准数的元素。
	5. 交换指针 $i$、指针 $j$ 指向的两个元素位置。
	6. 重复第 $3 \sim 5$ 步，直到指针 $i$ 和指针 $j$ 相遇时停止，最后将基准数放到两个子数组交界的位置上。
2. **递归分解**：完成哨兵划分之后，对划分好的左右子数组分别进行递归排序。
	1. 按照基准数的位置将数组拆分为左右两个子数组。
	2. 对每个子数组分别重复「哨兵划分」和「递归分解」，直到各个子数组只有 $1$ 个元素，排序结束。

### 思路 6：代码

```python
import random

class Solution:
    # 随机哨兵划分：从 nums[low: high + 1] 中随机挑选一个基准数，并进行移位排序
    def randomPartition(self, nums: [int], low: int, high: int) -> int:
        # 随机挑选一个基准数
        i = random.randint(low, high)
        # 将基准数与最低位互换
        nums[i], nums[low] = nums[low], nums[i]
        # 以最低位为基准数，然后将数组中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
        return self.partition(nums, low, high)
    
    # 哨兵划分：以第 1 位元素 nums[low] 为基准数，然后将比基准数小的元素移动到基准数左侧，将比基准数大的元素移动到基准数右侧，最后将基准数放到正确位置上
    def partition(self, nums: [int], low: int, high: int) -> int:        
        # 以第 1 位元素为基准数
        pivot = nums[low]
        
        i, j = low, high
        while i < j:
            # 从右向左找到第 1 个小于基准数的元素
            while i < j and nums[j] >= pivot:
                j -= 1
            # 从左向右找到第 1 个大于基准数的元素
            while i < j and nums[i] <= pivot:
                i += 1
            # 交换元素
            nums[i], nums[j] = nums[j], nums[i]
        
        # 将基准数放到正确位置上
        nums[j], nums[low] = nums[low], nums[j]
        return j

    def quickSort(self, nums: [int], low: int, high: int) -> [int]:
        if low < high:
            # 按照基准数的位置，将数组划分为左右两个子数组
            pivot_i = self.partition(nums, low, high)
            # 对左右两个子数组分别进行递归快速排序
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i + 1, high)

        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.quickSort(nums, 0, len(nums) - 1)
```

### 思路 6：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(n)$。

### 思路 7：堆排序（通过）

> **堆排序（Heap sort）基本思想**：借用「堆结构」所设计的排序算法。将数组转化为大顶堆，重复从大顶堆中取出数值最大的节点，并让剩余的堆结构继续维持大顶堆性质。

假设数组的元素个数为 $n$ 个，则堆排序的算法步骤如下：

1. **构建初始大顶堆**：
	1. 定义一个数组实现的堆结构，将原始数组的元素依次存入堆结构的数组中（初始顺序不变）。
	2. 从数组的中间位置开始，从右至左，依次通过「下移调整」将数组转换为一个大顶堆。

2. **交换元素，调整堆**：
	1. 交换堆顶元素（第 $1$ 个元素）与末尾（最后 $1$ 个元素）的位置，交换完成后，堆的长度减 $1$。
	2. 交换元素之后，由于堆顶元素发生了改变，需要从根节点开始，对当前堆进行「下移调整」，使其保持堆的特性。

3. **重复交换和调整堆**：
	1. 重复第 $2$ 步，直到堆的大小为 $1$ 时，此时大顶堆的数组已经完全有序。

### 思路 7：代码

```python
class Solution:
    # 调整为大顶堆
    def heapify(self, arr, index, end):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子节点
            max_index = index
            if arr[left] > arr[max_index]:
                max_index = left
            if right <= end and arr[right] > arr[max_index]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            arr[index], arr[max_index] = arr[max_index], arr[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 初始化大顶堆
    def buildMaxHeap(self, arr):
        size = len(arr)
        # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(arr, i, size - 1)
        return arr

    # 升序堆排序，思路如下：
    # 1. 先建立大顶堆
    # 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
    # 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
    # 4. 以此类推，直到最后一个元素交换之后完毕。
    def maxHeapSort(self, arr):
        self.buildMaxHeap(arr)
        size = len(arr)
        for i in range(size):
            arr[0], arr[size-i-1] = arr[size-i-1], arr[0]
            self.heapify(arr, 0, size-i-2)
        return arr

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.maxHeapSort(nums)
```

### 思路 7：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(1)$。

### 思路 8：计数排序（通过）

> **计数排序（Counting Sort）基本思想**：通过统计数组中每个元素在数组中出现的次数，根据这些统计信息将数组元素有序的放置到正确位置，从而达到排序的目的。

假设数组的元素个数为 $n$ 个，则计数排序的算法步骤如下：

1. **计算排序范围**：遍历数组，找出待排序序列中最大值元素 $nums\_max$ 和最小值元素 $nums\_min$，计算出排序范围为 $nums\_max - nums\_min + 1$。
2. **定义计数数组**：定义一个大小为排序范围的计数数组 $counts$，用于统计每个元素的出现次数。其中：
	1. 数组的索引值 $num - nums\_min$ 表示元素的值为 $num$。
	2. 数组的值 $counts[num - nums\_min]$ 表示元素 $num$ 的出现次数。

3. **对数组元素进行计数统计**：遍历待排序数组 $nums$，对每个元素在计数数组中进行计数，即将待排序数组中「每个元素值减去最小值」作为索引，将「对计数数组中的值」加 $1$，即令 $counts[num - nums\_min]$ 加 $1$。
4. **生成累积计数数组**：从 $counts$ 中的第 $1$ 个元素开始，每一项累家前一项和。此时 $counts[num - nums\_min]$ 表示值为 $num$ 的元素在排序数组中最后一次出现的位置。
5. **逆序填充目标数组**：逆序遍历数组 $nums$，将每个元素 $num$ 填入正确位置。
  6. 将其填充到结果数组 $res$ 的索引 $counts[num - nums\_min]$ 处。
  7. 放入后，令累积计数数组中对应索引减 $1$，从而得到下个元素 $num$ 的放置位置。

### 思路 8：代码

```python
class Solution:
    def countingSort(self, nums: [int]) -> [int]:
        # 计算待排序数组中最大值元素 nums_max 和最小值元素 nums_min
        nums_min, nums_max = min(nums), max(nums)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = nums_max - nums_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计值为 num 的元素出现的次数
        for num in nums:
            counts[num - nums_min] += 1
        
        # 生成累积计数数组
        for i in range(1, size):
            counts[i] += counts[i - 1]

        # 反向填充目标数组
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 根据累积计数数组，将 num 放在数组对应位置
            res[counts[num - nums_min] - 1] = num
            # 将 num 的对应放置位置减 1，从而得到下个元素 num 的放置位置
            counts[nums[i] - nums_min] -= 1

        return res

    def sortArray(self, nums: [int]) -> [int]:
        return self.countingSort(nums)
```

### 思路 8：复杂度分析

- **时间复杂度**：$O(n + k)$。其中 $k$ 代表待排序序列的值域。
- **空间复杂度**：$O(k)$。其中 $k$ 代表待排序序列的值域。

### 思路 9：桶排序（通过）

> **桶排序（Bucket Sort）基本思想**：将待排序数组中的元素分散到若干个「桶」中，然后对每个桶中的元素再进行单独排序。

假设数组的元素个数为 $n$ 个，则桶排序的算法步骤如下：

1. **确定桶的数量**：根据待排序数组的值域范围，将数组划分为 $k$ 个桶，每个桶可以看做是一个范围区间。
2. **分配元素**：遍历待排序数组元素，将每个元素根据大小分配到对应的桶中。
3. **对每个桶进行排序**：对每个非空桶内的元素单独排序（使用插入排序、归并排序、快排排序等算法）。
4. **合并桶内元素**：将排好序的各个桶中的元素按照区间顺序依次合并起来，形成一个完整的有序数组。

### 思路 9：代码

```python
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp
            
        return nums

    def bucketSort(self,  nums: [int], bucket_size=5) -> [int]:
        # 计算待排序序列中最大值元素 nums_max、最小值元素 nums_min
        nums_min, nums_max = min(nums), max(nums)
        # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
        bucket_count = (nums_max - nums_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历待排序数组元素，将每个元素根据大小分配到对应的桶中
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)

        # 对每个非空桶内的元素单独排序，排序之后，按照区间顺序依次合并到 res 数组中
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)
        
        # 返回结果数组
        return res

    def sortArray(self, nums: [int]) -> [int]:
        return self.bucketSort(nums)
```

### 思路 9：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n + m)$。$m$ 为桶的个数。

### 思路 10：基数排序（提交解答错误，普通基数排序只适合非负数）

> **基数排序（Radix Sort）基本思想**：将整数按位数切割成不同的数字，然后从低位开始，依次到高位，逐位进行排序，从而达到排序的目的。

我们以最低位优先法为例，讲解一下基数排序的算法步骤。

1. **确定排序的最大位数**：遍历数组元素，获取数组最大值元素，并取得对应位数。
2. **从最低位（个位）开始，到最高位为止，逐位对每一位进行排序**：
	1. 定义一个长度为 $10$ 的桶数组 $buckets$，每个桶分别代表 $0 \sim 9$ 中的 $1$ 个数字。
	2. 按照每个元素当前位上的数字，将元素放入对应数字的桶中。
	3. 清空原始数组，然后按照桶的顺序依次取出对应元素，重新加入到原始数组中。

### 思路 10：代码

```python
class Solution:
    def radixSort(self, nums: [int]) -> [int]:
        # 桶的大小为所有元素的最大位数
        size = len(str(max(nums)))
        
        # 从最低位（个位）开始，逐位遍历每一位
        for i in range(size):
            # 定义长度为 10 的桶数组 buckets，每个桶分别代表 0 ~ 9 中的 1 个数字。
            buckets = [[] for _ in range(10)]
            # 遍历数组元素，按照每个元素当前位上的数字，将元素放入对应数字的桶中。
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            # 清空原始数组
            nums.clear()
            # 按照桶的顺序依次取出对应元素，重新加入到原始数组中。
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)
                    
        # 完成排序，返回结果数组
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.radixSort(nums)
```

### 思路 10：复杂度分析

- **时间复杂度**：$O(n \times k)$。其中 $n$ 是待排序元素的个数，$k$ 是数字位数。$k$ 的大小取决于数字位的选择（十进制位、二进制位）和待排序元素所属数据类型全集的大小。
- **空间复杂度**：$O(n + k)$。

