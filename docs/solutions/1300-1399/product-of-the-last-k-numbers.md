# [1352. 最后 K 个数的乘积](https://leetcode.cn/problems/product-of-the-last-k-numbers/)

- 标签：设计、队列、数组、数学、数据流
- 难度：中等

## 题目链接

- [1352. 最后 K 个数的乘积 - 力扣](https://leetcode.cn/problems/product-of-the-last-k-numbers/)

## 题目大意

**描述**：实现一个 `ProductOfNumbers` 类，支持以下操作：
- `ProductOfNumbers()` 初始化对象。
- `add(int num)` 将数字 $num$ 添加到当前数字列表末尾。
- `getProduct(int k)` 返回当前列表中最后 $k$ 个数字的乘积。

**说明**：
- $0 \le num \le 100$。
- $1 \le k \le 4 \times 10^4$。
- 最多调用 $add$ 和 $getProduct$ 共 $4 \times 10^4$ 次。

**示例**：

- 示例 1：

```python
输入：
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

输出：
[null,null,null,null,null,null,20,40,0,null,32]

解释：
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32
```


## 解题思路

### 思路 1：前缀积

#### 1. 核心思想

如果所有数字都 $\ge 1$，可以用前缀积数组轻松求解：
- $prefix[i]$ 表示前 $i$ 个数的乘积
- 最后 $k$ 个数的乘积 = $prefix[n] \; / \; prefix[n-k]$

但本题允许 $num = 0$。加入 $0$ 后，从 $0$ 之后的所有前缀积都会变成 $0$。

解决方法：遇到 $0$ 时重置前缀积数组，清空之前的积累。这样 $getProduct$ 时只需检查 $k$ 是否超出数组范围。

#### 2. 具体步骤

**初始化**：
- $prefix = [1]$，存储前缀积。初始 $1$ 表示空集的乘积。

**$add(num)$**：
- 如果 $num == 0$：重置 $prefix = [1]$（之前的所有积累作废）
- 否则：$prefix.append(prefix[-1] \times num)$

**$getProduct(k)$**：
- 如果 $k \ge len(prefix)$：说明最后 $k$ 个数中包含了 $0$，返回 $0$
- 否则：返回 $prefix[-1] \; / \; prefix[-k-1]$

#### 3. 正确性证明

遇到 $0$ 时重置是核心所在。因为 $0$ 之后的乘积不受 $0$ 之前数字的影响（任何数乘 $0$ 都是 $0$），而且题目只要求最后 $k$ 个数的乘积。如果 $k$ 跨过了 $0$ 的位置，结果必然是 $0$。

#### 4. 举例说明

以操作序列 `add(2), add(3), add(0), add(5), add(4), getProduct(2), getProduct(3)` 为例：

| 操作 | prefix 数组 |
| --- | ---------- |
| 初始 | [1] |
| add(2) | [1, 2] |
| add(3) | [1, 2, 6] |
| add(0) | [1]（重置） |
| add(5) | [1, 5] |
| add(4) | [1, 5, 20] |
| getProduct(2) | 20 / 5 = 4 |
| getProduct(3) | k=3 ≥ len(prefix)=3，返回 0 |

### 思路 1：代码

```python
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]  # 前缀积

    def add(self, num: int) -> None:
        if num == 0:
            # 遇到 0，重置前缀积
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0  # 最后 k 个数包含 0
        return self.prefix[-1] // self.prefix[-k - 1]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$，$add$ 和 $getProduct$ 都是 $O(1)$ 时间。
- **空间复杂度**：$O(n)$，其中 $n$ 是当前列表中非零连续数字的个数（重置清零）。

---

### 思路 2：对比与总结

本题的关键点在于 $num$ 可能为 $0$。如果数字范围保证 $num \ge 1$，则直接使用标准前缀积即可。遇到 $0$ 的重置策略是本题的巧妙之处，将问题限制在非零区间内解决，$getProduct$ 时边界判断保证正确性。
