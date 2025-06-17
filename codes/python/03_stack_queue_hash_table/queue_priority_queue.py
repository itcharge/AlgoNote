class Heapq:
    # 堆调整方法：调整为大顶堆
    def heapAdjust(self, nums: [int], index: int, end: int):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子结点
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
            # value 小于当前根节点，则插入到当前位置
            if nums[cur_root] > value:
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
        # 得到最大值（堆顶元素）然后调整堆
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
    
            
nums = [49, 38, 65, 97, 76, 13, 27, 49]
heap = Heapq()
# 1. 创建堆，并进行堆排序
heap.heapSort(nums)
heap.heapify(nums)

# 2. 测试 heappop()
rst = heap.heappop(nums)
print(rst)

rst = heap.heappop(nums)
print(rst)

rst = heap.heappop(nums)
print(rst)

rst = heap.heappop(nums)
print(rst)

rst = heap.heappop(nums)
print(rst)

rst = heap.heappop(nums)
print(rst)

# 3. 测试 heappush()
nums = [49, 38, 65, 97, 76, 13, 27, 49]
heapList = []
for num in nums:
    heap.heappush(heapList, num)
    print(heapList)
    
# 4. 堆排序
rst = heap.heapSort(heapList)
print(heapList)