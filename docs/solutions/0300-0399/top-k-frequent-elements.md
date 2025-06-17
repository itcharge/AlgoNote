# [0347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)

- 标签：数组、哈希表、分治、桶排序、计数、快速选择、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0347. 前 K 个高频元素 - 力扣](https://leetcode.cn/problems/top-k-frequent-elements/)

## 题目大意

**描述**：给定一个整数数组 $nums$ 和一个整数 $k$。

**要求**：返回出现频率前 $k$ 高的元素。可以按任意顺序返回答案。

**说明**：

- $1 \le nums.length \le 10^5$。
- $k$ 的取值范围是 $[1, \text{ 数组中不相同的元素的个数}]$。
- 题目数据保证答案唯一，换句话说，数组中前 $k$ 个高频元素的集合是唯一的。

**示例**：

- 示例 1：

```python
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

- 示例 2：

```python
输入: nums = [1], k = 1
输出: [1]
```

## 解题思路

### 思路 1：哈希表 + 优先队列

1. 使用哈希表记录下数组中各个元素的频数。
2. 然后将哈希表中的元素去重，转换为新数组。时间复杂度 $O(n)$，空间复杂度 $O(n)$。
3. 使用二叉堆构建优先队列，优先级为元素频数。此时堆顶元素即为频数最高的元素。时间复杂度 $O(n)$，空间复杂度 $O(n)$。
4. 将堆顶元素加入到答案数组中，进行出队操作。时间复杂度 $O(log{n})$。
   - 出队操作：交换堆顶元素与末尾元素，将末尾元素已移出堆。继续调整大顶堆。
5. 不断重复第 4 步，直到 $k$ 次结束。调整 $k$ 次的时间复杂度 $O(n \times \log n)$。

### 思路 1：代码

```python
class Heapq:
    # 堆调整方法：调整为大顶堆
    def heapAdjust(self, nums: [int], nums_dict, index: int, end: int):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子结点
            max_index = index
            if nums_dict[nums[left]] > nums_dict[nums[max_index]]:
                max_index = left
            if right <= end and nums_dict[nums[right]] > nums_dict[nums[max_index]]:
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
    def heapify(self, nums: [int], nums_dict):
        size = len(nums)
        # (size - 2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            # 调用调整堆函数
            self.heapAdjust(nums, nums_dict, i, size - 1)
    
    # 入队操作
    def heappush(self, nums: list, nums_dict, value):
        nums.append(value)
        size = len(nums)
        i = size - 1
        # 寻找插入位置
        while (i - 1) // 2 >= 0:
            cur_root = (i - 1) // 2
            # value 小于当前根节点，则插入到当前位置
            if nums_dict[nums[cur_root]] > nums_dict[value]:
                break
            # 继续向上查找
            nums[i] = nums[cur_root]
            i = cur_root
        # 找到插入位置或者到达根位置，将其插入
        nums[i] = value
                
    # 出队操作
    def heappop(self, nums: list, nums_dict) -> int:
        size = len(nums)
        nums[0], nums[-1] = nums[-1], nums[0]
        # 得到最大值（堆顶元素）然后调整堆
        top = nums.pop()
        if size > 0:
            self.heapAdjust(nums, nums_dict, 0, size - 2)
            
        return top

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素频数
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        # 使用 set 方法去重，得到新数组
        new_nums = list(set(nums))
        size = len(new_nums)

        heap = Heapq()
        queue = []
        for num in new_nums:
            heap.heappush(queue, nums_dict, num)
        
        res = []
        for i in range(k):
            res.append(heap.heappop(queue, nums_dict))
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(n)$。