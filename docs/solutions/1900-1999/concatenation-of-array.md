# [1929. 数组串联](https://leetcode.cn/problems/concatenation-of-array/)

- 标签：数组
- 难度：简单

## 题目链接

- [1929. 数组串联 - 力扣](https://leetcode.cn/problems/concatenation-of-array/)

## 题目大意

**描述**：给定一个长度为 $n$ 的整数数组 $nums$。

**要求**：构建一个长度为 $2 \times n$ 的答案数组 $ans$，答案数组下标从 $0$ 开始计数 ，对于所有 $0 \le i < n$ 的 $i$ ，满足下述所有要求：

- $ans[i] == nums[i]$。
- $ans[i + n] == nums[i]$。

具体而言，$ans$ 由两个 $nums$ 数组「串联」形成。

**说明**：

- $n == nums.length$。
- $1 \le n \le 1000$。
- $1 \le nums[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

- 示例 2：

```python
输入：nums = [1,3,2,1]
输出：[1,3,2,1,1,3,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

## 解题思路

### 思路 1：按要求模拟

1. 定义一个数组变量（列表）$ans$ 作为答案数组。
2. 然后按顺序遍历两次数组 $nums$ 中的元素，并依次添加到 $ans$ 的尾部。最后返回 $ans$。

### 思路 1：代码

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(n)$。如果算上答案数组的空间占用，则空间复杂度为 $O(n)$。不算上则空间复杂度为 $O(1)$。

### 思路 2：利用运算符

Python 中可以直接利用 `+` 号运算符将两个列表快速进行串联。即 `return nums + nums`。

### 思路 2：代码

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(n)$。如果算上答案数组的空间占用，则空间复杂度为 $O(n)$。不算上则空间复杂度为 $O(1)$。
