# [1475. 商品折扣后的最终价格](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/)

- 标签：栈、数组、单调栈
- 难度：简单

## 题目链接

- [1475. 商品折扣后的最终价格 - 力扣](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/)

## 题目大意

**描述**：给定一个数组 $prices$，其中 $prices[i]$ 表示第 $i$ 件商品的价格。对第 $i$ 件商品，可以享受一个折扣：找到 $j > i$ 中第一个 $prices[j] \le prices[i]$ 的商品，折扣为 $prices[j]$。

**要求**：返回最终价格数组（原价 - 折扣）。如果没有符合条件的 $j$，则无折扣。

**示例**：

- 示例 1：

```python
输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
```

- 示例 2：

```python
输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。
```

## 解题思路

### 思路 1：单调栈

#### 1. 核心思想

对每个 $i$，找右边第一个 $\le prices[i]$ 的元素。这是单调栈的经典应用，维护一个单调递增栈（从栈底到栈顶递增）。

#### 2. 具体步骤

**第 1 步**：初始化 $ans = prices$ 的副本，空栈。

**第 2 步**：遍历 $i = 0 \to n-1$：
- 当栈不空且 $prices[stack[-1]] \ge prices[i]$ 时，栈顶元素找到了右边第一个 $\le$ 它的元素，$ans[stack[-1]] -= prices[i]$，弹出栈顶。
- 将 $i$ 入栈。

**第 3 步**：返回 $ans$。

#### 3. 举例说明

以 $prices = [8, 4, 6, 2, 3]$ 为例：

- $i=0$：栈空，入栈 $[0]$
- $i=1$：$prices[0]=8 \ge 4$，$ans[0]=8-4=4$，弹出 0，入栈 $[1]$
- $i=2$：$prices[1]=4 < 6$，入栈 $[1,2]$
- $i=3$：$prices[2]=6 \ge 2$，$ans[2]=6-2=4$，弹出 2；$prices[1]=4 \ge 2$，$ans[1]=4-2=2$，弹出 1；入栈 $[3]$
- $i=4$：$prices[3]=2 < 3$，入栈 $[3,4]$

结果：$[4, 2, 4, 2, 3]$。

### 思路 1：代码

```python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = prices[:]
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] -= prices[i]
            stack.append(i)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个元素入栈出栈各一次。
- **空间复杂度**：$O(n)$。
