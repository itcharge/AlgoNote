## 1. 快速排序算法思想

> **快速排序（Quick Sort）基本思想**：
>
> 采用分治策略，选择一个基准元素，将数组分为两部分：小于基准的元素放在左侧，大于基准的元素放在右侧。然后递归地对左右两部分进行排序，最终得到有序数组。

## 2. 快速排序算法步骤

快速排序的核心是 **分区操作**，具体步骤如下：

1. **选择基准**：从数组中选择一个元素作为基准值（通常选择第一个元素）
2. **分区操作**：
   - 使用双指针法，左指针从数组开始，右指针从数组末尾
   - 右指针向左移动，找到第一个小于基准值的元素
   - 左指针向右移动，找到第一个大于基准值的元素
   - 交换这两个元素
   - 重复上述过程，直到左右指针相遇
   - 将基准值放到正确位置（左右指针相遇处）
3. **递归排序**：对基准值左右的两个子数组分别进行快速排序

以数组 $[4, 7, 5, 2, 6, 1, 3]$ 为例，先来演示一下快速排序的分区操作过程。

::: tabs#partition

@tab <1>

![分区操作 1](https://qcdn.itcharge.cn/images/20230818175908.png)

@tab <2>

![分区操作 2](https://qcdn.itcharge.cn/images/20230818175922.png)

@tab <3>

![分区操作 3](https://qcdn.itcharge.cn/images/20230818175952.png)

@tab <4>

![分区操作 4](https://qcdn.itcharge.cn/images/20230818180001.png)

@tab <5>

![分区操作 5](https://qcdn.itcharge.cn/images/20230818180009.png)

@tab <6>

![分区操作 6](https://qcdn.itcharge.cn/images/20230818180019.png)

@tab <7>

![分区操作 7](https://qcdn.itcharge.cn/images/20230818180027.png)

:::

完成一次分区后，数组被分为三部分：左子数组、基准值、右子数组。然后递归地对左右子数组进行排序。

![快速排序算法步骤](https://qcdn.itcharge.cn/images/20230818153642.png)

## 3. 快速排序代码实现

```python
import random

class Solution:
    def randomPartition(self, nums: [int], low: int, high: int) -> int:
        # 随机选择基准值，避免最坏情况
        i = random.randint(low, high)
        # 将基准数与最低位互换
        nums[i], nums[low] = nums[low], nums[i]
        # 随机将基准数移到首位，后续进行分区操作
        return self.partition(nums, low, high)
    
    # 哨兵划分法（Hoare 法）：以 nums[low] 作为基准值
    # 左右指针分别从区间两端向中间收缩
    # 使比基准值小的元素都移动到基准值左侧
    # 使比基准值大的元素都移动到基准值右侧
    # 循环后将基准值放入最终的位置，并返回该位置索引
    def partition(self, nums: [int], low: int, high: int) -> int:
        pivot = nums[low]  # 选取基准值（当前区间第一个元素）
        i, j = low, high
        
        while i < j:
            # 从右向左找小于基准值的元素
            while i < j and nums[j] >= pivot:
                j -= 1
            # 从左向右找大于基准值的元素
            while i < j and nums[i] <= pivot:
                i += 1
            # 交换元素
            nums[i], nums[j] = nums[j], nums[i]
        
        # 将基准值放到正确位置
        nums[i], nums[low] = nums[low], nums[i]
        # 返回基准数的索引
        return i

    def quickSort(self, nums: [int], low: int, high: int) -> [int]:
        if low < high:
            # 分区并获取基准值位置
            pivot_i = self.randomPartition(nums, low, high)
            # 递归排序左右子数组
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i + 1, high)
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.quickSort(nums, 0, len(nums) - 1)
```

## 4. 快速排序算法分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n \log n)$ | 每次都能将数组平均分成两半 |
| **最坏时间复杂度** | $O(n^2)$ | 每次选择的基准值都是极值（如已排序数组） |
| **平均时间复杂度** | $O(n \log n)$ | 随机选择基准值时的期望复杂度 |
| **空间复杂度** | $O(\log n)$ | 递归栈空间，最坏情况下为 $O(n)$ |
| **稳定性** | 不稳定 | 交换操作可能改变相等元素的相对位置 |

**适用场景**：

- 大规模数据排序（$n \geq 1000$）
- 对平均性能要求高的场景
- 数据分布相对均匀的情况

**优化策略**：

- 随机选择基准值，避免最坏情况
- 三数取中法选择基准值
- 小数组使用插入排序
- 处理重复元素时使用三路快排

## 5. 总结

快速排序是一种高效的排序算法，采用分治策略，通过分区操作将数组分成两部分，然后递归排序。

- **优点**：
   - 平均情况下效率高，时间复杂度为 $O(n \log n)$
   - 原地排序，空间复杂度低
   - 缓存友好，局部性良好
   - 实际应用中常数因子较小
- **缺点**：
   - 不稳定排序
   - 最坏情况下性能较差，时间复杂度为 $O(n^2)$
   - 对于小数组，其他算法可能更快
   - 递归调用可能导致栈溢出

快速排序是许多编程语言内置排序函数的实现基础，在实际应用中非常广泛。通过合理的优化策略，可以显著提高其性能和稳定性。

## 练习题目

- [0912. 排序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0900-0999/sort-an-array.md)
- [0169. 多数元素](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/majority-element.md)

- [排序算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)

## 参考资料

- 【文章】[快速排序 - OI Wiki](https://oi-wiki.org/basic/quick-sort/)
