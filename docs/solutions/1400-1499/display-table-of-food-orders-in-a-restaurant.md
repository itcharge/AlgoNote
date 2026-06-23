# [1418. 点菜展示表](https://leetcode.cn/problems/display-table-of-food-orders-in-a-restaurant/)

- 标签：数组、哈希表、字符串、有序集合、排序
- 难度：中等

## 题目链接

- [1418. 点菜展示表 - 力扣](https://leetcode.cn/problems/display-table-of-food-orders-in-a-restaurant/)

## 题目大意

**描述**：给定一个订单列表 $orders$，每个订单 $orders[i] = [customerName_i, tableNumber_i, foodItem_i]$。

**要求**：返回点菜展示表。表的第一行是表头 `"Table"` 后跟所有菜品名称（按字母序升序）。后续每行对应一个餐桌号（升序），每行第一个是该桌号，然后是该桌每个菜品的点餐数量。

**说明**：
- $1 \le orders.length \le 5000$。

**示例**：

- 示例 1：

```python
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
解释：
点菜展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
餐桌 10：Corina 点了 "Beef Burrito"
```

- 示例 2：

```python
输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
解释：
对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles"
而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken"
```

## 解题思路

### 思路 1：哈希表统计

#### 1. 核心思想

用哈希表 $food\_set$ 收集所有菜品名称，用 $table\_orders[table][food]$ 统计每个桌每个菜品的数量。

#### 2. 具体步骤

**第 1 步**：遍历 $orders$：
- 将 $foodItem$ 加入 $food\_set$。
- $table\_orders[table][food] += 1$。

**第 2 步**：排序 $food\_set$ 得到表头。

**第 3 步**：排序餐桌号，对每个桌号，按表头顺序输出数量（不存在则为 $0$）。

#### 3. 举例说明

以 $orders = [["David","3","Ceviche"],["Corina","10","Beef"],["David","3","Fried"],...]$ 为例：

菜品集合（排序后）：$["Beef","Ceviche","Fried Chicken","Water"]$

餐桌 $3$：$\{"Ceviche": 1, "Fried Chicken": 1\}$
餐桌 $10$：$\{"Beef": 1, "Ceviche": 1, "Water": 1\}$

输出：
```
[["Table","Beef","Ceviche","Fried Chicken","Water"],
 ["3","0","1","1","0"],
 ["10","1","1","0","1"]]
```

### 思路 1：代码

```python
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_set = set()
        table_orders = {}

        for _, table, food in orders:
            food_set.add(food)
            if table not in table_orders:
                table_orders[table] = {}
            table_orders[table][food] = table_orders[table].get(food, 0) + 1

        # 表头
        foods = sorted(food_set)
        header = ["Table"] + foods

        # 按桌号排序（转为整数排序）
        result = [header]
        for table in sorted(table_orders.keys(), key=int):
            row = [table]
            orders_for_table = table_orders[table]
            for food in foods:
                row.append(str(orders_for_table.get(food, 0)))
            result.append(row)

        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + F \log F + T \times F)$，其中 $n$ 是订单数，$F$ 是菜品数，$T$ 是桌数。
- **空间复杂度**：$O(T \times F)$。
