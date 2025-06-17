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
    
print(Solution().sortArray([39, 49, 8, 13, 22, 15, 10, 30, 5, 44]))