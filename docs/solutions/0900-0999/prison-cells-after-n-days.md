# [0957. N 天后的牢房](https://leetcode.cn/problems/prison-cells-after-n-days/)

- 标签：位运算、数组、哈希表、数学
- 难度：中等

## 题目链接

- [0957. N 天后的牢房 - 力扣](https://leetcode.cn/problems/prison-cells-after-n-days/)

## 题目大意

**描述**：

监狱中 8 间牢房排成一排，每间牢房可能被占用或空置。

每天，无论牢房是被占用或空置，都会根据以下规则进行变更：

- 如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
- 否则，它就会被空置。

注意：由于监狱中的牢房排成一行，所以行中的第一个和最后一个牢房不存在两个相邻的房间。

给你一个整数数组 $cells$，用于表示牢房的初始状态：如果第 $i$ 间牢房被占用，则 $cell[i]==1$，否则 $cell[i]==0$。另给你一个整数 $n$。

**要求**：

请你返回 $n$ 天后监狱的状况（即，按上文描述进行 $n$ 次变更）。

**说明**：

- $cells.length == 8$。
- $cells[i]$ 为 0 或 1。
- $1 \le n \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：cells = [0,1,0,1,1,0,0,1], n = 7
输出：[0,0,1,1,0,0,0,0]
解释：下表总结了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

- 示例 2：

```python
输入：cells = [1,0,0,1,0,0,1,0], n = 1000000000
输出：[0,0,1,1,1,1,1,0]
```

## 解题思路

### 思路 1：哈希表 + 找规律

由于牢房只有 $8$ 间，状态数量有限（最多 $2^8 = 256$ 种），必然会出现循环。我们可以利用这个特性来优化。

1. **模拟变化**：按照规则模拟牢房状态的变化。
2. **检测循环**：使用哈希表记录每个状态第一次出现的天数，当出现重复状态时，说明进入循环。
3. **计算结果**：
   - 如果 $n$ 天内没有循环，直接返回第 $n$ 天的状态
   - 如果出现循环，计算循环周期，通过取模快速得到第 $n$ 天的状态
4. **边界处理**：注意第一个和最后一个牢房始终为空。

### 思路 1：代码

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells):
            """计算下一天的状态"""
            new_cells = [0] * 8
            for i in range(1, 7):
                # 两个相邻房间状态相同，则被占用
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            return new_cells
        
        seen = {}
        day = 0
        
        while day < n:
            # 将状态转换为元组（可哈希）
            state = tuple(cells)
            
            # 检测循环
            if state in seen:
                # 计算循环周期
                cycle_length = day - seen[state]
                # 跳过完整的循环
                remaining_days = (n - day) % cycle_length
                # 继续模拟剩余天数
                for _ in range(remaining_days):
                    cells = next_day(cells)
                return cells
            
            # 记录当前状态
            seen[state] = day
            # 模拟下一天
            cells = next_day(cells)
            day += 1
        
        return cells
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\min(n, 2^k))$，其中 $k = 8$ 是牢房数量。最多模拟 $2^8 = 256$ 天就会出现循环。
- **空间复杂度**：$O(2^k)$，哈希表最多存储 $256$ 个状态。
