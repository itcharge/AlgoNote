# [1710. 卡车上的最大单元数](https://leetcode.cn/problems/maximum-units-on-a-truck/)

- 标签：贪心、数组、排序
- 难度：简单

## 题目链接

- [1710. 卡车上的最大单元数 - 力扣](https://leetcode.cn/problems/maximum-units-on-a-truck/)

## 题目大意

**描述**：现在需要将一些箱子装在一辆卡车上。给定一个二维数组 $boxTypes$，其中 $boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]$。

$numberOfBoxesi$ 是类型 $i$ 的箱子的数量。$numberOfUnitsPerBoxi$ 是类型 $i$ 的每个箱子可以装载的单元数量。

再给定一个整数 $truckSize$ 表示一辆卡车上可以装载箱子的最大数量。只要箱子数量不超过 $truckSize$，你就可以选择任意箱子装到卡车上。

**要求**：返回卡车可以装载的最大单元数量。

**说明**：

- $1 \le boxTypes.length \le 1000$。
- $1 \le numberOfBoxesi, numberOfUnitsPerBoxi \le 1000$。
- $1 \le truckSize \le 106$。

**示例**：

- 示例 1：

```python
输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
输出：8
解释
箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
```

- 示例 2：

```python
输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
输出：91
```

## 解题思路

### 思路 1：贪心算法

题目中，一辆卡车上可以装载箱子的最大数量是固定的（$truckSize$），那么如果想要使卡车上装载的单元数量最大，就应该优先选取装载单元数量多的箱子。

所以，从贪心算法的角度来考虑，我们应该按照每个箱子可以装载的单元数量对数组 $boxTypes$ 从大到小排序。然后优先选取装载单元数量多的箱子。 

下面我们使用贪心算法三步走的方法解决这道题。

1. **转换问题**：将原问题转变为，在 $truckSize$ 的限制下，当选取完装载单元数量最多的箱子 $box$ 之后，再解决剩下箱子（$truckSize - box[0]$）的选择问题（子问题）。
2. **贪心选择性质**：对于当前 $truckSize$，优先选取装载单元数量最多的箱子。
3. **最优子结构性质**：在上面的贪心策略下，当前 $truckSize$ 的贪心选择 + 剩下箱子的子问题最优解，就是全局最优解。也就是说在贪心选择的方案下，能够使得卡车可以装载的单元数量达到最大。

使用贪心算法的解决步骤描述如下：

1. 对数组 $boxTypes$ 按照每个箱子可以装载的单元数量从大到小排序。使用变量 $res$ 记录卡车可以装载的最大单元数量。
2. 遍历数组 $boxTypes$，对于当前种类的箱子 $box$：
   1. 如果 $truckSize > box[0]$，说明当前种类箱子可以全部装载。则答案数量加上该种箱子的单元总数，即 $box[0] \times box[1]$，并且最大数量 $truckSize$ 减去装载的箱子数。
   2. 如果 $truckSize \le box[0]$，说明当前种类箱子只能部分装载。则答案数量加上 $truckSize \times box[1]$，并跳出循环。
3. 最后返回答案 $res$。

### 思路 1：代码

```python
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        res = 0
        for box in boxTypes:
            if truckSize > box[0]:
                res += box[0] * box[1]
                truckSize -= box[0]
            else:
                res += truckSize * box[1]
                break
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 是数组 $boxTypes$ 的长度。
- **空间复杂度**：$O(\log n)$。
