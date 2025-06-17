# [面试题 10.01. 合并排序的数组](https://leetcode.cn/problems/sorted-merge-lcci/)

- 标签：数组、双指针、排序
- 难度：简单

## 题目链接

- [面试题 10.01. 合并排序的数组 - 力扣](https://leetcode.cn/problems/sorted-merge-lcci/)

## 题目大意

**描述**：给定两个排序后的数组 `A` 和 `B`，以及 `A` 的元素数量 `m` 和 `B` 的元素数量 `n`。 `A` 的末端有足够的缓冲空间容纳 `B`。

**要求**：编写一个方法，将 `B` 合并入 `A` 并排序。

**说明**：

- $A.length == n + m$。

**示例**：

- 示例 1：

```python
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```

## 解题思路

### 思路 1：归并排序

可以利用归并排序算法的归并步骤思路。

1. 使用两个指针分别表示`A`、`B` 正在处理的元素下标。
2. 对 `A`、`B` 进行归并操作，将结果存入新数组中。归并之后，再将所有元素赋值到数组 `A` 中。

### 思路 1：代码

```python
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        arr = []
        index_A, index_B = 0, 0
        while index_A < m and index_B < n:
            if A[index_A] <= B[index_B]:
                arr.append(A[index_A])
                index_A += 1
            else:
                arr.append(B[index_B])
                index_B += 1
        while index_A < m:
            arr.append(A[index_A])
            index_A += 1
        while index_B < n:
            arr.append(B[index_B])
            index_B += 1
        for i in range(m + n):
            A[i] = arr[i]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$。
- **空间复杂度**：$O(m + n)$。

