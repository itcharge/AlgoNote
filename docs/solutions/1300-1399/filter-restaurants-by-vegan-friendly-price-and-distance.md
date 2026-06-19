# [1333. 餐厅过滤器](https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/)

- 标签：数组、排序
- 难度：中等

## 题目链接

- [1333. 餐厅过滤器 - 力扣](https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/)

## 题目大意

**描述**：给定餐厅数组 $restaurants$，每个元素 $[id, rating, veganFriendly, price, distance]$。需要按条件过滤后按评分降序、ID 降序返回餐厅 ID。

过滤条件：
1. 如果 $veganFriendly = 1$，只保留 veganFriendly 为 $1$ 的餐厅。
2. 价格不超过 $maxPrice$。
3. 距离不超过 $maxDistance$。

**示例**：

- 示例 1：

```python
输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
输出：[3,1,5] 
解释： 
这些餐馆为：
餐馆 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
餐馆 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
餐馆 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
餐馆 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
餐馆 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
在按照 veganFriendly = 1, maxPrice = 50 和 maxDistance = 10 进行过滤后，我们得到了餐馆 3, 餐馆 1 和 餐馆 5（按评分从高到低排序）。
```

- 示例 2：

```python
输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
输出：[4,3,2,1,5]
解释：餐馆与示例 1 相同，但在 veganFriendly = 0 的过滤条件下，应该考虑所有餐馆。
```


## 解题思路

### 思路 1：排序 + 过滤

#### 1. 核心思想

先过滤再排序。过滤时使用列表推导，排序时按评分降序和 ID 降序。

#### 2. 具体步骤

**第 1 步**：遍历过滤。

**第 2 步**：按条件排序：$(-rating, -id)$。

**第 3 步**：提取 ID。

### 思路 1：代码

```python
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = [r for r in restaurants
                    if (veganFriendly == 0 or r[2] == 1)
                    and r[3] <= maxPrice
                    and r[4] <= maxDistance]
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        return [r[0] for r in filtered]
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log n)$。
- **空间复杂度**：$O(n)$。
