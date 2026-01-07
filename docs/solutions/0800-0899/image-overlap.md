# [0835. 图像重叠](https://leetcode.cn/problems/image-overlap/)

- 标签：数组、矩阵
- 难度：中等

## 题目链接

- [0835. 图像重叠 - 力扣](https://leetcode.cn/problems/image-overlap/)

## 题目大意

**描述**：

给定两个图像 $img1$ 和 $img2$，两个图像的大小都是 $n \times n$，用大小相同的二进制正方形矩阵表示。二进制矩阵仅由若干 0 和若干 1 组成。

「转换」其中一个图像，将所有的 1 向左，右，上，或下滑动任何数量的单位；然后把它放在另一个图像的上面。该转换的「重叠」是指两个图像「都」具有 1 的位置的数目。

请注意，转换「不包括」向任何方向旋转。越过矩阵边界的 1 都将被清除。

**要求**：

计算最大可能的重叠数量。

**说明**：

- $n == img1.length == img1[i].length$。
- $n == img2.length == img2[i].length$。
- $1 \le n \le 30$。
- $img1[i][j]$ 为 0 或 1。
- $img2[i][j]$ 为 0 或 1。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg)

```python
输入：img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
输出：3
解释：将 img1 向右移动 1 个单位，再向下移动 1 个单位。
```

![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg)

```python
两个图像都具有 1 的位置的数目是 3（用红色标识）。
```

![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg)


- 示例 2：

```python
输入：img1 = [[1]], img2 = [[1]]
输出：1
```

## 解题思路

### 思路 1：哈希表 + 偏移量统计

这道题要求计算两个二进制矩阵的最大重叠数。可以通过平移其中一个矩阵来实现重叠。

关键观察：

- 只有值为 $1$ 的位置才会对重叠产生贡献。
- 可以枚举 $img1$ 中所有值为 $1$ 的位置和 $img2$ 中所有值为 $1$ 的位置，计算它们之间的偏移量。
- 相同偏移量出现的次数就是该偏移下的重叠数。

算法步骤：

1. 提取 $img1$ 和 $img2$ 中所有值为 $1$ 的位置。
2. 对于 $img1$ 中的每个 $1$ 和 $img2$ 中的每个 $1$，计算偏移量 $(dx, dy)$。
3. 使用哈希表统计每个偏移量出现的次数。
4. 返回最大的出现次数。

### 思路 1：代码

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # 提取 img1 和 img2 中所有值为 1 的位置
        ones1 = []
        ones2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))
        
        # 统计每个偏移量出现的次数
        offset_count = {}
        for x1, y1 in ones1:
            for x2, y2 in ones2:
                # 计算偏移量
                dx = x1 - x2
                dy = y1 - y2
                offset = (dx, dy)
                offset_count[offset] = offset_count.get(offset, 0) + 1
        
        # 返回最大重叠数
        return max(offset_count.values()) if offset_count else 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^4)$，其中 $n$ 是矩阵的边长。最坏情况下，两个矩阵都全为 $1$，需要枚举 $O(n^2) \times O(n^2)$ 对位置。
- **空间复杂度**：$O(n^2)$，需要存储所有值为 $1$ 的位置和偏移量统计。
