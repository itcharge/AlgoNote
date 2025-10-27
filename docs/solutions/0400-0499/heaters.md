# [0475. 供暖器](https://leetcode.cn/problems/heaters/)

- 标签：数组、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [0475. 供暖器 - 力扣](https://leetcode.cn/problems/heaters/)

## 题目大意

**描述**：

给定位于一条水平线上的房屋 $houses$ 和供暖器 $heaters$ 的位置。

**要求**：

冬季已经来临。 

你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
在加热器的加热半径范围内的每个房屋都可以获得供暖。

请你找出并返回可以覆盖所有房屋的最小加热半径。

**说明**：

- 注意：所有供暖器 $heaters$ 都遵循你的半径标准，加热的半径也一样。
- $1 \le houses.length, heaters.length \le 3 \times 10^{4}$。
- $1 \le houses[i], heaters[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
```

- 示例 2：

```python
输入：houses = [1,5], heaters = [2]
输出：3
```

## 解题思路

### 思路 1：排序 + 二分查找

为了能够覆盖所有房屋，我们需要找到每个房屋最近的供暖器距离，然后在这些距离中取最大值作为最小加热半径。

具体思路如下：

1. **排序**：先对房屋数组 $houses$ 和供暖器数组 $heaters$ 进行排序。
2. **二分查找**：对于每个房屋 $houses[i]$，使用二分查找找到距离它最近的供暖器位置。
3. **计算距离**：对于每个房屋，计算到最近供暖器的距离 $distance$。
4. **取最大值**：在所有距离中取最大值，即为所需的最小加热半径。

实现细节：

- 对房屋 $houses[i]$，在排序后的 $heaters$ 中二分查找第一个大于等于 $houses[i]$ 的供暖器位置 $right$。
- 计算 $houses[i]$ 到 $heaters[right]$ 的距离 $dist1$。
- 计算 $houses[i]$ 到 $heaters[right-1]$ 的距离 $dist2$（如果存在）。
- 取 $min(dist1, dist2)$ 作为当前房屋最近的供暖器距离。

### 思路 1：代码

```python
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 对房屋和供暖器进行排序
        houses.sort()
        heaters.sort()
        
        # 初始化答案为最小整数
        ans = 0
        
        # 遍历每个房屋
        for house in houses:
            # 使用二分查找找到第一个大于等于 house 的供暖器位置
            left, right = 0, len(heaters) - 1
            right_pos = len(heaters)  # 初始化右边界位置
            
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] >= house:
                    right_pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 计算到右侧供暖器的距离（如果存在）
            dist1 = abs(house - heaters[right_pos]) if right_pos < len(heaters) else float('inf')
            # 计算到左侧供暖器的距离（如果存在）
            dist2 = abs(house - heaters[right_pos - 1]) if right_pos > 0 else float('inf')
            
            # 取较小的距离作为当前房屋最近的供暖器距离
            min_dist = min(dist1, dist2)
            # 更新全局答案，取所有房屋最近供暖器距离的最大值
            ans = max(ans, min_dist)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n + m \log m)$，其中 $n$ 是房屋数量，$m$ 是供暖器数量。排序的时间复杂度为 $O(n \log n + m \log m)$，对每个房屋进行二分查找的时间复杂度为 $O(n \log m)$，总体时间复杂度为 $O(n \log n + m \log m)$。
- **空间复杂度**：$O(\log n + \log m)$，排序所需的额外空间。
