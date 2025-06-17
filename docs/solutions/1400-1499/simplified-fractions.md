# [1447. 最简分数](https://leetcode.cn/problems/simplified-fractions/)

- 标签：数学、字符串、数论
- 难度：中等

## 题目链接

- [1447. 最简分数 - 力扣](https://leetcode.cn/problems/simplified-fractions/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回所有 $0$ 到 $1$ 之间（不包括 $0$ 和 $1$）满足分母小于等于 $n$ 的最简分数。分数可以以任意顺序返回。

**说明**：

- $1 \le n \le 100$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
```

- 示例 2：

```python
输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2"。
```

## 解题思路

### 思路 1：数学

如果分子和分母的最大公约数为 $1$ 时，则当前分数为最简分数。

而 $n$ 的数据范围为 $(1, 100)$。因此我们可以使用两重遍历，分别枚举分子和分母，然后通过判断分子和分母是否为最大公约数，来确定当前分数是否为最简分数。

### 思路 1：代码

```python
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1:
                    res.append(str(i) + "/" + str(j))

        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times \log n)$。
- **空间复杂度**：$O(1)$。

