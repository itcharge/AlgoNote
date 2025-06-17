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
    
print(Solution().sortArray([5, 2, 3, 6, 1, 4]))