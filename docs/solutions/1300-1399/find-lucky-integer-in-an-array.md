# [1394. 找出数组中的幸运数](https://leetcode.cn/problems/find-lucky-integer-in-an-array/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [1394. 找出数组中的幸运数 - 力扣](https://leetcode.cn/problems/find-lucky-integer-in-an-array/)

## 题目大意

**描述**：给定一个整数数组 $arr$。幸运数是指一个整数在数组中出现的次数等于它本身的值。

**要求**：返回最大的幸运数。如果没有，返回 $-1$。

**说明**：
- $1 \le arr.length \le 500$。
- $1 \le arr[i] \le 500$。

**示例**：

- 示例 1：

```python
输入：arr = [2,2,3,4]
输出：2
解释：数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。
```

- 示例 2：

```python
输入：arr = [1,2,2,3,3,3]
输出：3
解释：1、2 以及 3 都是幸运数，只需要返回其中最大的 3 。
```


## 解题思路

### 思路 1：哈希表

#### 1. 核心思想

用哈希表统计每个数字的出现次数，然后遍历哈希表，找出满足 $key == value$ 的最大 $key$。

#### 2. 代码

```python
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        ans = -1
        for num, cnt in freq.items():
            if num == cnt:
                ans = max(ans, num)
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
