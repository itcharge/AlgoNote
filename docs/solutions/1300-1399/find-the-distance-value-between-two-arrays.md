# [1385. 两个数组间的距离值](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/)

- 标签：数组、双指针、二分查找、排序
- 难度：简单

## 题目链接

- [1385. 两个数组间的距离值 - 力扣](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/)

## 题目大意

**描述**：给定两个整数数组 $arr1$ 和 $arr2$，以及一个整数 $d$。

**要求**：返回满足以下条件的 $arr1[i]$ 的个数：对于所有 $arr2[j]$，都有 $|arr1[i] - arr2[j]| > d$。

**示例**：

- 示例 1：

```python
输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
输出：2
解释：
对于 arr1[0]=4 我们有：
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
所以 arr1[0]=4 符合距离要求

对于 arr1[1]=5 我们有：
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
所以 arr1[1]=5 也符合距离要求

对于 arr1[2]=8 我们有：
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
存在距离小于等于 2 的情况，不符合距离要求 

故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
```

- 示例 2：

```python
输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
输出：2
```


## 解题思路

### 思路 1：排序 + 二分

#### 1. 核心思想

将 $arr2$ 排序，对每个 $arr1[i]$，在 $arr2$ 中二分查找最接近的元素。如果与最近元素的差值 $> d$，则满足条件。

#### 2. 具体步骤

**第 1 步**：对 $arr2$ 排序。

**第 2 步**：遍历 $arr1$，对每个 $x$，在 $arr2$ 中二分查找第一个 $\ge x$ 的元素和最后一个 $< x$ 的元素，计算最小差值。

**第 3 步**：如果最小差值 $> d$，计数加 $1$。

### 思路 1：代码

```python
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            min_diff = float('inf')
            if idx < len(arr2):
                min_diff = min(min_diff, abs(x - arr2[idx]))
            if idx > 0:
                min_diff = min(min_diff, abs(x - arr2[idx - 1]))
            if min_diff > d:
                ans += 1
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log m)$，$n = len(arr1)$，$m = len(arr2)$。
- **空间复杂度**：$O(1)$。
