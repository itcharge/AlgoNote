# [1460. 通过翻转子数组使两个数组相等](https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-subarrays/)

- 标签：数组、哈希表、排序
- 难度：简单

## 题目链接

- [1460. 通过翻转子数组使两个数组相等 - 力扣](https://leetcode.cn/problems/make-two-arrays-equal-by-reversing-subarrays/)

## 题目大意

**描述**：给定两个长度相同的数组 $target$ 和 $arr$，每一步可以选择 $arr$ 的任意非空子数组并翻转。

**要求**：判断能否通过若干次翻转操作使 $arr$ 变得与 $target$ 相等。

**说明**：
- $1 \le target.length = arr.length \le 1000$。

**示例**：

- 示例 1：

```python
输入：target = [1,2,3,4], arr = [2,4,1,3]
输出：true
解释：你可以按照如下步骤使 arr 变成 target：
1- 翻转子数组 [2,4,1] ，arr 变成 [1,4,2,3]
2- 翻转子数组 [4,2] ，arr 变成 [1,2,4,3]
3- 翻转子数组 [4,3] ，arr 变成 [1,2,3,4]
上述方法并不是唯一的，还存在多种将 arr 变成 target 的方法。
```

- 示例 2：

```python
输入：target = [7], arr = [7]
输出：true
解释：arr 不需要做任何翻转已经与 target 相等。
```

## 解题思路

### 思路 1：排序比较

#### 1. 核心思想

反转子数组可以任意重排 $arr$（因为反转两个元素的子数组等价于交换相邻元素）。因此只需检查两个数组的元素是否相同（同一个集合的排列）。

#### 2. 具体步骤

**第 1 步**：对 $target$ 和 $arr$ 分别排序。

**第 2 步**：比较排序后的数组是否完全相同。

#### 3. 举例说明

以 $target = [1,2,3,4], arr = [2,4,1,3]$ 为例：

排序后：$target = [1,2,3,4], arr = [1,2,3,4]$，相同 → 返回 $True$。

### 思路 1：代码

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序。
- **空间复杂度**：$O(n)$，排序额外空间。

---

### 思路 2：哈希计数

```python
from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
```

$O(n)$ 时间，$O(n)$ 空间。
