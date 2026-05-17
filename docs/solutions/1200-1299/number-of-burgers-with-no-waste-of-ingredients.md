# [1276. 不浪费原料的汉堡制作方案](https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/)

- 标签：数学
- 难度：中等

## 题目链接

- [1276. 不浪费原料的汉堡制作方案 - 力扣](https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/)

## 题目大意

**描述**：给定两个整数 $tomatoSlices$ 和 $cheeseSlices$，分别表示番茄片和奶酪片的数量。制作一个巨无霸汉堡需要 $4$ 片番茄和 $1$ 片奶酪，制作一个小皇堡需要 $2$ 片番茄和 $1$ 片奶酪。

**要求**：返回 $[total\_jumbo, total\_small]$ 使得恰好用完所有原料。如果无法恰好用完，返回 $[]$。

**说明**：

- $0 \le tomatoSlices \le 10^{7}$。
- $0 \le cheeseSlices \le 10^{7}$。

**示例**：

- 示例 1：

```python
输入：tomatoSlices = 16, cheeseSlices = 7
输出：[1, 6]
解释：制作 1 个巨无霸和 6 个小皇堡需要 4×1+2×6=16 片番茄和 1+6=7 片奶酪。
```

- 示例 2：

```python
输入：tomatoSlices = 17, cheeseSlices = 4
输出：[]
解释：只靠整数个汉堡无法恰好用完。
```

- 示例 3：

```python
输入：tomatoSlices = 4, cheeseSlices = 17
输出：[]
```

## 解题思路

### 思路 1：数学解方程组

#### 1. 核心思想

这是一道经典的**鸡兔同笼**问题（二元一次方程组）。

设巨无霸汉堡数量为 $x$，小皇堡数量为 $y$。根据题意：

$$
\begin{cases}
4x + 2y = tomatoSlices \\
x + y = cheeseSlices
\end{cases}
$$

解方程组：

由第二个方程得 $y = cheeseSlices - x$，代入第一个方程：
$$4x + 2(cheeseSlices - x) = tomatoSlices$$
$$4x + 2 \times cheeseSlices - 2x = tomatoSlices$$
$$2x = tomatoSlices - 2 \times cheeseSlices$$
$$x = \frac{tomatoSlices - 2 \times cheeseSlices}{2}$$

$$y = cheeseSlices - x$$

#### 2. 合法解的条件

解必须满足：
1. $x$ 是非负整数：$tomatoSlices - 2 \times cheeseSlices$ 必须是偶数且 $\ge 0$。
2. $y$ 是非负整数。
3. 代入验证原方程（确保 $4x + 2y = tomatoSlices$，但根据推导，条件 1 已经隐含了这个等式的正确性）。

#### 3. 具体步骤

**第 1 步**：计算 $x = (tomatoSlices - 2 \times cheeseSlices) / 2$。

**第 2 步**：如果 $x$ 是偶数且 $\ge 0$，且 $y = cheeseSlices - x \ge 0$，返回 $[x, y]$。

**第 3 步**：否则返回 $[]$。

#### 4. 结合示例走一遍

$tomatoSlices = 16, cheeseSlices = 7$

$$x = \frac{16 - 2 \times 7}{2} = \frac{2}{2} = 1$$
$$y = 7 - 1 = 6$$

$x \ge 0$，$y \ge 0$，返回 $[1, 6]$。

$tomatoSlices = 17, cheeseSlices = 4$

$$x = \frac{17 - 2 \times 4}{2} = \frac{9}{2} = 4.5$$

$x$ 不是整数，返回 $[]$。

### 思路 1：代码

```python
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 解方程组
        # 4x + 2y = tomato
        # x + y = cheese
        if (tomatoSlices - 2 * cheeseSlices) % 2 != 0:
            return []
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        if x >= 0 and y >= 0:
            return [x, y]
        return []
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，只需常数次计算。
- **空间复杂度**：$O(1)$，只使用常数个变量。
