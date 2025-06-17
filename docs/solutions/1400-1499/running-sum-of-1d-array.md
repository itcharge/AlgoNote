# [1480. 一维数组的动态和](https://leetcode.cn/problems/running-sum-of-1d-array/)

- 标签：数组、前缀和
- 难度：简单

## 题目链接

- [1480. 一维数组的动态和 - 力扣](https://leetcode.cn/problems/running-sum-of-1d-array/)

## 题目大意

**描述**：给定一个数组 $nums$。

**要求**：返回数组 $nums$ 的动态和。

**说明**：

- **动态和**：数组前 $i$ 项元素和构成的数组，计算公式为 $runningSum[i] = \sum_{x = 0}^{x = i}(nums[i])$。
- $1 \le nums.length \le 1000$。
- $-10^6 \le nums[i] \le 10^6$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4]。
```

- 示例 2：

```python
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]。
```

## 解题思路

### 思路 1：递推

根据动态和的公式 $runningSum[i] = \sum_{x = 0}^{x = i}(nums[i])$，可以推导出：

$runningSum = \begin{cases} nums[0], & i = 0 \cr runningSum[i - 1] + nums[i], & i > 0\end{cases}$

则解决过程如下：

1. 新建一个长度等于 $nums$ 的数组 $res$ 用于存放答案。
2. 初始化 $res[0] = nums[0]$。
3. 从下标 $1$ 开始遍历数组 $nums$，递推更新 $res$，即：`res[i] = res[i - 1] + nums[i]`。
4. 遍历结束，返回 $res$ 作为答案。

### 思路 1：代码

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [0 for _ in range(size)]
        for i in range(size):
            if i == 0:
                res[i] = nums[i]
            else:
                res[i] = res[i - 1] + nums[i]
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。一重循环遍历的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(n)$。如果算上答案数组的空间占用，则空间复杂度为 $O(n)$。不算上则空间复杂度为 $O(1)$。

