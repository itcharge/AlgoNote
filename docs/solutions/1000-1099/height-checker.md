# [1051. 高度检查器](https://leetcode.cn/problems/height-checker/)

- 标签：数组、计数排序、排序
- 难度：简单

## 题目链接

- [1051. 高度检查器 - 力扣](https://leetcode.cn/problems/height-checker/)

## 题目大意

**描述**：学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。

排序后的高度情况用整数数组 $expected$ 表示，其中 $expected[i]$ 是预计排在这一行中第 $i$ 位的学生的高度（下标从 $0$ 开始）。

给定一个整数数组 $heights$ ，表示当前学生站位的高度情况。$heights[i]$ 是这一行中第 $i$ 位学生的高度（下标从 $0$ 开始）。

**要求**：返回满足 $heights[i] \ne expected[i]$ 的下标数量 。

**说明**：

- $1 \le heights.length \le 100$。
- $1 \le heights[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：heights = [1,1,4,2,1,3]
输出：3 
解释：
高度：[1,1,4,2,1,3]
预期：[1,1,1,2,3,4]
下标 2 、4 、5 处的学生高度不匹配。
```

- 示例 2：

```python
输入：heights = [5,1,2,3,4]
输出：5
解释：
高度：[5,1,2,3,4]
预期：[1,2,3,4,5]
所有下标的对应学生高度都不匹配。
```

## 解题思路

### 思路 1：排序算法

1. 将数组 $heights$ 复制一份，记为 $expected$。
2. 对数组 $expected$ 进行排序。
3. 排序之后，对比并统计 $heights[i] \ne expected[i]$ 的下标数量，记为 $ans$。
4. 返回 $ans$。

### 思路 1：代码

```Python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        ans = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为数组 $heights$ 的长度。
- **空间复杂度**：$O(n)$。

### 思路 2：计数排序

题目中 $heights[i]$ 的数据范围为 $[1, 100]$，所以我们可以使用计数排序。

### 思路 2：代码

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 待排序数组中最大值元素 heights_max = 100 和最小值元素 heights_min = 1
        heights_min, heights_max = 1, 100
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = heights_max - heights_min + 1
        counts = [0 for _ in range(size)]
		
        # 统计值为 height 的元素出现的次数
        for height in heights:
            counts[height - heights_min] += 1

        ans = 0
        idx = 0
        # 从小到大遍历 counts 的元素值范围
        for height in range(heights_min, heights_max + 1):
            while counts[height - heights_min]:
                # 对于每个元素值，判断是否与对应位置上的 heights[idx] 相等
                if heights[idx] != height:
                    ans += 1
                idx += 1
                counts[height - heights_min] -= 1
        
        return ans
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n + k)$，其中 $n$ 为数组 $heights$ 的长度，$k$ 为数组 $heights$ 的值域范围。
- **空间复杂度**：$O(k)$。

