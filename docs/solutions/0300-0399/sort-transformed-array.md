# [0360. 有序转化数组](https://leetcode.cn/problems/sort-transformed-array/)

- 标签：数组、数学、双指针、排序
- 难度：中等

## 题目链接

- [0360. 有序转化数组 - 力扣](https://leetcode.cn/problems/sort-transformed-array/)

## 题目大意

**描述**：给定一个已经排好的整数数组 $nums$ 和整数 $a$、$b$、$c$。

**要求**：对于数组中的每一个数 $x$，计算函数值 $f(x) = ax^2 + bx + c$，请将函数值产生的数组返回。

**说明**：

- 返回的这个数组必须按照升序排列，并且我们所期望的解法时间复杂度为 $O(n)$。
- $1 \le nums.length \le 200$。
- $-100 \le nums[i], a, b, c \le 100$。
- $nums$ 按照升序排列。

**示例**：

- 示例 1：

```python
输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
输出: [3,9,15,33]
```

- 示例 2：

```python
输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
输出: [-23,-5,1,7]
```

## 解题思路

### 思路 1： 数学 + 对撞指针

这是一道数学题。需要根据一元二次函数的性质来解决问题。因为返回的数组必须按照升序排列，并且期望的解法时间复杂度为 $O(n)$。这就不能先计算再排序了，而是要在线性时间复杂度内考虑问题。

我们先定义一个函数用来计算 $f(x)$。然后进行分情况讨论。

- 如果 $a == 0$，说明函数是一条直线。则根据 $b$ 值的正负来确定数组遍历顺序。
  - 如果 $b \ge 0$，说明这条直线是一条递增直线。则按照从头到尾的顺序依次计算函数值，并依次存入答案数组。
  - 如果 $b < 0$，说明这条直线是一条递减直线。则按照从尾到头的顺序依次计算函数值，并依次存入答案数组。
- 如果 $a > 0$，说明函数是一条开口向上的抛物线，最小值横坐标为 $diad = \frac{-b}{2.0 * a}$，离 diad 越远，函数值越大。则可以使用双指针从远到近，由大到小依次填入数组。具体步骤如下：
  - 使用双指针 $left$、$right$，令 $left$ 指向数组第一个元素位置，$right$ 指向数组最后一个元素位置。再定义 $index = len(nums) - 1$ 作为答案数组填入顺序的索引值。
  - 比较 $left - diad$ 与 $right - diad$ 的绝对值大小。大的就是目前距离 $diad$ 最远的那个。
    - 如果 $abs(nums[left] - diad)$ 更大，则将其填入答案数组对应位置，并令 $left += 1$。
    - 如果 $abs(nums[right] - diad)$ 更大，则将其填入答案数组对应位置，并令 $right -= 1$。
    - 令 $index -= 1$。
  - 直到 $left == right$，最后将 $nums[left]$ 填入答案数组对应位置。
- 如果 $a < 0$，说明函数是一条开口向下的抛物线，最大值横坐标为 $diad = \frac{-b}{2.0 * a}$，离 diad 越远，函数值越小。则可以使用双指针从远到近，由小到大一次填入数组。具体步骤如下：
  - 使用双指针 $left$、$right$，令 $left$ 指向数组第一个元素位置，$right$ 指向数组最后一个元素位置。再定义 $index = 0$ 作为答案数组填入顺序的索引值。
  - 比较 $left - diad$ 与 $right - diad$ 的绝对值大小。大的就是目前距离 $diad$ 最远的那个。
    - 如果 $abs(nums[left] - diad)$ 更大，则将其填入答案数组对应位置，并令 $left += 1$。
    - 如果 $abs(nums[right] - diad)$ 更大，则将其填入答案数组对应位置，并令 $right -= 1$。
    - 令 $index += 1$。
  - 直到 $left == right$，最后将 $nums[left]$ 填入答案数组对应位置。

### 思路 1：代码

```python
class Solution:
    def calFormula(self, x, a, b, c):
        return a * x * x + b * x + c

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        size = len(nums)
        res = [0 for _ in range(size)]

        # 直线
        if a == 0:
            if b >= 0:
                index = 0
                for i in range(size):
                    res[index] = self.calFormula(nums[i], a, b, c)
                    index += 1
            else:
                index = 0
                for i in range(size - 1, -1, -1):
                    res[index] = self.calFormula(nums[i], a, b, c)
                    index += 1
        else:
            diad = -(b / (2.0 * a))
            left, right = 0, size - 1

            if a > 0:
                index = size - 1
                while left < right:
                    if abs(diad - nums[left]) > abs(diad - nums[right]):
                        res[index] = self.calFormula(nums[left], a, b, c)
                        left += 1
                    else:
                        res[index] = self.calFormula(nums[right], a, b, c)
                        right -= 1
                    index -= 1
                res[index] = self.calFormula(nums[left], a, b, c)
            else:
                diad = -(b / (2.0 * a))
                left, right = 0, size - 1
                index = 0
                while left < right:
                    if abs(diad - nums[left]) > abs(diad - nums[right]):
                        res[index] = self.calFormula(nums[left], a, b, c)
                        left += 1
                    else:
                        res[index] = self.calFormula(nums[right], a, b, c)
                        right -= 1
                    index += 1
                res[index] = self.calFormula(nums[left], a, b, c)
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$，不考虑最终返回值的空间占用。

