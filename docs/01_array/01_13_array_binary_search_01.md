## 1. 二分查找算法介绍

### 1.1 算法简介

> **二分查找算法（Binary Search Algorithm）**，又称折半查找或对数查找，是一种在有序数组中高效定位目标元素的方法。其核心思想是每次将查找区间缩小一半，从而快速锁定目标位置。

### 1.2 算法步骤

1. **初始化**：确定待查找的有序数据集合（如数组或列表），并确保元素已按升序或降序排列。
2. **设置查找区间**：定义查找的左右边界，初始时 $left$ 指向数组起始位置，$right$ 指向数组末尾位置。
3. **计算中间下标**：通过 $mid = \lfloor (left + right) / 2 \rfloor$ 计算当前查找区间的中间下标 $mid$。
4. **比较并缩小区间**：将目标值 $target$ 与 $nums[mid]$ 比较：
   1. 若 $target == nums[mid]$，则找到目标，返回 $mid$。
   2. 若 $target < nums[mid]$，目标在左半区间，更新右边界 $right = mid - 1$。
   3. 若 $target > nums[mid]$，目标在右半区间，更新左边界 $left = mid + 1$。
5. 重复步骤 $3 \sim 4$，直到找到目标元素（返回 $mid$），或查找区间为空（$left > right$），此时返回 $-1$，表示目标不存在。

我们以在有序数组 $[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]$ 中查找目标元素 $6$ 为例，二分查找的具体过程如下：

1. **设置查找区间**：左边界 $left = 0$（数组起始位置），右边界 $right = 10$（数组末尾位置），查找区间为 $[0, 10]$。
2. **第一次取中间元素**：$mid = (0 + 10) \div 2 = 5$，$nums[5] = 5$。
3. **比较目标值与中间元素**：$6 > 5$，目标值在右半区间，更新左边界 $left = 6$，查找区间变为 $[6, 10]$。
4. **第二次取中间元素**：$mid = (6 + 10) \div 2 = 8$，$nums[8] = 8$。
5. **再次比较**：$6 < 8$，目标值在左半区间，更新右边界 $right = 7$，查找区间变为 $[6, 7]$。
6. **第三次取中间元素**：$mid = (6 + 7) \div 2 = 6$，$nums[6] = 6$。
7. **找到目标值**：$6 == 6$，查找成功，返回下标 $6$，算法结束。

可以看到，对于一个长度为 $10$ 的有序数组，使用二分查找仅需 $3$ 次比较就能定位目标元素；而若采用顺序遍历，最坏情况下则需要 $10$ 次比较才能找到目标。这充分体现了二分查找在有序数据中的高效性。

下面展示了二分查找算法在有序数组中查找目标元素 $6$ 的完整过程，详细说明了每一步如何更新查找区间、选择中间元素，并最终定位到目标元素的位置。

::: tabs#BinarySearch

@tab <1>

