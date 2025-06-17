# [0845. 数组中的最长山脉](https://leetcode.cn/problems/longest-mountain-in-array/)

- 标签：数组、双指针、动态规划、枚举
- 难度：中等

## 题目链接

- [0845. 数组中的最长山脉 - 力扣](https://leetcode.cn/problems/longest-mountain-in-array/)

## 题目大意

**描述**：给定一个整数数组 $arr$。

**要求**：返回最长山脉子数组的长度。如果不存在山脉子数组，返回 $0$。

**说明**：

- **山脉数组**：符合下列属性的数组 $arr$ 称为山脉数组。
  - $arr.length \ge 3$。
  - 存在下标 $i(0 < i < arr.length - 1)$ 满足：
    - $arr[0] < arr[1] < … < arr[i]$
    - $arr[i] > arr[i + 1] > … > arr[arr.length - 1]$

- $1 \le arr.length \le 10^4$。
- $0 \le arr[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [2,1,4,7,3,2,5]
输出：5
解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
```

- 示例 2：

```python
输入：arr = [2,2,2]
输出：0
解释：不存在山脉子数组。
```

## 解题思路

### 思路 1：快慢指针

1. 使用变量 $ans$ 保存最长山脉长度。
2. 遍历数组，假定当前节点为山峰。
3. 使用双指针 $left$、$right$ 分别向左、向右查找山脉的长度。
4. 如果当前山脉的长度比最长山脉长度更长，则更新最长山脉长度。
5. 最后输出 $ans$。

### 思路 1：代码

```python
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        size = len(arr)
        res = 0
        for i in range(1, size - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < size - 1 and arr[right + 1] < arr[right]:
                    right += 1
                if right - left + 1 > res:
                    res = right - left + 1
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $arr$ 中的元素数量。
- **空间复杂度**：$O(1)$。

