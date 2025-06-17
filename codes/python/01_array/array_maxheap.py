class MaxHeap:
    def __init__(self):
        self.max_heap = []
        
    def peek(self) -> int:
        # 大顶堆为空
        if not self.max_heap:
            return None
        # 返回堆顶元素
        return self.max_heap[0]
    
    def push(self, val: int):
        # 将新元素添加到堆的末尾
        self.max_heap.append(val)
        
        size = len(self.max_heap)
        # 从新插入的元素节点开始，进行上移调整
        self.__shift_up(size - 1)
        
    def __shift_up(self, i: int):
        while (i - 1) // 2 >= 0 and self.max_heap[i] > self.max_heap[(i - 1) // 2]:
            self.max_heap[i], self.max_heap[(i - 1) // 2] = self.max_heap[(i - 1) // 2], self.max_heap[i]
            i = (i - 1) // 2
            
    def pop(self) -> int:
        # 堆为空
        if not self.max_heap:
            raise IndexError("堆为空")
            
        size = len(self.max_heap)
        self.max_heap[0], self.max_heap[size - 1] = self.max_heap[size - 1], self.max_heap[0]
        # 删除堆顶元素
        val = self.max_heap.pop()
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
                if self.max_heap[left] >= self.max_heap[right]:
                    larger = left
                else:
                    larger = right
                    
            # 将当前节点值与其较大的子节点进行比较
            if self.max_heap[i] < self.max_heap[larger]:
                # 如果当前节点值小于其较大的子节点，则将它们交换
                self.max_heap[i], self.max_heap[larger] = self.max_heap[larger], self.max_heap[i]
                i = larger
            else:
                # 如果当前节点值大于等于于其较大的子节点，此时结束
                break

    
class Solution:
    def maxHeapOperations(self):
        max_heap = MaxHeap()
        max_heap.push(3)
        print(max_heap.peek())
        max_heap.push(2)
        print(max_heap.peek())
        max_heap.push(4)
        print(max_heap.peek())
        max_heap.pop()
        print(max_heap.peek())
        
        
    
print(Solution().maxHeapOperations())