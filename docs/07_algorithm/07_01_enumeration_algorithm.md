## 1. 枚举算法简介

> **枚举算法（Enumeration Algorithm）**，又称穷举算法，是指根据问题的特点，逐一列出所有可能的解，并与目标条件进行比较，找出满足要求的答案。枚举时要确保不遗漏、不重复。

枚举算法的核心思想就是：遍历所有可能的状态，逐个判断是否满足条件，找到符合要求的解。

由于需要遍历所有状态，枚举算法在问题规模较大时效率较低。但它也有明显优点：

1. 实现简单，易于编程和调试。
2. 基于穷举所有情况，正确性容易验证。

因此，枚举算法常用于小规模问题，或作为其他算法的辅助工具，通过枚举部分信息来提升主算法的效率。

## 2. 枚举算法的解题思路

### 2.1 枚举算法的解题思路

枚举算法是最简单、最基础的搜索方法，通常是遇到问题时的首选方案。

由于实现简单，我们可以先用枚举算法尝试解决问题，再考虑是否需要优化。

枚举算法的基本步骤如下：

1. 明确需要枚举的对象、枚举范围和约束条件。
2. 逐一枚举所有可能情况，判断是否满足题意。
3. 思考如何提升枚举效率。

提升效率的常用方法有：

- 抓住问题本质，尽量缩小状态空间。
- 增加约束条件，减少无效枚举。
- 利用某些问题特有的性质（例如对称性等），避免重复计算。

### 2.2 枚举算法的简单应用

以经典的「百钱买百鸡问题」为例：

> **问题**：公鸡 5 元/只，母鸡 3 元/只，小鸡 1 元/3 只。用 100 元买 100 只鸡，问各买多少只？

**解题步骤**：

1. **确定枚举对象和范围**
   - 枚举对象：公鸡数 $x$，母鸡数 $y$，小鸡数 $z$
   - 枚举范围：$0 \le x, y, z \le 100$
   - 约束条件：$5x + 3y + \frac{z}{3} = 100$ 且 $x + y + z = 100$

2. **暴力枚举**

    ```python
    class Solution:
        def buyChicken(self):
            for x in range(101):
                for y in range(101):
                    for z in range(101):
                        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100 and x + y + z == 100:
                            print("公鸡 %s 只，母鸡 %s 只，小鸡 %s 只" % (x, y, z))
    ```

3. **优化枚举效率**   
   - 利用 $z = 100 - x - y$ 减少一重循环
   - 缩小枚举范围：$x \in [0, 20]$，$y \in [0, 33]$

    ```python
    class Solution:
        def buyChicken(self):
            for x in range(21):
                for y in range(34):
                    z = 100 - x - y
                    if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
                        print("公鸡 %s 只，母鸡 %s 只，小鸡 %s 只" % (x, y, z))
    ```


## 3. 枚举算法的应用

### 3.1 经典例题：两数之和

#### 3.1.1 题目链接

- [1. 两数之和 - 力扣（LeetCode）](https://leetcode.cn/problems/two-sum/)

#### 3.1.2 题目大意

**描述**：给定一个整数数组 $nums$ 和一个整数目标值 $target$。

**要求**：在该数组中找出和为 $target$ 的两个整数，并输出这两个整数的下标。可以按任意顺序返回答案。

**说明**：

- $2 \le nums.length \le 10^4$。
- $-10^9 \le nums[i] \le 10^9$。
- $-10^9 \le target \le 10^9$。
- 只会存在一个有效答案。

**示例**：

- 示例 1：

```python
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

- 示例 2：

```python
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

#### 3.1.3 解题思路

##### 思路 1：枚举算法

1. 通过两重循环，依次枚举数组中所有可能的下标对 $(i, j)$（其中 $i < j$），判断 $nums[i] + nums[j]$ 是否等于 $target$。
2. 一旦找到满足条件的下标对，即 $nums[i] + nums[j] == target$，立即返回这两个下标 $[i, j]$ 作为答案。

##### 思路 1：代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 遍历第一个数的下标
        for i in range(len(nums)):
            # 遍历第二个数的下标（只需从i+1开始，避免和自身重复）
            for j in range(i + 1, len(nums)):
                # 判断两数之和是否等于目标值
                if nums[i] + nums[j] == target:
                    return [i, j]  # 返回下标对
        return []  # 如果没有找到，返回空列表
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 为数组 $nums$ 的元素数量。
- **空间复杂度**：$O(1)$。

### 3.2 统计平方和三元组的数目

#### 3.2.1 题目链接

- [1925. 统计平方和三元组的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-square-sum-triples/)

#### 3.2.2 题目大意

**描述**：给你一个整数 $n$。

**要求**：请你返回满足 $1 \le a, b, c \le n$ 的平方和三元组的数目。

**说明**：

- **平方和三元组**：指的是满足 $a^2 + b^2 = c^2$ 的整数三元组 $(a, b, c)$。
- $1 \le n \le 250$。

**示例**：

- 示例 1：

```python
输入 n = 5
输出 2
解释 平方和三元组为 (3,4,5) 和 (4,3,5)。
```

- 示例 2：

```python
输入：n = 10
输出：4
解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10)。
```

#### 3.2.3 解题思路

##### 思路 1：枚举算法

直接枚举 $a$ 和 $b$，计算 $c^2 = a^2 + b^2$，判断 $c$ 是否为整数且 $1 \leq c \leq n$，如果满足条件则计数加一，最后返回总数。

该方法时间复杂度为 $O(n^2)$。


- 注意：为避免浮点误差，可以用 $\sqrt{a^2 + b^2 + 1}$ 代替 $\sqrt{a^2 + b^2}$，这样判断 $c$ 是否为整数更安全。

##### 思路 1：代码

```python
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0  # 统计满足条件的三元组个数
        for a in range(1, n + 1):  # 枚举 a
            for b in range(1, n + 1):  # 枚举 b
                # 计算 c，注意加 1 防止浮点误差
                c = int(sqrt(a * a + b * b + 1))
                # 判断 c 是否在范围内，且 a^2 + b^2 == c^2
                if c <= n and a * a + b * b == c * c:
                    cnt += 1  # 满足条件，计数加一
        return cnt  # 返回最终统计结果
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

## 4. 总结

枚举算法通过遍历所有可能状态来寻找解，优点是实现简单、思路直接、正确性易于验证；缺点是在问题规模增大时时间开销迅速上升，往往无法满足效率要求。

它适用于规模较小、可快速验证答案的问题，或作为基线方案、结果校验与对拍工具。实战中应尽量结合剪枝（添加约束、提前判定不可能）、缩小搜索空间（利用对称性、边界与不变量）、降维与变量替换、以及避免重复计算等手段，显著提升效率。

实践建议是：先写出「能过的暴力正确解」，再围绕「减分支、减范围、减重算」迭代优化；当复杂度仍难以接受时，考虑切换到更合适的范式，例如哈希加速、双指针与滑动窗口、二分查找、分治、动态规划或图算法等。

## 练习题目

- [0001. 两数之和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/two-sum.md)
- [0204. 计数质数](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/count-primes.md)
- [1925. 统计平方和三元组的数目](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1900-1999/count-square-sum-triples.md)
- [2427. 公因子的数目](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2400-2499/number-of-common-factors.md)
- [LCR 180. 文件组合](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/LCR/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof.md)
- [2249. 统计圆内格点数目](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2200-2299/count-lattice-points-inside-a-circle.md)

- [枚举算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E6%9E%9A%E4%B8%BE%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)