## 1. 基数排序算法思想

> **基数排序（Radix Sort）基本思想**：
>
> 按照数字的每一位进行排序，从最低位到最高位，逐位比较。

## 2. 基数排序算法步骤

基数排序算法可以采用「最低位优先法（Least Significant Digit First）」或者「最高位优先法（Most Significant Digit first）」。最常用的是「最低位优先法」。

下面我们以最低位优先法为例，讲解一下算法步骤。

1. **确定最大位数**：遍历数组元素，找到数组中最大值的位数。
2. **从最低位（个位）开始，到最高位为止，逐位对每一位进行排序**：
   1. 创建 10 个桶（每个桶分别代表 $0 \sim 9$ 中的一个数字）。
   2. 按照每个元素当前位上的数字，将元素放入对应桶中。
   3. 清空原始数组，然后按照桶的顺序依次取出对应元素，重新加入到数组中。

我们以 $[692, 924, 969, 503, 871, 704, 542, 436]$ 为例，演示一下基数排序的算法步骤。

![基数排序的算法步骤](https://qcdn.itcharge.cn/images/20230822171758.png)

## 3. 基数排序代码实现

```python
class Solution:
    def radixSort(self, nums: [int]) -> [int]:
        # 获取最大位数
        size = len(str(max(nums)))
        
        # 从个位开始逐位排序
        for i in range(size):
            # 创建 10 个桶，每个桶分别代表 0 ~ 9 中的 1 个数字
            buckets = [[] for _ in range(10)]
            
            # 按当前位数字分桶
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            
            # 重新收集
            nums.clear()
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)
                    
        # 完成排序，返回结果数组
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.radixSort(nums)
```

## 4. 基数排序算法分析

| 指标 | 复杂度 | 说明 |
|------|--------|------|
| **最佳时间复杂度** | $O(n \times k)$ | 所有数字位数相同，$k$ 为最大位数 |
| **最坏时间复杂度** | $O(n \times k)$ | 所有数字位数相同，$k$ 为最大位数 |
| **平均时间复杂度** | $O(n \times k)$ | 基数排序的时间复杂度与数据状态无关 |
| **空间复杂度** | $O(n + k)$ | 需要 $n$ 个元素的存储空间和 $k$ 个桶 |
| **稳定性** | 稳定 | 桶排序保证相等元素的相对位置不变 |

**适用场景**：

- 整数排序，位数不多（$k$ 较小）
- 数据范围大但位数固定
- 电话号码、身份证号等固定位数数据

## 5. 总结

基数排序是一种非比较排序算法，通过按位分配和收集实现排序。

- **优点**：时间复杂度与数据范围无关，稳定排序，适合固定位数数据
- **缺点**：空间复杂度较高，只适用于整数排序

## 练习题目

- [0912. 排序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0900-0999/sort-an-array.md)
- [0164. 最大间距](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/maximum-gap.md)
- [0561. 数组拆分](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0500-0599/array-partition.md)

- [排序算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)