# [1299. 将每个元素替换为右侧最大元素](https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/)

- 标签：数组
- 难度：简单

## 题目链接

- [1299. 将每个元素替换为右侧最大元素 - 力扣](https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/)

## 题目大意

**描述**：给定一个数组 $arr$。

**要求**：将每个元素替换为其右侧所有元素中的最大值。最后一个元素替换为 $-1$。返回替换后的数组。

**说明**：

- $1 \le arr.length \le 10^{4}$。
- $1 \le arr[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
解释：
- 下标 0 → 右侧最大值 max([18,5,4,6,1]) = 18
- 下标 1 → 右侧最大值 max([5,4,6,1]) = 6
- 下标 2 → 右侧最大值 max([4,6,1]) = 6
- 下标 3 → 右侧最大值 max([6,1]) = 6
- 下标 4 → 右侧最大值 max([1]) = 1
- 下标 5 → -1
```

## 解题思路

### 思路 1：反向遍历

#### 1. 核心思想

正向遍历时，每次都需要扫描右侧所有元素找最大值，时间复杂度 $O(n^2)$。

如果**从右向左**遍历，可以一边遍历一边维护当前右侧的最大值，只需要 $O(n)$ 时间。

#### 2. 具体步骤

**第 1 步**：初始化结果数组 $ans = [-1] \times n$，当前最大值 $max\_right = -1$。

**第 2 步**：从右向左遍历 $i = n-1$ 到 $0$：
- $ans[i] = max\_right$。
- 更新 $max\_right = \max(max\_right, arr[i])$。

**第 3 步**：返回 $ans$。

#### 3. 结合示例走一遍

$arr = [17,18,5,4,6,1]$

反向遍历：
- $i=5$：$ans[5] = -1$，$max\_right = \max(-1, 1) = 1$
- $i=4$：$ans[4] = 1$，$max\_right = \max(1, 6) = 6$
- $i=3$：$ans[3] = 6$，$max\_right = \max(6, 4) = 6$
- $i=2$：$ans[2] = 6$，$max\_right = \max(6, 5) = 6$
- $i=1$：$ans[1] = 6$，$max\_right = \max(6, 18) = 18$
- $i=0$：$ans[0] = 18$，$max\_right = \max(18, 17) = 18$

结果 $[18,6,6,6,1,-1]$。

### 思路 1：代码

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        max_right = -1
        for i in range(n - 1, -1, -1):
            ans[i] = max_right
            max_right = max(max_right, arr[i])
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。一次反向遍历。
- **空间复杂度**：$O(1)$，不考虑结果数组。
