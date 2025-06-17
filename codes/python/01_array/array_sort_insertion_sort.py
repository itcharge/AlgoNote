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
    
print(Solution().sortArray([5, 2, 3, 6, 1, 4]))