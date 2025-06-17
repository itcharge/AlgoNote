class MinHeap:
    def __init__(self):
        self.min_heap = []
        
    def peek(self) -> int:
        # 大顶堆为空
        if not self.min_heap:
            return None
        # 返回堆顶元素
        return self.min_heap[0]
    
    def push(self, val: int):
        # 将新元素添加到堆的末尾
        self.min_heap.append(val)
        
        size = len(self.min_heap)
        # 从新插入的元素节点开始，进行上移调整
        self.__shift_up(size - 1)
        
    def __shift_up(self, i: int):
        while (i - 1) // 2 >= 0 and self.min_heap[i] < self.min_heap[(i - 1) // 2]:
            self.min_heap[i], self.min_heap[(i - 1) // 2] = self.min_heap[(i - 1) // 2], self.min_heap[i]
            i = (i - 1) // 2
            
    def pop(self) -> int:
        # 堆为空
        if not self.min_heap:
            raise IndexError("堆为空")
        
        size = len(self.min_heap)
        self.min_heap[0], self.min_heap[size - 1] = self.min_heap[size - 1], self.min_heap[0]
        # 删除堆顶元素
        val = self.min_heap.pop()
        # 节点数减 1
        size -= 1 
        
        self.__shift_down(0, size)
        
        # 返回堆顶元素
        return val

    
    def __shift_down(self, i: int, n: int):
        while 2 * i + 1 < n:
            # 左右子节点编号
            left, right = 2 * i + 1, 2 * i + 2
            
            # 找出左右子节点中的较大值节点编号
            if 2 * i + 2 >= n:
                # 右子节点编号超出范围（只有左子节点
                larger = left
            else:
                # 左子节点、右子节点都存在
                if self.min_heap[left] <= self.min_heap[right]:
                    larger = left
                else:
                    larger = right
            
            # 将当前节点值与其较小的子节点进行比较
            if self.min_heap[i] > self.min_heap[larger]:
                # 如果当前节点值小于其较大的子节点，则将它们交换
                self.min_heap[i], self.min_heap[larger] = self.min_heap[larger], self.min_heap[i]
                i = larger
            else:
                # 如果当前节点值大于等于于其较大的子节点，此时结束
                break
    
    def __buildMinHeap(self, nums: [int]):
        size = len(nums)
        # 先将数组 nums 的元素按顺序添加到 min_heap 中
        for i in range(size):
            self.min_heap.append(nums[i])
        
        # 从最后一个非叶子节点开始，进行下移调整
        for i in range((size - 2) // 2, -1, -1):
            self.__shift_down(i, size)

    def minHeapSort(self, nums: [int]) -> [int]:
        # 根据数组 nums 建立初始堆
        self.__buildMinHeap(nums)
        
        size = len(self.min_heap)
        for i in range(size - 1, -1, -1):
            # 交换根节点与当前堆的最后一个节点
            self.min_heap[0], self.min_heap[i] = self.min_heap[i], self.min_heap[0]
            # 从根节点开始，对当前堆进行下移调整
            self.__shift_down(0, i)
        
        # 返回排序后的数组
        return self.min_heap
    
class Solution:
    def minHeapSort(self, nums: [int]) -> [int]:
        return MinHeap().minHeapSort(nums)
        
    def sortArray(self, nums: [int]) -> [int]:
        return self.minHeapSort(nums)
    
print(Solution().sortArray([10, 25, 6, 8, 7, 1, 20, 23, 16, 19, 17, 3, 18, 14]))