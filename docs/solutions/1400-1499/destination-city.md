# [1436. 旅行终点站](https://leetcode.cn/problems/destination-city/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [1436. 旅行终点站 - 力扣](https://leetcode.cn/problems/destination-city/)

## 题目大意

**描述**：给定一个数组 $paths$，其中 $paths[i] = [cityA_i, cityB_i]$ 表示一条从 $cityA_i$ 到 $cityB_i$ 的直达路线。所有路线没有环。

**要求**：返回旅行的终点站（即没有出度的城市）。

**说明**：
- $1 \le paths.length \le 100$。
- 保证有且只有一个终点站。

**示例**：

- 示例 1：

```python
输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo" 
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。
```

- 示例 2：

```python
输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。
```

## 解题思路

### 思路 1：哈希集合

#### 1. 核心思想

终点站没有出度（不会作为起点出现在任何 $paths[i][0]$ 中）。将所有起点加入集合，遍历所有终点，第一个不在起点集合中的就是答案。

#### 2. 具体步骤

**第 1 步**：将所有 $paths[i][0]$ 加入 $starts$ 集合。

**第 2 步**：遍历所有 $paths[i][1]$，第一个不在 $starts$ 中的即为终点。

#### 3. 举例说明

以 $paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]$ 为例：

起点集合：$\{"London", "New York", "Lima"\}$

遍历终点："New York" 在集合中，"Lima" 在集合中，"Sao Paulo" 不在 → 返回。

### 思路 1：代码

```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {p[0] for p in paths}
        for p in paths:
            if p[1] not in starts:
                return p[1]
        return ""
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
