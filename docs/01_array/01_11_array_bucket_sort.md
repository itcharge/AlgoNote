## 1. 桶排序算法思想

> **桶排序（Bucket Sort）**：
> 
> 将待排序元素分散到多个桶中，对每个桶单独排序后合并。

## 2. 桶排序算法步骤

1. **确定桶的数量**：根据待排序数组的数值范围，将其划分为 $k$ 个桶，每个桶对应一个特定的区间。
2. **元素分配**：遍历数组，将每个元素根据其数值映射到所属的桶中。
3. **桶内排序**：对每个非空桶分别进行排序（可选用插入排序、归并排序、快速排序等算法）。
4. **合并结果**：按桶的顺序依次合并所有已排序的桶，得到最终有序数组。

以数组 $[39, 49, 8, 13, 22, 15, 10, 30, 5, 44]$ 为例，演示一下桶排序的算法步骤。

![桶排序的算法步骤](https://qcdn.itcharge.cn/images/20230822153701.png)

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

    def bucketSort(self, nums: [int], bucket_size=5) -> [int]:
        # 计算数据范围
        nums_min, nums_max = min(nums), max(nums)
        bucket_count = (nums_max - nums_min + 1) // bucket_size
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历待排序数组元素，将每个元素根据大小分配到对应的桶中
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)

        # 排序并合并
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

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n)$ | 数据分布均匀，每个桶内元素数量相近 |
| **最坏时间复杂度** | $O(n^2)$ | 数据集中在少数桶中，桶内排序复杂度高 |
| **平均时间复杂度** | $O(n + k)$ | $k$ 为桶的数量，数据分布较均匀时接近 $O(n)$ |
| **空间复杂度** | $O(n + m)$ | 需要额外空间存储桶，$m$ 为桶的数量 |
| **稳定性** | 稳定 | 取决于桶内排序算法，通常使用稳定排序 |

**适用场景**：

- 数据分布均匀
- 外部排序
- 数据范围已知且有限

## 5. 总结

桶排序是一种分布式排序算法，通过将数据分散到多个桶中，对每个桶单独排序后合并实现排序。

- **优点**：数据分布均匀时效率高，适合外部排序，可并行处理
- **缺点**：需要额外空间，数据分布不均匀时效率下降，对数据范围有要求

## 练习题目

- [0912. 排序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0900-0999/sort-an-array.md)
- [0220. 存在重复元素 III](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/contains-duplicate-iii.md)
- [0164. 最大间距](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/maximum-gap.md)

- [排序算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)
