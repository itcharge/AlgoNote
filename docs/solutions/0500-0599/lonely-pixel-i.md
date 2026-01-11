# [0531. 孤独像素 I](https://leetcode.cn/problems/lonely-pixel-i/)

- 标签：数组、哈希表、矩阵
- 难度：中等

## 题目链接

- [0531. 孤独像素 I - 力扣](https://leetcode.cn/problems/lonely-pixel-i/)

## 题目大意

**描述**：

给定一个由 `'B'` 和 `'W'` 组成的二维矩阵 $picture$，其中 `'B'` 表示黑色像素，`'W'` 表示白色像素。

如果一个黑色像素 `'B'` 满足以下条件，则称其为孤独像素：

- 它所在的行和列中，只有这一个黑色像素

**要求**：

返回图片中孤独像素的数量。

**说明**：

- $m == picture.length$。
- $n == picture[i].length$。
- $1 \le m, n \le 500$。
- $picture[i][j]$ 为 `'W'` 或 `'B'`。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/11/11/pixel1.jpg)

```python
输入：picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
输出：3
解释：全部三个 'B' 都是黑色的孤独像素
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2020/11/11/pixel2.jpg)

```python
输入：picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
输出：0
```

## 解题思路

### 思路 1：统计行列黑色像素数量

先统计每一行和每一列中黑色像素的数量，然后遍历矩阵，对于每个黑色像素，检查其所在行和列的黑色像素数量是否都为 $1$。

**解题步骤**：

1. 统计每一行的黑色像素数量 $row\_count[i]$。
2. 统计每一列的黑色像素数量 $col\_count[j]$。
3. 遍历矩阵，对于 `picture[i][j] == 'B'`，如果 $row\_count[i] == 1$ 且 $col\_count[j] == 1$，则计数加 $1$。

### 思路 1：代码

```python
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture or not picture[0]:
            return 0
        
        m, n = len(picture), len(picture[0])
        
        # 统计每行和每列的黑色像素数量
        row_count = [0] * m
        col_count = [0] * n
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        
        # 统计孤独像素
        lonely_count = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    lonely_count += 1
        
        return lonely_count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times n)$，其中 $m$ 和 $n$ 分别是矩阵的行数和列数。需要遍历矩阵两次。
- **空间复杂度**：$O(m + n)$，需要存储每行和每列的黑色像素数量。