![二分查找算法 1](https://qcdn.itcharge.cn/images/20230907144632.png)

@tab <2>

![二分查找算法 2](https://qcdn.itcharge.cn/images/20230906133742.png)

@tab <3>

![二分查找算法 3](https://qcdn.itcharge.cn/images/20230906133758.png)

@tab <4>

![二分查找算法 4](https://qcdn.itcharge.cn/images/20230906133809.png)

@tab <5>

![二分查找算法 5](https://qcdn.itcharge.cn/images/20230906133820.png)

@tab <6>

![二分查找算法 6](https://qcdn.itcharge.cn/images/20230906133830.png)

@tab <7>

![二分查找算法 7](https://qcdn.itcharge.cn/images/20230906133839.png)

@tab <8>

![二分查找算法 8](https://qcdn.itcharge.cn/images/20230906133848.png)

:::

### 1.3 二分查找算法思想

二分查找算法体现了经典的 **「减而治之」** 思想。

所谓 **「减」**，就是每一步都通过条件判断，排除掉一部分一定不包含目标元素的区间，从而缩小问题规模；**「治」**，则是在缩小后的区间内继续解决剩下的子问题。也就是说，二分查找的核心在于：**每次查找都排除掉不可能存在目标的区间，仅在可能存在目标的区间内继续查找**。

通过不断缩小查找区间，问题规模逐步减小。由于区间有限，经过有限次迭代，最终要么找到目标元素，要么确定目标不存在于数组中。

## 2. 简单二分查找

下面通过一个简单的例子来讲解下二分查找的思路和代码。

- 题目链接：[704. 二分查找](https://leetcode.cn/problems/binary-search/)

### 2.1 题目大意

**描述**：给定一个升序的数组 $nums$，和一个目标值 $target$。

**要求**：返回 $target$ 在数组中的位置，如果找不到，则返回 $-1$。

**说明**：

- 你可以假设 $nums$ 中的所有元素是不重复的。
- $n$ 将在 $[1, 10000]$ 之间。
- $nums$ 的每个元素都将在 $[-9999, 9999]$之间。

**示例**：

```python
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

### 2.2 解题思路

#### 思路 1：二分查找

1. 初始化左右边界，令 $left = 0$，$right = len(nums) - 1$，即查找区间为 $[left, right]$（左闭右闭）。
2. 在每轮循环中，计算中间位置 $mid$，比较 $nums[mid]$ 与目标值 $target$：
   1. 如果 $nums[mid] == target$，直接返回 $mid$。
   2. 如果 $nums[mid] < target$，则目标值只可能在右半区间，将 $left$ 更新为 $mid + 1$。
   3. 如果 $nums[mid] > target$，则目标值只可能在左半区间，将 $right$ 更新为 $mid - 1$。
3. 当 $left > right$ 时，说明查找区间已为空，目标值不存在，返回 $-1$。

#### 思路 1：代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 循环查找区间为 [left, right]，直到区间为空
        while left <= right:
            # 计算中间位置，防止溢出可写为 left + (right - left) // 2
            mid = (left + right) // 2
            # 命中目标，直接返回下标
            if nums[mid] == target:
                return mid
            # 目标在右半区间，收缩左边界
            elif nums[mid] < target:
                left = mid + 1
            # 目标在左半区间，收缩右边界
            else:
                right = mid - 1
        # 查找失败，返回 -1
        return -1
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(1)$。

## 3. 总结

### 3.1 核心要点

**二分查找**是一种在**有序数组**中高效查找目标元素的算法，其核心思想是**每次将查找区间缩小一半**，从而快速定位目标位置。

### 3.2 算法特点

- **时间复杂度**：$O(\log n)$，比线性查找 $O(n)$ 更高效。
- **空间复杂度**：$O(1)$，只需要常数级别的额外空间。
- **适用条件**：数据必须是有序的（升序或降序）。
- **核心思想**：减而治之，每次排除一半不可能的区域。

### 3.3 实现要点

1. **区间定义**：使用左闭右闭区间 `[left, right]`。
2. **中间计算**：`mid = (left + right) // 2` 或 `mid = left + (right - left) // 2`（防溢出）。
3. **边界更新**：
   - 目标在右半区间：`left = mid + 1`
   - 目标在左半区间：`right = mid - 1`
4. **终止条件**：`left > right` 时查找失败。

### 3.4 应用场景

- 在有序数组中查找特定元素
- 查找插入位置
- 寻找边界值
- 数值范围查询

二分查找是算法学习中的基础算法，掌握其思想和实现对于解决更复杂的查找问题具有重要意义。

## 练习题目

- [0704. 二分查找](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/binary-search.md)
- [0374. 猜数字大小](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/guess-number-higher-or-lower.md)
- [0035. 搜索插入位置](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/search-insert-position.md)
- [0167. 两数之和 II - 输入有序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/two-sum-ii-input-array-is-sorted.md)

- [二分查找题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE%E9%A2%98%E7%9B%AE)