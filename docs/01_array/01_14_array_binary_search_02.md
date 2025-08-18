## 1. 二分查找细节

在上一节中，我们已经掌握了二分查找的基本思路和实现代码。然而，在实际解题过程中，二分查找还涉及许多关键细节，常见的有以下几个方面：

1. **区间的开闭选择**：查找区间应采用左闭右闭 $[left, right]$，还是左闭右开 $[left, right)$？
2. **$mid$ 的计算方式**：是 $mid = \lfloor \frac{left + right}{2} \rfloor$，还是 $mid = \lfloor \frac{left + right + 1}{2} \rfloor$？
3. **循环终止条件**：应使用 $left \le right$ 还是 $left < right$？
4. **区间收缩方式**：如 $left = mid + 1$、$right = mid - 1$、$left = mid$、$right = mid$ 等，应该如何选择？

接下来将针对这些细节逐一分析说明。

## 2. 区间的开闭问题

在二分查找中，区间的开闭方式决定了查找范围的边界取值。常见的有两种：

- **左闭右闭区间 $[left, right]$**：初始化时，$left = 0$，$right = len(nums) - 1$。此时 $left$ 和 $right$ 都指向有效元素，区间两端的元素都包含在查找范围内。
- **左闭右开区间 $[left, right)$**：初始化时，$left = 0$，$right = len(nums)$。$left$ 指向第一个元素，$right$ 指向最后一个元素的下一个位置，查找范围包含左端点但不包含右端点。

虽然两种区间写法都可以实现二分查找，但在实际编码和边界处理时，左闭右开区间往往更容易出错，需要额外关注边界条件，逻辑也更复杂。因此，**强烈推荐统一采用「左闭右闭区间」的写法**，这样更易于理解和维护，出错概率更低。

## 3. $mid$ 的取值问题

在实际应用二分查找时，$mid$ 的取值通常有两种常见写法：

1. `mid = (left + right) // 2`
2. `mid = (left + right + 1) // 2`

这里的 `//` 表示向下取整。若当前查找区间元素个数为奇数，这两种写法都会得到区间正中间的下标。

当区间元素个数为偶数时，`mid = (left + right) // 2` 会取到中间偏左的下标，而 `mid = (left + right + 1) // 2` 则会取到中间偏右的下标。

::: tabs#mid

@tab <1>

