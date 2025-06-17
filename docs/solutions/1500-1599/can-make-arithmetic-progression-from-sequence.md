# [1502. 判断能否形成等差数列](https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [1502. 判断能否形成等差数列 - 力扣](https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/)

## 题目大意

**描述**：给定一个数字数组 `arr`。如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数序就称为等差数列。

**要求**：如果数组 `arr` 通过重新排列可以形成等差数列，则返回 `True`；否则返回 `False`。

**说明**：

- $2 \le arr.length \le 1000$
- $-10^6 \le arr[i] \le 10^6$

**示例**：

- 示例 1：

```python
输入：arr = [3,5,1]
输出：True
解释：数组重新排序后得到 [1,3,5] 或者 [5,3,1]，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
```

## 解题思路

### 思路 1：

- 如果数组元素个数小于等于 `2`，则数组肯定可以形成等差数列，直接返回 `True`。
- 对数组进行排序。
- 从下标为 `2` 的元素开始，遍历相邻的 `3` 个元素 `arr[i]` 、`arr[i - 1]`、`arr[i - 2]`。判断 `arr[i] - arr[i - 1]` 是否等于 `arr[i - 1] - arr[i - 2]`。如果不等于，则数组无法形成等差数列，返回 `False`。
- 如果遍历完数组，则说明数组可以形成等差数列，返回 `True`。

## 代码

### 思路 1 代码：

```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        size = len(arr)
        if size <= 2:
            return True

        arr.sort()
        for i in range(2, size):
            if arr[i] - arr[i - 1] != arr[i - 1] - arr[i - 2]:
                return False
        return True
```

