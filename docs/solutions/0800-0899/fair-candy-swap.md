# [0888. 公平的糖果交换](https://leetcode.cn/problems/fair-candy-swap/)

- 标签：数组、哈希表、二分查找、排序
- 难度：简单

## 题目链接

- [0888. 公平的糖果交换 - 力扣](https://leetcode.cn/problems/fair-candy-swap/)

## 题目大意

**描述**：

爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 $aliceSizes$ 和 $bobSizes$，$aliceSizes[i]$ 是爱丽丝拥有的第 $i$ 盒糖果中的糖果数量，$bobSizes[j]$ 是鲍勃拥有的第 $j$ 盒糖果中的糖果数量。

两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。

**要求**：

返回一个整数数组 $answer$，其中 $answer[0]$ 是爱丽丝必须交换的糖果盒中的糖果的数目，$answer[1]$ 是鲍勃必须交换的糖果盒中的糖果的数目。

如果存在多个答案，你可以返回其中「任何一个」。题目测试用例保证存在与输入对应的答案。


**说明**：

- $1 \le aliceSizes.length, bobSizes.length \le 10^{4}$。
- $1 \le aliceSizes[i], bobSizes[j] \le 10^{5}$。
- 爱丽丝和鲍勃的糖果总数量不同。
- 题目数据保证对于给定的输入至少存在一个有效答案。

**示例**：

- 示例 1：

```python
输入：aliceSizes = [1,1], bobSizes = [2,2]
输出：[1,2]
```

- 示例 2：

```python
输入：aliceSizes = [1,2], bobSizes = [2,3]
输出：[1,2]
```

## 解题思路

### 思路 1：哈希表 + 数学

这道题要求找到一对糖果盒，使得交换后两人的糖果总数相等。

设爱丽丝的糖果总数为 $sumA$，鲍勃的糖果总数为 $sumB$。交换后两人糖果总数相等，即：

$$sumA - x + y = sumB - y + x$$

其中 $x$ 是爱丽丝交换出去的糖果数，$y$ 是鲍勃交换出去的糖果数。

化简得：$y = x + \frac{sumB - sumA}{2}$

算法步骤：

1. 计算爱丽丝和鲍勃的糖果总数 $sumA$ 和 $sumB$。
2. 计算差值 $diff = \frac{sumB - sumA}{2}$。
3. 将鲍勃的糖果数存入哈希表，方便快速查找。
4. 遍历爱丽丝的糖果盒，对于每个 $x$，检查 $y = x + diff$ 是否在鲍勃的糖果盒中。
5. 如果找到，返回 $[x, y]$。

### 思路 1：代码

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # 计算爱丽丝和鲍勃的糖果总数
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        # 计算差值
        diff = (sumB - sumA) // 2
        
        # 将鲍勃的糖果数存入哈希表
        bobSet = set(bobSizes)
        
        # 遍历爱丽丝的糖果盒
        for x in aliceSizes:
            y = x + diff
            # 如果 y 在鲍勃的糖果盒中，返回结果
            if y in bobSet:
                return [x, y]
        
        return []
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 和 $m$ 分别是 $\text{aliceSizes}$ 和 $\text{bobSizes}$ 的长度。需要遍历两个数组。
- **空间复杂度**：$O(m)$，需要使用哈希表存储鲍勃的糖果数。
