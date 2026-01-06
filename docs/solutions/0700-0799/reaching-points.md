# [0780. 到达终点](https://leetcode.cn/problems/reaching-points/)

- 标签：数学
- 难度：困难

## 题目链接

- [0780. 到达终点 - 力扣](https://leetcode.cn/problems/reaching-points/)

## 题目大意

**描述**：

给定四个整数 $sx$，$sy$，$tx$ 和 $ty$。

**要求**：

如果通过一系列的转换可以从起点 $(sx, sy)$ 到达终点 $(tx, ty)$，则返回 true，否则返回 false。

从点 $(x, y)$ 可以转换到 $(x, x+y)$  或者 $(x+y, y)$。

**说明**：

- $1 \le sx, sy, tx, ty \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

- 示例 2：

```python
输入: sx = 1, sy = 1, tx = 2, ty = 2 
输出: false
```

## 解题思路

### 思路 1：数学

从起点 $(sx, sy)$ 到终点 $(tx, ty)$，每次可以将 $(x, y)$ 转换为 $(x, x+y)$ 或 $(x+y, y)$。我们可以反向思考：从 $(tx, ty)$ 逆推到 $(sx, sy)$。

**逆向操作**：
- 如果 $tx > ty$，则上一步是 $(tx - ty, ty)$。
- 如果 $ty > tx$，则上一步是 $(tx, ty - tx)$。

**优化**：
- 当 $tx \gg ty$ 时，可以一次性减去多个 $ty$：$tx = tx \% ty$（如果 $ty > sy$）。
- 否则，需要逐步减去，确保不会跳过 $(sx, sy)$。

### 思路 1：代码

```python
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 从终点逆推到起点
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                # 上一步是 (tx - ty, ty)
                if ty == sy:
                    # 检查是否能通过减去若干个 ty 到达 sx
                    return (tx - sx) % ty == 0
                # 一次性减去多个 ty
                tx %= ty
            else:
                # 上一步是 (tx, ty - tx)
                if tx == sx:
                    # 检查是否能通过减去若干个 tx 到达 sy
                    return (ty - sy) % tx == 0
                # 一次性减去多个 tx
                ty %= tx
        
        return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log(\max(tx, ty)))$，类似辗转相除法。
- **空间复杂度**：$O(1)$。
