# [1182. 与目标颜色间的最短距离](https://leetcode.cn/problems/shortest-distance-to-target-color/)

- 标签：数组、二分查找、动态规划
- 难度：中等

## 题目链接

- [1182. 与目标颜色间的最短距离 - 力扣](https://leetcode.cn/problems/shortest-distance-to-target-color/)

## 题目大意

**描述**：给定一个数组 $colors$，里面只有 $1$、$2$、$3$ 三种颜色值。再给定一个查询数组 $queries$，每个查询 $[i, c]$ 表示：从下标 $i$ 出发，找到最近的值为 $c$ 的元素。

**要求**：返回每个查询的结果（最短距离）。如果不存在目标颜色，返回 $-1$。

**说明**：

- $1 \le colors.length \le 5 \times 10^4$。
- $1 \le colors[i] \le 3$。
- $1 \le queries.length \le 5 \times 10^4$。
- $queries[i].length == 2$。
- $0 \le queries[i][0] < colors.length$。
- $1 \le queries[i][1] \le 3$。

**示例**：

- 示例 1：

```python
输入：colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
输出：[3,0,3]
解释： 
距离索引 1 最近的颜色 3 位于索引 4（距离为 3）。
距离索引 2 最近的颜色 2 就是它自己（距离为 0）。
距离索引 6 最近的颜色 1 位于索引 3（距离为 3）。
```

- 示例 2：

```python
输入：colors = [1,2], queries = [[0,3]]
输出：[-1]
解释：colors 中没有颜色 3。
```

## 解题思路

### 思路 1：预处理 + 左右扫描

**为什么扫两遍？** 某个位置最近的同色元素可能在它左边，也可能在它右边。一次从左到右只能知道左边的信息，所以需要再从右到左扫一遍补充右边的信息。

**拆解步骤**：

1. **创建两个二维数组** $left$ 和 $right$：
   - $left[i][c]$：位置 $i$ 左边（含 $i$）最近的颜色 $c$ 的下标，没有则为 $-1$
   - $right[i][c]$：位置 $i$ 右边（含 $i$）最近的颜色 $c$ 的下标，没有则为 $-1$

2. **从左到右遍历**：对于每个位置 $i$，先继承前一个位置的信息，再更新当前位置颜色的信息。

3. **从右到左遍历**：同理，先继承后一个位置的信息，再更新当前位置颜色的信息。

4. **处理每个查询 $[i, c]$**：
   - 看 $left[i][c]$ 和 $right[i][c]$ 哪个离 $i$ 更近
   - 如果左右都没有，返回 $-1$

### 思路 1：代码

```python
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        # left[i][c] 表示位置 i 左边最近的颜色 c 的位置
        left = [[-1] * 4 for _ in range(n)]
        # right[i][c] 表示位置 i 右边最近的颜色 c 的位置
        right = [[-1] * 4 for _ in range(n)]

        # 从左到右扫一遍，记录每个位置左边最近的每种颜色
        for i in range(n):
            if i > 0:
                # 继承前一个位置的信息
                for c in range(1, 4):
                    left[i][c] = left[i - 1][c]
            # 更新当前位置颜色的位置
            left[i][colors[i]] = i

        # 从右到左扫一遍，记录每个位置右边最近的每种颜色
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                # 继承后一个位置的信息
                for c in range(1, 4):
                    right[i][c] = right[i + 1][c]
            # 更新当前位置颜色的位置
            right[i][colors[i]] = i

        # 处理每个查询
        result = []
        for i, c in queries:
            left_pos = left[i][c]
            right_pos = right[i][c]

            if left_pos == -1 and right_pos == -1:
                result.append(-1)           # 没有这个颜色
            elif right_pos == -1:
                result.append(i - left_pos) # 只有左边有
            elif left_pos == -1:
                result.append(right_pos - i) # 只有右边有
            else:
                # 左右都有，取距离更小的那个
                result.append(min(i - left_pos, right_pos - i))

        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + q)$。用人话说就是：预处理需要从左到右再从右到左各扫一遍，共 $O(n)$；每个查询只需要常数时间就能回答，总共 $O(q)$。
- **空间复杂度**：$O(n)$。需要存储 $left$ 和 $right$ 两个大小为 $n \times 4$ 的数组。
