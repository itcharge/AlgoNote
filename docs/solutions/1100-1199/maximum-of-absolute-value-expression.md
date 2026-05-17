# [1131. 绝对值表达式的最大值](https://leetcode.cn/problems/maximum-of-absolute-value-expression/)

- 标签：数组、数学
- 难度：中等

## 题目链接

- [1131. 绝对值表达式的最大值 - 力扣](https://leetcode.cn/problems/maximum-of-absolute-value-expression/)

## 题目大意

**描述**：给定两个长度相等的整数数组 $arr1$ 和 $arr2$。

**要求**：计算下面这个表达式的最大值：

$|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|$

其中 $i$ 和 $j$ 是数组中的任意两个下标。

**说明**：

- $2 \le arr1.length == arr2.length \le 40000$。
- $-10^6 \le arr1[i], arr2[i] \le 10^6$。

**示例**：

```python
输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
输出：13
```

## 解题思路

### 思路 1：转化为曼哈顿距离

这道题难在绝对值太多。去掉绝对值的技巧是：**每个绝对值 $|x|$ 要么等于 $x$，要么等于 $-x$。** 所以对于三个绝对值，一共有 $2^3 = 8$ 种符号组合。

展开后得到 8 种不含绝对值的表达式。但分析发现，其中 4 种和另外 4 种只是交换了 $i$ 和 $j$ 的位置，本质上是等价的。

所以只需要考虑 4 种组合：

1. $arr1[i] + arr2[i] + i$
2. $arr1[i] + arr2[i] - i$
3. $arr1[i] - arr2[i] + i$
4. $arr1[i] - arr2[i] - i$

对于每种组合，遍历所有位置，算出最大值和最小值，它们的差就是在这种组合下表达式的可能取值。取 4 种组合中最大的那个差。

**为什么要算最大值减最小值？**
因为 $|a_i - a_j|$ 的最大值 = $\max(a_i - a_j) = \max(a_i) - \min(a_j)$，也就是最大值减最小值。

**步骤拆解：**

1. 准备 4 组系数 $(d1, d2, d3)$，分别对应 $arr1$、$arr2$、$i$ 的符号。
2. 对每组系数，遍历数组算出每个位置的值 $d1 \times arr1[i] + d2 \times arr2[i] + d3 \times i$。
3. 记录最大值和最小值，差值就是该组合下的最大可能值。
4. 取 4 组结果中的最大值。

### 思路 1：代码

```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        
        # 4 种符号组合
        directions = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
        
        ans = 0
        
        for d1, d2, d3 in directions:
            max_val = float('-inf')
            min_val = float('inf')
            
            for i in range(n):
                val = d1 * arr1[i] + d2 * arr2[i] + d3 * i
                max_val = max(max_val, val)
                min_val = min(min_val, val)
            
            ans = max(ans, max_val - min_val)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。遍历 4 次数组，每次 $O(n)$。
- **空间复杂度**：$O(1)$。只用了几个变量。
