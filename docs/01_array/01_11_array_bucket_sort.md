## 1. 桶排序算法思想

> **桶排序（Bucket Sort）基本思想**：
>
> 将待排序数组中的元素分散到若干个「桶」中，然后对每个桶中的元素再进行单独排序。

## 2. 桶排序算法步骤

1. **确定桶的数量**：根据待排序数组的值域范围，将数组划分为 $k$ 个桶，每个桶可以看做是一个范围区间。
2. **分配元素**：遍历待排序数组元素，将每个元素根据大小分配到对应的桶中。
3. **对每个桶进行排序**：对每个非空桶内的元素单独排序（使用插入排序、归并排序、快排排序等算法）。
4. **合并桶内元素**：将排好序的各个桶中的元素按照区间顺序依次合并起来，形成一个完整的有序数组。

我们以 $[39, 49, 8, 13, 22, 15, 10, 30, 5, 44]$ 为例，演示一下桶排序算法的整个步骤。

![桶排序算法步骤](https://qcdn.itcharge.cn/images/20230822153701.png)

## 3. 桶排序代码实现

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

## 4. 桶排序算法分析

- **时间复杂度**：$O(n)$。当输入元素个数为 $n$，桶的个数是 $m$ 时，每个桶里的数据就是 $k = \frac{n}{m}$ 个。每个桶内排序的时间复杂度为 $O(k \times \log k)$。$m$ 个桶就是 $m \times O(k \times \log k) = m \times O(\frac{n}{m} \times \log \frac{n}{m}) = O(n \times \log \frac{n}{m})$。当桶的个数 $m$ 接近于数据个数 $n$ 时，$\log \frac{n}{m}$ 就是一个较小的常数，所以排序桶排序时间复杂度接近于 $O(n)$。
- **空间复杂度**：$O(n + m)$。由于桶排序使用了辅助空间，所以桶排序的空间复杂度是 $O(n + m)$。
- **排序稳定性**：桶排序的稳定性取决于桶内使用的排序算法。如果桶内使用稳定的排序算法（比如插入排序算法），并且在合并桶的过程中保持相等元素的相对顺序不变，则桶排序是一种 **稳定排序算法**。反之，则桶排序是一种 **不稳定排序算法**。

## 5. 总结

桶排序将元素分散到多个桶中，每个桶单独排序后再合并。它先确定桶的数量和范围，把元素分配到对应桶中，对每个桶排序，最后合并所有桶。

桶排序的时间复杂度接近 $O(n)$，在数据分布均匀时效率很高。空间复杂度是 $O(n + m)$，需要额外存储桶。排序的稳定性取决于桶内使用的排序算法。

桶排序适合数据分布均匀的情况，当数据集中在少数桶时会降低效率。实际应用中常用于外部排序和处理大数据量的场景。合理设置桶的数量和范围对性能很重要。

## 练习题目

- [0912. 排序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0900-0999/sort-an-array.md)
- [0220. 存在重复元素 III](https://github.com/itcharge/AlgoNote/blob/main/docs/solutions/0200-0299/contains-duplicate-iii.md)
- [0164. 最大间距](https://github.com/itcharge/AlgoNote/blob/main/docs/solutions/0100-0199/maximum-gap.md)

- [排序算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)