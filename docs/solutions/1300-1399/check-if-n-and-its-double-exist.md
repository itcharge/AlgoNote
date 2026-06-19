# [1346. 检查整数及其两倍数是否存在](https://leetcode.cn/problems/check-if-n-and-its-double-exist/)

- 标签：数组、哈希表、双指针、二分查找
- 难度：简单

## 题目链接

- [1346. 检查整数及其两倍数是否存在 - 力扣](https://leetcode.cn/problems/check-if-n-and-its-double-exist/)

## 题目大意

**描述**：给定一个整数数组 $arr$。

**要求**：检查是否存在两个不同的下标 $i$ 和 $j$，使得 $arr[i] = 2 \times arr[j]$。

**说明**：
- $2 \le arr.length \le 500$。
- $-10^3 \le arr[i] \le 10^3$。

**示例**：
- 示例 1：
```python
输入：arr = [10,2,5,3]
输出：true
解释：10 = 2 * 5。
```
- 示例 2：
```python
输入：arr = [3,1,7,11]
输出：false
```

## 解题思路

### 思路 1：哈希集合

#### 1. 核心思想

遍历数组，用集合记录已出现的数。对每个数检查它的两倍和它的一半是否出现过（注意偶数的一半才是整数）。

需要特别注意数字 $0$ 的情况：$0$ 的两倍是 $0$，所以如果 $0$ 出现过至少两次，也返回 $True$。用集合 + 条件判断可以处理。

#### 2. 具体步骤

**第 1 步**：初始化集合 $seen$。

**第 2 步**：遍历 $arr$：
- 如果 $arr[i] \times 2$ 在 $seen$ 中，返回 $True$。
- 如果 $arr[i] \% 2 == 0$ 且 $arr[i] // 2$ 在 $seen$ 中，返回 $True$。
- 将 $arr[i]$ 加入 $seen$。

**第 3 步**：返回 $False$。

### 思路 1：代码

```python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
