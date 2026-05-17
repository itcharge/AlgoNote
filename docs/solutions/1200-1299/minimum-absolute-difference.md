# [1200. 最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [1200. 最小绝对差 - 力扣](https://leetcode.cn/problems/minimum-absolute-difference/)

## 题目大意

**描述**：给定一个整数数组 $arr$，其中每个元素都互不相同。

**要求**：找出所有具有最小绝对差的元素对，并且按升序返回它们。

**说明**：

- $2 \le arr.length \le 10^{5}$。
- $-10^{6} \le arr[i] \le 10^{6}$。
- $arr$ 中的所有元素互不相同。

**示例**：

- 示例 1：

```python
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
解释：最小绝对差为 1，所有差为 1 的元素对为 [1,2],[2,3],[3,4]。
```

- 示例 2：

```python
输入：arr = [1,3,6,10,15]
输出：[[1,3]]
解释：最小绝对差为 2，只有一对 [1,3]。
```

- 示例 3：

```python
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]
```

## 解题思路

### 思路 1：排序 + 一次遍历

#### 1. 核心思想

对于任意无序数组，最小绝对差一定出现在**排序后相邻的两个元素之间**。因为如果存在一个最小绝对差由非相邻元素产生，那么这两个元素中间的元素与其中一个的差必然更小（或相等），这与"最小"矛盾。

所以只需要：
1. 将数组排序。
2. 遍历排序后的数组，计算每对相邻元素的差值。
3. 记录最小差值，并收集差值等于最小差值的所有元素对。

#### 2. 具体步骤

**第 1 步**：对 $arr$ 进行升序排序。

**第 2 步**：初始化 $min\_diff = \infty$ 和结果列表 $ans = []$。

**第 3 步**：遍历 $i$ 从 $1$ 到 $n-1$：
- 计算 $diff = arr[i] - arr[i-1]$。
- 如果 $diff < min\_diff$：更新 $min\_diff = diff$，清空 $ans$，加入 $[arr[i-1], arr[i]]$。
- 如果 $diff == min\_diff$：将 $[arr[i-1], arr[i]]$ 加入 $ans$。
- 如果 $diff > min\_diff$：跳过。

**第 4 步**：返回 $ans$。

#### 3. 结合示例走一遍

$arr = [4,2,1,3]$

排序后：$arr = [1,2,3,4]$

遍历：
- $i=1$：$diff=2-1=1$，$min\_diff=1$，$ans=[[1,2]]$
- $i=2$：$diff=3-2=1 == min\_diff$，$ans=[[1,2],[2,3]]$
- $i=3$：$diff=4-3=1 == min\_diff$，$ans=[[1,2],[2,3],[3,4]]$

返回 $[[1,2],[2,3],[3,4]]$。

### 思路 1：代码

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组 $arr$ 的长度。排序需要 $O(n \log n)$ 时间，一次遍历需要 $O(n)$ 时间。
- **空间复杂度**：$O(\log n)$，排序使用的栈空间，不考虑存储结果所需的空间。
