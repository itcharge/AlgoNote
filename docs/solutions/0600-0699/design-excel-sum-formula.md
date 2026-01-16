# [0631. 设计 Excel 求和公式](https://leetcode.cn/problems/design-excel-sum-formula/)

- 标签：图、设计、拓扑排序、数组、哈希表、字符串、矩阵
- 难度：困难

## 题目链接

- [0631. 设计 Excel 求和公式 - 力扣](https://leetcode.cn/problems/design-excel-sum-formula/)

## 题目大意

**描述**：

请你设计 Excel 中的基本功能，并实现求和公式。

**要求**：

实现 Excel 类：

- `Excel(int height, char width)`：用高度 $height$ 和宽度 $width$ 初始化对象。该表格是一个大小为 $height \times width$ 的整数矩阵 $mat$，其中行下标范围是 $[1, height]$，列下标范围是 $['A', width]$。初始情况下，所有的值都应该为零。
- `void set(int row, char column, int val)`：将 $mat[row][column]$ 的值更改为 $val$。
- `int get(int row, char column)`：返回 $mat[row][column]$ 的值。
- `int sum(int row, char column, List<String> numbers)`：将 $mat[row][column]$ 的值设为由 $numbers$ 表示的单元格的和，并返回 $mat[row][column]$ 的值。此求和公式应该 **长期作用于** 该单元格，直到该单元格被另一个值或另一个求和公式覆盖。其中，$numbers[i]$ 的格式可以为：
  - `"ColRow"`：表示某个单元格。例如，`"F7"` 表示单元格 $mat[7]['F']$。
  - `"ColRow1:ColRow2"`：表示一组单元格。该范围将始终为一个矩形，其中 `"ColRow1"` 表示左上角单元格的位置，`"ColRow2"` 表示右下角单元格的位置。例如，`"B3:F7"` 表示 $3 \le i \le 7$ 和 $'B' \le j \le 'F'$ 的单元格 $mat[i][j]$。

**说明**：

- 注意：可以假设不会出现循环求和引用。例如，$mat[1]['A'] == sum(1, "B")$，且 $mat[1]['B'] == sum(1, "A")$。
- $1 \le height \le 26$。
- $'A' \le width \le 'Z'$。
- $1 \le row \le height$。
- $'A' \le column \le width$。
- $-10^3 \le val \le 10^3$。
- $1 \le numbers.length \le 5$。
- $numbers[i]$ 的格式为 `"ColRow"` 或 `"ColRow1:ColRow2"`。
- 最多会对 `set`、`get` 和 `sum` 进行 $10^3$ 次调用。

**示例**：

- 示例 1：

```python
输入：
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
输出：
[null, null, 4, null, 6]

解释：
执行以下操作：
Excel excel = new Excel(3, "C");
 // 构造一个 3 * 3 的二维数组，所有值初始化为零。
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // 将 mat[1]["A"] 设置为 2 。
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // 返回 4
 // 将 mat[3]["C"] 设置为 mat[1]["A"] 的值与矩形范围的单元格和的和，该范围的左上角单元格位置为 mat[1]["A"]，右下角单元格位置为 mat[2]["B"]。
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // 将 mat[2]["B"] 设置为 2 。注意 mat[3]["C"] 也应该更改。
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // 返回 6
```

## 解题思路

### 思路 1：哈希表 + 图

这道题目要求设计一个 Excel 表格，支持设置单元格值、获取单元格值和设置求和公式。关键在于求和公式需要 **长期作用**，即当依赖的单元格值改变时，公式单元格的值也要自动更新。

**核心思路**：

- 使用哈希表存储每个单元格的值。
- 使用图结构记录单元格之间的依赖关系：如果单元格 $A$ 的值依赖于单元格 $B$，则 $B \to A$ 有一条边。
- 当某个单元格的值改变时，需要递归更新所有依赖它的单元格。

**算法步骤**：

1. **初始化**：创建哈希表存储单元格值，创建图存储依赖关系。
2. **set 操作**：设置单元格值，清除该单元格的依赖关系，递归更新依赖它的单元格。
3. **get 操作**：直接返回单元格的值。
4. **sum 操作**：解析 $numbers$，计算和，设置单元格值，建立依赖关系。

### 思路 1：代码

```python
class Excel:

    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1
        # formulas[r][c] = (cells_dict, val)
        # cells_dict: 依赖的单元格及其计数，val: 当前值
        self.formulas = [[None] * self.width for _ in range(height)]

    def get(self, row: int, column: str) -> int:
        r, c = row - 1, ord(column) - ord('A')
        if self.formulas[r][c] is None:
            return 0
        return self.formulas[r][c][1]

    def set(self, row: int, column: str, val: int) -> None:
        r, c = row - 1, ord(column) - ord('A')
        # 设置为纯值，清空依赖
        self.formulas[r][c] = ({}, val)
        # 拓扑排序更新依赖此单元格的所有单元格
        stack = []
        self._topological_sort(r, c, stack, set())
        self._execute_stack(stack)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r, c = row - 1, ord(column) - ord('A')
        cells = self._convert(numbers)
        summ = self._calculate_sum(r, c, cells)
        self.formulas[r][c] = (cells, summ)
        # 拓扑排序更新依赖此单元格的所有单元格
        stack = []
        self._topological_sort(r, c, stack, set())
        self._execute_stack(stack)
        return summ

    def _convert(self, strs: List[str]) -> dict:
        """将公式字符串转换为单元格计数字典"""
        res = {}
        for st in strs:
            if ':' not in st:
                res[st] = res.get(st, 0) + 1
            else:
                parts = st.split(':')
                si, ei = int(parts[0][1:]), int(parts[1][1:])
                sj, ej = parts[0][0], parts[1][0]
                for i in range(si, ei + 1):
                    for j in range(ord(sj), ord(ej) + 1):
                        key = chr(j) + str(i)
                        res[key] = res.get(key, 0) + 1
        return res

    def _topological_sort(self, r: int, c: int, stack: list, visited: set) -> None:
        """拓扑排序：找出所有依赖 (r,c) 的单元格"""
        key = chr(ord('A') + c) + str(r + 1)
        for i in range(len(self.formulas)):
            for j in range(len(self.formulas[0])):
                if self.formulas[i][j] is not None and key in self.formulas[i][j][0]:
                    if (i, j) not in visited:
                        self._topological_sort(i, j, stack, visited)
        if (r, c) not in visited:
            visited.add((r, c))
            stack.append((r, c))

    def _execute_stack(self, stack: list) -> None:
        """按拓扑顺序更新单元格"""
        while stack:
            r, c = stack.pop()
            if self.formulas[r][c] is not None and self.formulas[r][c][0]:
                self._calculate_sum(r, c, self.formulas[r][c][0])

    def _calculate_sum(self, r: int, c: int, cells: dict) -> int:
        """计算单元格的和"""
        total = 0
        for s, cnt in cells.items():
            x, y = int(s[1:]) - 1, ord(s[0]) - ord('A')
            val = self.formulas[x][y][1] if self.formulas[x][y] else 0
            total += val * cnt
        self.formulas[r][c] = (cells, total)
        return total


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - $set$ 操作：$O(d)$，其中 $d$ 是依赖此单元格的单元格数量，需要更新所有依赖的单元格。
  - $get$ 操作：$O(1)$，直接返回缓存的值。
  - $sum$ 操作：$O(k + d)$，其中 $k$ 是公式中依赖的单元格数量，$d$ 是依赖此单元格的单元格数量。需要计算所有依赖的单元格，并更新依赖此单元格的其他单元格。
- **空间复杂度**：$O(n + m)$，其中 $n$ 是单元格的数量，$m$ 是依赖关系的数量。
