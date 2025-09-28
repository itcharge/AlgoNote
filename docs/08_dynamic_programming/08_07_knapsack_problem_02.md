## 1. 完全背包问题简介

> **完全背包问题**：给定 $n$ 种物品和一个最大承重为 $W$ 的背包。每种物品的重量为 $weight[i]$，价值为 $value[i]$，且每种物品的数量不限。请问在不超过背包承重上限的前提下，背包内可获得的最大总价值是多少？

![完全背包问题](https://qcdn.itcharge.cn/images/20240514111640.png)

## 2. 完全背包问题的基本思路

> **完全背包问题的核心特性**：每种物品可以选取任意多次（数量无限）。

完全背包问题与 0-1 背包问题的状态定义和基本思路类似，不同之处在于每种物品可以被多次选择。对于容量为 $w$ 的背包，第 $i - 1$ 种物品最多可以选择 $\left\lfloor \frac{w}{weight[i - 1]} \right\rfloor$ 件。因此，可以在动态规划的基础上增加一层循环，枚举第 $i - 1$ 种物品的选取数量 $k$（$0 \leq k \leq \left\lfloor \frac{w}{weight[i - 1]} \right\rfloor$），从而将完全背包问题转化为多重选择的 0-1 背包问题模型。

#### 思路 1：动态规划 + 二维数组基础解法

###### 1. 阶段划分

以物品种类序号和当前背包剩余容量作为阶段。

###### 2. 定义状态

设 $dp[i][w]$ 表示前 $i$ 种物品，放入容量不超过 $w$ 的背包时可获得的最大价值。

其中 $i$ 表示考虑前 $i$ 种物品，$w$ 表示当前背包容量。

###### 3. 状态转移方程

由于每种物品可以选取任意多次，$dp[i][w]$ 可以通过枚举第 $i - 1$ 种物品的选取数量 $k$ 得到：

- 选 $0$ 件第 $i - 1$ 种物品：$dp[i - 1][w]$
- 选 $1$ 件第 $i - 1$ 种物品：$dp[i - 1][w - weight[i - 1]] + value[i - 1]$
- 选 $2$ 件第 $i - 1$ 种物品：$dp[i - 1][w - 2 \times weight[i - 1]] + 2 \times value[i - 1]$
- ...
- 选 $k$ 件第 $i - 1$ 种物品：$dp[i - 1][w - k \times weight[i - 1]] + k \times value[i - 1]$

其中 $0 \leq k \leq \left\lfloor \frac{w}{weight[i-1]} \right\rfloor$。

因此，状态转移方程为：

$$
dp[i][w] = \max_{0 \leq k \leq \left\lfloor \frac{w}{weight[i-1]} \right\rfloor} \left\{ dp[i-1][w - k \times weight[i-1]] + k \times value[i-1] \right\}
$$

###### 4. 初始条件

- 对所有 $0 \leq i \leq size$，$dp[i][0] = 0$，即背包容量为 $0$ 时最大价值为 $0$。
- 对所有 $0 \leq w \leq W$，$dp[0][w] = 0$，即没有物品时最大价值为 $0$。

###### 5. 最终结果

最终答案为 $dp[size][W]$，即用前 $size$ 种物品、背包容量为 $W$ 时能获得的最大价值。

#### 思路 1：代码

```python
class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def completePackMethod1(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(w // weight[i - 1] + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
        
        return dp[size][W]
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times W \times \sum\frac{W}{weight[i]})$，其中 $n$ 为物品种类数量，$W$ 为背包的载重上限，$weight[i]$ 是第 $i$ 种物品的重量。
- **空间复杂度**：$O(n \times W)$。

## 3. 完全背包问题的状态转移方程优化

在前面的解法中，对于每种物品，我们都需要枚举所有可能的选取数量 $k$，这导致时间复杂度较高。

实际上，我们可以对状态转移方程进行优化，从而显著降低算法的时间复杂度。

原始的状态转移方程为：

$$
dp[i][w] = \max_{0 \leq k \leq \left\lfloor \frac{w}{weight[i-1]} \right\rfloor} \left\{ dp[i-1][w - k \times weight[i-1]] + k \times value[i-1] \right\}
$$

将其展开，可以得到：

$$(1)\quad dp[i][w] = \max \begin{cases}
dp[i-1][w] \\
dp[i-1][w - weight[i-1]] + value[i-1] \\
dp[i-1][w - 2 \times weight[i-1]] + 2 \times value[i-1] \\
\cdots \\
dp[i-1][w - k \times weight[i-1]] + k \times value[i-1]
\end{cases},\quad 0 \leq k \leq \left\lfloor \frac{w}{weight[i-1]} \right\rfloor$$

再来看 $dp[i][w - weight[i-1]]$ 的展开：

$$(2)\quad dp[i][w - weight[i-1]] = \max \begin{cases}
dp[i-1][w - weight[i-1]] \\
dp[i-1][w - 2 \times weight[i-1]] + value[i-1] \\
dp[i-1][w - 3 \times weight[i-1]] + 2 \times value[i-1] \\
\cdots \\
dp[i-1][w - k \times weight[i-1]] + (k-1) \times value[i-1]
\end{cases}$$

对比 $(1)$ 和 $(2)$ 可以发现：

1. $(1)$ 有 $k+1$ 项，$(2)$ 有 $k$ 项；
2. $(1)$ 的第 $2$ 到第 $k+1$ 项，与 $(2)$ 的所有项一一对应，且每项多了一个 $value[i-1]$。

因此，将 $(2)$ 式加上 $value[i-1]$，再与 $(1)$ 式合并，可以得到优化后的状态转移方程：

$$(3)\quad dp[i][w] = \max \left\{ dp[i-1][w],\ dp[i][w - weight[i-1]] + value[i-1] \right\},\quad w \geq weight[i-1]$$

这样，原本需要三重循环的解法，优化为只需两重循环即可，大大提升了效率。

> 注意：当 $w < weight[i-1]$ 时，$dp[i][w] = dp[i-1][w]$，即当前物品无法放入背包。

因此，最终的状态转移方程为：

$$
dp[i][w] = 
\begin{cases}
dp[i-1][w] & w < weight[i-1] \\
\max\left\{ dp[i-1][w],\ dp[i][w - weight[i-1]] + value[i-1] \right\} & w \geq weight[i-1]
\end{cases}
$$

可以看到，这个状态转移方程与 0-1 背包问题的状态转移方程非常相似。

> 唯一的区别在于：
>
> 1. 0-1 背包问题中，转移用的是 $dp[i-1][w - weight[i-1]] + value[i-1]$，即上一阶段的状态；
> 2. 完全背包问题中，转移用的是 $dp[i][w - weight[i-1]] + value[i-1]$，即当前阶段的状态。

#### 思路 2：动态规划 + 状态转移方程优化

###### 1. 阶段划分

按照物品种类的序号、当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[i][w]$ 表示为：前 $i$ 种物品放入一个最多能装重量为 $w$ 的背包中，可以获得的最大价值。

状态 $dp[i][w]$ 是一个二维数组，其中第一维代表「当前正在考虑的物品种类」，第二维表示「当前背包的载重上限」，二维数组值表示「可以获得的最大价值」。

###### 3. 状态转移方程

$\quad dp[i][w] = \begin{cases}  dp[i - 1][w] & w < weight[i - 1] \cr max \lbrace dp[i - 1][w], \quad dp[i][w - weight[i - 1]] + value[i - 1]  \rbrace & w \ge weight[i - 1] \end{cases}$

###### 4. 初始条件

- 如果背包载重上限为 $0$，则无论选取什么物品，可以获得的最大价值一定是 $0$，即 $dp[i][0] = 0, 0 \le i \le size$。
- 无论背包载重上限是多少，前 $0$ 种物品所能获得的最大价值一定为 $0$，即 $dp[0][w] = 0, 0 \le w \le W$。

###### 5. 最终结果

根据我们之前定义的状态，$dp[i][w]$ 表示为：前 $i$ 种物品放入一个最多能装重量为 $w$ 的背包中，可以获得的最大价值。则最终结果为 $dp[size][W]$，其中 $size$ 为物品的种类数，$W$ 为背包的载重上限。

#### 思路 2：代码

```python
class Solution:
    # 思路 2：动态规划 + 状态转移方程优化
    def completePackMethod2(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                else:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                    dp[i][w] = max(dp[i - 1][w], dp[i][w - weight[i - 1]] + value[i - 1])
                    
        return dp[size][W]
```

#### 思路 2：复杂度分析

- **时间复杂度**：$O(n \times W)$，其中 $n$ 为物品种类数量，$W$ 为背包的载重上限。
- **空间复杂度**：$O(n \times W)$。

## 4. 完全背包问题的滚动数组优化

通过观察「思路 2」中的状态转移方程 

$dp[i][w] = \begin{cases}  dp[i - 1][w] & w < weight[i - 1] \cr max \lbrace dp[i - 1][w], \quad dp[i][w - weight[i - 1]] + value[i - 1]  \rbrace & w \ge weight[i - 1] \end{cases}$

可以看出：我们只用到了当前行（第 $i$ 行）的 $dp[i][w]$、$dp[i][w - weight[i - 1]]$，以及上一行（第 $i - 1$ 行）的 $dp[i - 1][w]$。

所以我们没必要保存所有阶段的状态，只需要使用一个一维数组 $dp[w]$ 保存上一阶段的所有状态，采用使用「滚动数组」的方式对空间进行优化（去掉动态规划状态的第一维）。

#### 思路 3：动态规划 + 滚动数组优化

###### 1. 阶段划分

按照当前背包的载重上限进行阶段划分。

###### 2. 定义状态

定义状态 $dp[w]$ 表示为：将物品装入最多能装重量为 $w$ 的背包中，可以获得的最大价值。

###### 3. 状态转移方程

$dp[w] = \begin{cases}  dp[w] & w < weight[i - 1] \cr max \lbrace dp[w], \quad dp[w - weight[i - 1]]  + value[i - 1] \rbrace & w \ge weight[i - 1] \end{cases}$

> 注意：这里的 $dp[w - weight[i - 1]]$ 是第 $i$ 轮计算之后的「第 $i$ 阶段的状态值」。

因为在计算 $dp[w]$ 时，我们需要用到第 $i$ 轮计算之后的 $dp[w - weight[i - 1]]$，所以我们需要按照「从 $0 \sim W$ 正序递推的方式」递推 $dp[w]$，这样才能得到正确的结果。

因为 $w < weight[i - 1]$ 时，$dp[w]$ 只能取上一阶段的 $dp[w]$，其值相当于没有变化，这部分可以不做处理。所以我们在正序递推 $dp[w]$ 时，只需从 $weight[i - 1]$ 开始遍历即可。

###### 4. 初始条件

- 无论背包载重上限为多少，只要不选择物品，可以获得的最大价值一定是 $0$，即 $dp[w] = 0, 0 \le w \le W$。

###### 5. 最终结果

根据我们之前定义的状态， $dp[w]$ 表示为：将物品装入最多能装重量为 $w$ 的背包中，可以获得的最大价值。则最终结果为 $dp[W]$，其中 $W$ 为背包的载重上限。

#### 思路 3：代码

```python
class Solution:
    # 思路 3：动态规划 + 滚动数组优化
    def completePackMethod3(self, weight: [int], value: [int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                
        return dp[W]
```

> 通过观察「0-1 背包问题滚动数组优化的代码」和「完全背包问题滚动数组优化的代码」可以看出，两者的唯一区别在于：
>
> 1. 0-1 背包问题滚动数组优化的代码采用了「从 $W \sim weight[i - 1]$ 逆序递推的方式」。
> 2. 完全背包问题滚动数组优化的代码采用了「从 $weight[i - 1] \sim W$ 正序递推的方式」。

#### 思路 3：复杂度分析

- **时间复杂度**：$O(n \times W)$，其中 $n$ 为物品种类数量，$W$ 为背包的载重上限。
- **空间复杂度**：$O(W)$。

## 练习题目

- [0279. 完全平方数](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0200-0299/perfect-squares.md)
- [0322. 零钱兑换](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/coin-change.md)
- [0518. 零钱兑换 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0500-0599/coin-change-ii.md)
- [0377. 组合总和 IV](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0300-0399/combination-sum-iv.md)

- [完全背包问题题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E9%A2%98%E7%9B%AE)

## 参考资料

- 【资料】[背包九讲 - 崔添翼](https://github.com/tianyicui/pack)
- 【文章】[背包 DP - OI Wiki](https://oi-wiki.org/dp/knapsack/)
- 【文章】[背包问题 第四讲 - 宫水三叶的刷题日记](https://juejin.cn/post/7003243733604892685)
- 【题解】[『 套用完全背包模板 』详解完全背包（含数学推导） - 完全平方数 - 力扣](https://leetcode.cn/problems/perfect-squares/solution/by-flix-sve5/)
- 【题解】[『 一文搞懂完全背包问题 』从0-1背包到完全背包，逐层深入+推导 - 零钱兑换 - 力扣](https://leetcode.cn/problems/coin-change/solution/by-flix-su7s/)