![mid 取值问题 1](https://qcdn.itcharge.cn/images/20230906153359.png)

@tab <2>

![mid 取值问题 2](https://qcdn.itcharge.cn/images/20230906153409.png)

:::

将这两个公式分别应用到 [704. 二分查找](https://leetcode.cn/problems/binary-search/) 的代码中，会发现它们都能通过题目测试。这是为什么？

原因在于，二分查找的核心思想是：每次根据中间元素的值，决定下一步在哪个区间继续查找。实际上，中间元素的位置不必严格取区间正中，偏左、偏右，甚至取区间的三分之一、五分之一等位置都可以，例如 `mid = (left + right) * 1 // 5` 也是可行的。

不过，通常取区间中点能在平均意义下获得最优效率，且实现最为简洁。因此，实际编码时大多数情况下会选择第一个公式。但在某些特定场景下，需要用到第二个公式，具体会在「5.2 排除法」部分详细说明。

除了上述两种写法，我们还常见如下两种等价公式：

1. `mid = left + (right - left) // 2`
2. `mid = left + (right - left + 1) // 2`

这两种写法本质上与前面的公式等价，只是通过减法避免了整型溢出的问题（虽然 Python 不会溢出，但其他语言可能会）。当 $left + right$ 不会超过整型最大值时，哪种写法都可以；但如果有溢出风险，推荐使用后一种写法。

因此，为了统一和简化二分查找的实现，建议采用如下写法：

1. `mid = left + (right - left) // 2`
2. `mid = left + (right - left + 1) // 2`

## 4. 出界条件的判断

在二分查找的实现中，`while` 循环的边界判断主要有两种常见写法：

1. `left <= right`
2. `left < right`

那么，实际编码时应如何选择呢？我们可以从循环终止的条件来分析：

- 当使用 `left <= right` 作为循环条件时，如果目标元素不存在，循环会在 `left > right` 时终止，即 $[right + 1, right]$，此时查找区间已为空，无需再判断，直接返回 $-1$ 即可。例如区间 $[3, 2]$，左边界大于右边界，查找结束。
- 当使用 `left < right` 作为循环条件时，若目标元素不存在，循环会在 `left == right` 时终止，即 $[right, right]$，此时区间内还剩下一个元素。此时不能直接返回 $-1$，因为最后一个元素可能就是目标值。例如区间 $[2, 2]$，$nums[2]$ 可能等于 $target$，直接返回 $-1$ 会遗漏正确答案。

如果选择 `left < right`，则需要在循环结束后额外判断 $nums[left]$ 是否等于目标值：

```python
    # ...
    while left < right:
        # ...
    return left if nums[left] == target else -1
```

另外，采用 `while left < right` 作为循环条件的一个优点是，循环结束时必然有 `left == right`，此时只需判断一个位置，无需区分返回 $left$ 还是 $right$，简化了后续处理。


## 5. 搜索区间范围的选择

在选择二分查找的区间更新方式时，常见有三种写法：

1. `left = mid + 1`，`right = mid - 1`
2. `left = mid + 1`，`right = mid`
3. `left = mid`，`right = mid - 1`

那么，究竟该如何确定具体的区间更新方式呢？

这正是二分查找中最容易出错的地方，区间更新不当容易导致死循环或结果错误。

本质上，这与二分查找的两种核心思路和三种区间写法密切相关：

- 思路一：「直接法」—— 在循环体内一旦找到目标元素立即返回。
- 思路二：「排除法」—— 每次循环排除目标元素一定不存在的区间。

下面我们将详细介绍这两种思路的具体实现和适用场景。

## 5.1 直接法思路

> **直接法思想**：在循环过程中，一旦找到目标元素，立即返回其下标。

这种方法实现简单，实际上我们在前文「1.13 二分查找（一）- 2. 简单二分查找」中已经用过。下面简要回顾其核心思路与代码：

#### 思路 1：直接法

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

#### 思路 1：细节

- 这种思路是在一旦循环体中找到元素就直接返回。
- 循环可以继续的条件是 `left <= right`。
- 如果一旦退出循环，则说明这个区间内一定不存在目标元素。

### 5.2 排除法 思路

> **排除法思想**：每轮循环都优先排除掉一定不包含目标元素的区间，仅在可能存在目标的区间内继续查找。

#### 思路 2：排除法

1. 初始化左右边界 $left = 0$，$right = len(nums) - 1$，查找区间为 $[left, right]$（左闭右闭）。
2. 每次计算中间位置 $mid$，比较 $nums[mid]$ 与 $target$，优先排除掉目标元素一定不存在的区间。
3. 在剩余的区间内继续查找，重复上述过程。
4. 当区间收缩到只剩一个元素时，判断该元素是否为目标值。

基于排除法，可以实现两种常见写法：

#### 思路 2：代码 1

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 在闭区间 [left, right] 内查找 target
        while left < right:
            # 计算中间位置，向下取整
            mid = left + (right - left) // 2
            # 若 nums[mid] 小于目标值，排除 [left, mid] 区间，继续在 [mid + 1, right] 查找
            if nums[mid] < target:
                left = mid + 1
            # 否则目标值可能在 [left, mid] 区间，收缩右边界
            else:
                right = mid
        # 循环结束后，left == right，判断该位置是否为目标值
        return left if nums[left] == target else -1
```

#### 思路 2：代码 2

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # 在闭区间 [left, right] 内查找 target
        while left < right:
            # 计算中间位置，向上取整，防止死循环
            mid = left + (right - left + 1) // 2
            # 如果 nums[mid] > target，说明目标只可能在 [left, mid - 1] 区间
            if nums[mid] > target:
                right = mid - 1
            # 否则，目标在 [mid, right] 区间（包括 mid）
            else:
                left = mid
        # 循环结束后，left == right，判断该位置是否为目标值
        return left if nums[left] == target else -1
```

#### 思路 2：细节

- 循环条件采用 `left < right`，这样循环结束时必然有 `left == right`，无需再区分返回 $left$ 还是 $right$，只需判断 $nums[left]$ 是否为目标值即可。
- 在循环体内，先比较目标值与中间元素的大小，优先排除目标值不可能存在的区间，然后在剩余区间继续查找。
- 排除目标值不可能存在的区间后，`else` 分支通常直接取剩余的另一半区间，无需额外判断。例如，若排除 $[left, mid]$，则剩余区间为 $[mid + 1, right]$；若排除 $[mid, right]$，则剩余区间为 $[left, mid-1]$。
- 为避免死循环，当区间被划分为 $[left, mid-1]$ 和 $[mid, right]$ 时，**$mid$ 需要向上取整**，即 `mid = left + (right - left + 1) // 2`。因为当区间只剩两个元素（$right = left + 1$）时，若 $mid$ 向下取整，`left = mid` 会导致区间不变，陷入死循环。
  - 例如 $left = 5$，$right = 6$，若 $mid = 5$，执行 $left = mid$ 后区间仍为 $[5, 6]$，无法收缩，导致死循环。
  - 若 $mid$ 向上取整，$mid = 6$，执行 $left = mid$ 后区间变为 $[6, 6]$，循环得以终止。

- 边界设置可记忆为：只要出现 `left = mid`，就要让 $mid$ 向上取整。具体配对如下：
  - `left = mid + 1`、`right = mid` 搭配 `mid = left + (right - left) // 2`。
  - `right = mid - 1`、`left = mid` 搭配 `mid = left + (right - left + 1) // 2`。

### 4.3 两种思路适用范围

- **直接法**：因为判断语句是 `left <= right`，有时候要考虑返回是 $left$ 还是 $right$。循环体内有 3 个分支，并且一定有一个分支用于退出循环或者直接返回。这种思路适合解决简单题目。即要查找的元素性质简单，数组中都是非重复元素，且 `==`、`>`、`<` 的情况非常好写的时候。
- **排除法**：更加符合二分查找算法的减治思想。每次排除目标元素一定不存在的区间，达到减少问题规模的效果。然后在可能存在的区间内继续查找目标元素。这种思路适合解决复杂题目。比如查找一个数组里可能不存在的元素，找边界问题，可以使用这种思路。

## 5. 总结  

二分查找的细节问题包括区间开闭、mid取值、循环条件和搜索范围的选择。  

**区间开闭**：建议使用左闭右闭区间，这样逻辑更简单，减少出错可能。  

**mid取值**：通常使用 `mid = left + (right - left) // 2`，防止整型溢出。在某些情况下，如 `left = mid` 时，需向上取整，避免死循环。  

**循环条件**：  
- `left <= right`：适用于直接法，循环结束时若未找到目标，直接返回 $-1$。  
- `left < right`：适用于排除法，循环结束时需额外判断 `nums[left]` 是否为目标值。  

**搜索范围选择**：  
- 直接法：`left = mid + 1` 或 `right = mid - 1`，明确缩小范围。  
- 排除法：根据情况选择 `left = mid + 1` 或 `right = mid`，以及 `right = mid - 1` 或 `left = mid`，确保每次排除无效区间。  

**两种思路**：  
- **直接法**：简单直接，适合查找明确存在的元素。  
- **排除法**：更通用，适合复杂问题，如边界查找或不确定元素是否存在的情况。  

掌握这些细节能更灵活地应用二分查找，避免常见错误。

## 练习题目

- [0278. 第一个错误的版本](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/first-bad-version.md)
- [0069. x 的平方根](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/sqrtx.md)
- [1011. 在 D 天内送达包裹的能力](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1000-1099/capacity-to-ship-packages-within-d-days.md)
- [0033. 搜索旋转排序数组](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/search-in-rotated-sorted-array.md)
- [0153. 寻找旋转排序数组中的最小值](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0100-0199/find-minimum-in-rotated-sorted-array.md)

- [二分查找题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE%E9%A2%98%E7%9B%AE)

## 参考资料

- 【博文】[Learning-Algorithms-with-Leetcode - 第 3.1 节 二分查找算法](https://www.yuque.com/liweiwei1419/algo/wkmtx4)
- 【博文】[二分法的细节加细节 你真的应该搞懂！！！_小马的博客](https://blog.csdn.net/xiao_jj_jj/article/details/106018702)
- 【课程】[零起步学算法 - LeetBook - 二分查找的基本思想：减而治之](https://leetcode.cn/leetbook/read/learning-algorithms-with-leetcode/xsz9zc/)
- 【题解】[二分查找算法细节详解，顺便写了首诗 - LeetCode](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/)