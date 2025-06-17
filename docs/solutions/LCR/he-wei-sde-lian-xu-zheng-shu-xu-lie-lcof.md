# [LCR 180. 文件组合](https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

- 标签：数学、双指针、枚举
- 难度：简单

## 题目链接

- [LCR 180. 文件组合 - 力扣](https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

## 题目大意

**描述**：给定一个正整数 `target`。

**要求**：输出所有和为 `target` 的连续正整数序列（至少含有两个数）。序列中的数字由小到大排列，不同序列按照首个数字从小到大排列。

**说明**：

- $1 \le target \le 10^5$。

**示例**：

- 示例 1：

```python
输入：target = 9
输出：[[2,3,4],[4,5]]
```

- 示例 2：

```python
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

## 解题思路

### 思路 1：枚举算法

连续正整数序列中元素的最小值大于等于 `1`，而最大值不会超过 `target`。所以我们可以枚举可行的区间，并计算出区间和，将其与 `target` 进行比较，如果相等则将对应的区间元素加入答案数组中，最终返回答案数组。

因为题目要求至少含有两个数，则序列开始元素不会超过 `target` 的一半，所以序列开始元素可以从 `1` 开始，枚举到 `target // 2` 即可。

具体步骤如下：

1. 使用列表变量 `res` 作为答案数组。
2. 使用一重循环 `i`，用于枚举序列开始位置，枚举范围为 `[1, target // 2]`。
3. 使用变量 `cur_sum` 维护当前区间的区间和，`cur_sum` 初始为 `0`。
4. 使用第 `2` 重循环 `j`，用于枚举序列的结束位置，枚举范围为 `[i, target - 1]`，并累积计算当前区间的区间和，即 `cur_sum += j`。
   1. 如果当前区间的区间和大于 `target`，则跳出循环。
   2. 如果当前区间的区间和等于 `target`，则将区间上的元素保存为列表，并添加到答案数组中，然后跳出第 `2` 重循环。
5. 遍历完返回答案数组。

### 思路 1：代码

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(1, target // 2 + 1):
            cur_sum = 0
            for j in range(i, target):
                cur_sum += j
                if cur_sum > target:
                    break
                if cur_sum == target:
                    cur_res = []
                    for k in range(i, j + 1):
                        cur_res.append(k)
                    res.append(cur_res)
                    break
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$target \times \sqrt{target}$。
- **空间复杂度**：$O(1)$。

### 思路 2：滑动窗口

具体做法如下：

- 初始化窗口，令 `left = 1`，`right = 2`。
- 计算 `sum = (left + right) * (right - left + 1) // 2`。
- 如果 `sum == target`，时，将其加入答案数组中。
- 如果 `sum < target` 时，说明需要扩大窗口，则 `right += 1`。
- 如果 `sum > target` 时，说明需要缩小窗口，则 `left += 1`。
- 直到 `left >= right` 时停止，返回答案数组。

### 思路 2：滑动窗口代码

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        res = []
        while left < right:
            sum = (left + right) * (right - left + 1) // 2
            if sum == target:
                arr = []
                for i in range(0, right - left + 1):
                    arr.append(i + left)
                res.append(arr)
                left += 1
            elif sum < target:
                right += 1
            else:
                left += 1
        return res
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(target)$。
- **空间复杂度**：$O(1)$。
