# [1122. 数组的相对排序](https://leetcode.cn/problems/relative-sort-array/)

- 标签：数组、哈希表、计数排序、排序
- 难度：简单

## 题目链接

- [1122. 数组的相对排序 - 力扣](https://leetcode.cn/problems/relative-sort-array/)

## 题目大意

**描述**：给定两个数组，$arr1$ 和 $arr2$，其中 $arr2$ 中的元素各不相同，$arr2$ 中的每个元素都出现在 $arr1$ 中。

**要求**：对 $arr1$ 中的元素进行排序，使 $arr1$ 中项的相对顺序和 $arr2$ 中的相对顺序相同。未在 $arr2$ 中出现过的元素需要按照升序放在 $arr1$ 的末尾。

**说明**：

- $1 \le arr1.length, arr2.length \le 1000$。
- $0 \le arr1[i], arr2[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
```

- 示例 2：

```python
输入：arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
输出：[22,28,8,6,17,44]
```

## 解题思路

### 思路 1：计数排序

因为元素值范围在 $[0, 1000]$，所以可以使用计数排序的思路来解题。

1. 使用数组 $count$ 统计 $arr1$ 各个元素个数。
2. 遍历 $arr2$ 数组，将对应元素$num2$ 按照个数 $count[num2]$ 添加到答案数组 $ans$ 中，同时在 $count$ 数组中减去对应个数。
3. 然后在处理 $count$ 中剩余元素，将 $count$ 中大于 $0$ 的元素下标依次添加到答案数组 $ans$ 中。
4. 最后返回答案数组 $ans$。

### 思路 1：代码

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 计算待排序序列中最大值元素 arr_max 和最小值元素 arr_min
        arr1_min, arr1_max = min(arr1), max(arr1)
        # 定义计数数组 counts，大小为 最大值元素 - 最小值元素 + 1
        size = arr1_max - arr1_min + 1
        counts = [0 for _ in range(size)]

        # 统计值为 num 的元素出现的次数
        for num in arr1:
            counts[num - arr1_min] += 1

        res = []
        for num in arr2:
            while counts[num - arr1_min] > 0:
                res.append(num)
                counts[num - arr1_min] -= 1

        for i in range(size):
            while counts[i] > 0:
                num = i + arr1_min
                res.append(num)
                counts[i] -= 1
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n + max(arr_1))$。其中 $m$ 是数组 $arr_1$ 的长度，$n$ 是数组 $arr_2$ 的长度，$max(arr_1)$ 是数组 $arr_1$ 的最大值。
- **空间复杂度**：$O(max(arr_1))$。



