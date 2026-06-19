# [1357. 每隔 n 个顾客打折](https://leetcode.cn/problems/apply-discount-every-n-orders/)

- 标签：设计、数组、哈希表
- 难度：中等

## 题目链接

- [1357. 每隔 n 个顾客打折 - 力扣](https://leetcode.cn/problems/apply-discount-every-n-orders/)

## 题目大意

**描述**：实现一个收银系统 $Cashier$，支持以下功能：
- 构造函数：接收 $n$（打折间隔）、$discount$（折扣百分比）、$products$（商品 ID 列表）、$prices$（商品价格列表）。
- $getBill(product, amounts)$：顾客购买的商品 ID 列表和对应数量列表。如果是第 $n$ 个顾客，总价享受 $discount$ 折扣（即总价乘以 $(100 - discount) / 100$）。

**要求**：正确计算每位顾客的账单。

**说明**：
- $1 \le n \le 10^4$。
- $0 \le discount \le 100$。
- $1 \le products.length \le 200$。
- $1 \le prices[i] \le 10^3$。
- 最多调用 $1000$ 次 $getBill$。

**示例**：

- 示例 1：

```python
输入
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
输出
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
解释
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // 返回 500.0, 账单金额为 = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // 返回 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // 返回 800.0 ，账单原本为 1600.0 ，但由于该顾客是第三位顾客，他将得到 50% 的折扣，所以实际金额为 1600 - 1600 * (50 / 100) = 800 。
cashier.getBill([4],[10]);                           // 返回 4000.0
cashier.getBill([7,3],[10,10]);                      // 返回 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // 返回 7350.0 ，账单原本为 14700.0 ，但由于系统计数再次达到三，该顾客将得到 50% 的折扣，实际金额为 7350.0 。
cashier.getBill([2,3,5],[5,3,2]);                    // 返回 2500.0
```

- 示例 2：

```python
输入：
输出：
```


## 解题思路

### 思路 1：哈希表 + 计数器

#### 1. 核心思想

用哈希表将商品 ID 映射到价格，用计数器记录当前是第几位顾客。当计数器为 $n$ 的倍数时，应用折扣。

#### 2. 具体步骤

**第 1 步**：在构造函数中：
- 用字典 $price\_map$ 存储 $product \to price$ 的映射。
- 记录 $n$ 和 $discount$。
- 初始化计数器 $counter = 0$。

**第 2 步**：在 $getBill$ 中：
- $counter += 1$。
- 遍历 $product$ 和 $amounts$，计算总价 $total = \sum price\_map[p] \times amount$。
- 如果 $counter \% n == 0$，$total = total \times (100 - discount) / 100$。
- 返回 $total$。

### 思路 1：代码

```python
class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.price_map = {}
        for p, price in zip(products, prices):
            self.price_map[p] = price
        self.counter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        total = 0
        for p, a in zip(product, amount):
            total += self.price_map[p] * a
        if self.counter % self.n == 0:
            total *= (100 - self.discount) / 100
        return total
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(L)$，$L$ 是每次购买的商品数量。
- **空间复杂度**：$O(P)$，$P$ 是商品种类数。
