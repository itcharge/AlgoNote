# [0970. 强整数](https://leetcode.cn/problems/powerful-integers/)

- 标签：哈希表、数学、枚举
- 难度：中等

## 题目链接

- [0970. 强整数 - 力扣](https://leetcode.cn/problems/powerful-integers/)

## 题目大意

**描述**：

给定三个整数 $x$、$y$ 和 $bound$。

**要求**：

返回值小于或等于 $bound$ 的所有「强整数」组成的列表。

**说明**：

- 如果某一整数可以表示为 $x^i + y^j$ ，其中整数 $i \le 0$ 且 $j \le 0$，那么我们认为该整数是一个「强整数」。
- 你可以按任何顺序返回答案。在你的回答中，每个值「最多」出现一次。
- $1 \le x, y \le 10^{3}$。
- $0 \le bound \le 10^{6}$。

**示例**：

- 示例 1：

```python
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释： 
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32
```

- 示例 2：

```python
输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]
```

## 解题思路

### 思路 1：枚举

根据题意，强整数可以表示为 $x^i + y^j$，其中 $i \ge 0$，$j \ge 0$。由于结果要小于等于 $bound$，我们可以枚举所有可能的 $i$ 和 $j$。

1. **确定枚举范围**：
   - 当 $x = 1$ 时，$x^i = 1$（对所有 $i$）
   - 当 $x > 1$ 时，$x^i$ 最多枚举到 $\log_x(bound)$
   - 同理，$y^j$ 也有类似的范围
2. **枚举所有组合**：使用两层循环枚举所有可能的 $i$ 和 $j$，计算 $x^i + y^j$。
3. **去重**：使用集合存储结果，自动去重。
4. **边界处理**：当 $x = 1$ 或 $y = 1$ 时，只需要枚举一次即可。

### 思路 1：代码

```python
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        
        # 确定 x 的幂次上限
        x_limit = 20 if x > 1 else 1  # x^20 > 10^6
        y_limit = 20 if y > 1 else 1  # y^20 > 10^6
        
        # 枚举所有可能的 i 和 j
        for i in range(x_limit):
            x_power = x ** i
            if x_power > bound:
                break
            
            for j in range(y_limit):
                y_power = y ** j
                total = x_power + y_power
                
                if total <= bound:
                    result.add(total)
                
                # 如果 y = 1，只需要枚举一次
                if y == 1:
                    break
            
            # 如果 x = 1，只需要枚举一次
            if x == 1:
                break
        
        return list(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log^2 \text{bound})$，最多枚举 $\log_x(\text{bound}) \times \log_y(\text{bound})$ 次。
- **空间复杂度**：$O(\log^2 \text{bound})$，集合中最多存储 $O(\log^2 \text{bound})$ 个元素。
