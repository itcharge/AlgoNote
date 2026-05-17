# [1287. 有序数组中出现次数超过25%的元素](https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/)

- 标签：数组
- 难度：简单

## 题目链接

- [1287. 有序数组中出现次数超过25%的元素 - 力扣](https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array/)

## 题目大意

**描述**：给你一个非递减的有序整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 $25\%$。

**要求**：找到并返回这个整数。

**说明**：

- $1 \le arr.length \le 10^4$。
- $0 \le arr[i] \le 10^5$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6
```

## 解题思路

### 思路 1：遍历计数

###### 1. 核心思想

数组是有序的，相同的元素一定连续排列在一起。我们可以从头到尾遍历数组，统计当前元素的出现次数。一旦某个元素的出现次数超过了数组长度的 $25\%$，它就是我们要找的元素。

###### 2. 具体步骤

**第 1 步：计算阈值**

计算 $25\%$ 阈值 $t = n // 4$（向下取整）。因为题目说「超过 $25\%$」，所以出现次数需要 $> n/4$。

**第 2 步：遍历并计数**

- 初始化 $count = 0$，记录当前元素的连续出现次数。
- 遍历数组：
  - 如果 $i == 0$ 或 $arr[i] == arr[i-1]$（和上一个相同），$count += 1$。
  - 否则（遇到了新元素），重置 $count = 1$。
  - 如果 $count > t$，返回 $arr[i]$。

### 思路 1：代码

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        t = n // 4  # 25% 阈值
        count = 0
        for i in range(n):
            if i == 0 or arr[i] == arr[i - 1]:
                # 和上一个元素相同，计数器加 1
                count += 1
            else:
                # 遇到了新元素，重置计数
                count = 1
            if count > t:
                return arr[i]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，需要遍历一次整个数组。
- **空间复杂度**：$O(1)$，只使用了常数个变量。

### 思路 2：跳跃检查

###### 1. 核心思想

因为某个元素出现次数超过 $25\%$，所以如果我们在数组的 $25\%$、$50\%$、$75\%$ 位置（即 $n/4$、$n/2$、$3n/4$ 下标处）分别取样，目标元素必定会出现在至少一个采样位置。利用这个性质，只需要检查 $3$ 个候选元素即可。

###### 2. 具体步骤

**第 1 步：确定候选位置**

计算三个候选下标：$n//4$、$n//2$、$3n//4$。

**第 2 步：检查每个候选元素**

对于每个候选下标 $i$，记 $val = arr[i]$：
- 使用二分查找的 `bisect_left` 找到 $val$ 在数组中的第一个出现位置。
- 使用二分查找的 `bisect_right` 找到 $val$ 在数组中的最后一个出现位置的下一位。
- 出现次数 = $right - left$，如果 $> n/4$，返回 $val$。

因为题目保证有且只有一个元素符合条件，所以三个候选中必然有一个满足。

### 思路 2：代码

```python
import bisect

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        t = n // 4
        # 检查三个候选位置
        for i in [n // 4, n // 2, 3 * n // 4]:
            val = arr[i]
            # 二分查找 val 的左右边界
            left = bisect.bisect_left(arr, val)
            right = bisect.bisect_right(arr, val)
            if right - left > t:
                return val
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(\log n)$，每次二分查找 $O(\log n)$，最多 $3$ 次，远优于思路 1 的 $O(n)$。
- **空间复杂度**：$O(1)$。
