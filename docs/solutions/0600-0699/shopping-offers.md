# [0638. 大礼包](https://leetcode.cn/problems/shopping-offers/)

- 标签：位运算、记忆化搜索、数组、动态规划、回溯、状态压缩
- 难度：中等

## 题目链接

- [0638. 大礼包 - 力扣](https://leetcode.cn/problems/shopping-offers/)

## 题目大意

**描述**：

在 LeetCode 商店中，有 $n$ 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

给定一个整数数组 $price$ 表示物品价格，其中 $price[i]$ 是第 $i$ 件物品的价格。另有一个整数数组 $needs$ 表示购物清单，其中 $needs[i]$ 是需要购买第 $i$ 件物品的数量。

还有一个数组 $special$ 表示大礼包，$special[i]$ 的长度为 $n + 1$，其中 $special[i][j]$ 表示第 $i$ 个大礼包中内含第 $j$ 件物品的数量，且 $special[i][n]$ （也就是数组中的最后一个整数）为第 $i$ 个大礼包的价格。

**要求**：

返回「确切」满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。

**说明**：

- $n == price.length == needs.length$。
- $1 \le n \le 6$。
- $0 \le price[i], needs[i] \le 10$。
- $1 \le special.length \le 10^{3}$。
- $special[i].length == n + 1$。
- $0 \le special[i][j] \le 50$。
- 生成的输入对于 $0 \le j \le n - 1$ 至少有一个 $special[i][j]$ 非零。

**示例**：

- 示例 1：

```python
输入：price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
输出：14
解释：有 A 和 B 两种物品，价格分别为 ¥2 和 ¥5 。 
大礼包 1 ，你可以以 ¥5 的价格购买 3A 和 0B 。 
大礼包 2 ，你可以以 ¥10 的价格购买 1A 和 2B 。 
需要购买 3 个 A 和 2 个 B ， 所以付 ¥10 购买 1A 和 2B（大礼包 2），以及 ¥4 购买 2A 。
```

- 示例 2：

```python
输入：price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
输出：11
解释：A ，B ，C 的价格分别为 ¥2 ，¥3 ，¥4 。
可以用 ¥4 购买 1A 和 1B ，也可以用 ¥9 购买 2A ，2B 和 1C 。 
需要买 1A ，2B 和 1C ，所以付 ¥4 买 1A 和 1B（大礼包 1），以及 ¥3 购买 1B ， ¥4 购买 1C 。 
不可以购买超出待购清单的物品，尽管购买大礼包 2 更加便宜。
```

## 解题思路

### 思路 1：记忆化搜索

这道题目要求计算满足购物清单的最低价格。可以使用记忆化搜索（动态规划）来避免重复计算。

1. 首先过滤掉不划算的大礼包（大礼包价格大于等于单独购买的价格）。
2. 使用记忆化搜索，状态为当前的购物需求 $needs$。
3. 对于每个状态，有两种选择：
   - 不使用大礼包，直接按单价购买所有物品。
   - 尝试使用每个大礼包，如果大礼包中的物品数量不超过需求，则使用该大礼包，并递归计算剩余需求的最低价格。
4. 返回所有选择中的最小值。

### 思路 1：代码

```python
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        from functools import lru_cache
        
        n = len(price)
        
        # 过滤掉不划算的大礼包
        filtered_special = []
        for offer in special:
            # 计算大礼包的原价
            original_price = sum(offer[i] * price[i] for i in range(n))
            # 如果大礼包价格更优惠，保留
            if offer[n] < original_price:
                filtered_special.append(offer)
        
        @lru_cache(None)
        def dfs(needs_tuple):
            needs = list(needs_tuple)
            
            # 不使用大礼包，直接购买
            min_cost = sum(needs[i] * price[i] for i in range(n))
            
            # 尝试使用每个大礼包
            for offer in filtered_special:
                # 检查是否可以使用该大礼包
                can_use = True
                new_needs = []
                for i in range(n):
                    if needs[i] < offer[i]:
                        can_use = False
                        break
                    new_needs.append(needs[i] - offer[i])
                
                if can_use:
                    # 使用该大礼包，递归计算剩余需求
                    min_cost = min(min_cost, offer[n] + dfs(tuple(new_needs)))
            
            return min_cost
        
        return dfs(tuple(needs))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times k^n)$，其中 $m$ 是大礼包的数量，$n$ 是物品的种类，$k$ 是每种物品的最大需求量。状态数最多为 $k^n$，每个状态需要尝试 $m$ 个大礼包。
- **空间复杂度**：$O(k^n)$，需要使用记忆化存储所有状态的结果。
