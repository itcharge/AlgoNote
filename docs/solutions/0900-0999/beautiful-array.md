# [0932. 漂亮数组](https://leetcode.cn/problems/beautiful-array/)

- 标签：数组、数学、分治
- 难度：中等

## 题目链接

- [0932. 漂亮数组 - 力扣](https://leetcode.cn/problems/beautiful-array/)

## 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回长度为 $n$ 的任一漂亮数组。

**说明**：

- **漂亮数组**（长度为 $n$ 的数组 $nums$ 满足下述条件）：
  - $nums$ 是由范围 $[1, n]$ 的整数组成的一个排列。
  - 对于每个 $0 \le i < j < n$，均不存在下标 $k$（$i < k < j$）使得 $2 \times nums[k] == nums[i] + nums[j]$。
- $1 \le n \le 1000$。
- 本题保证对于给定的 $n$ 至少存在一个有效答案。

**示例**：

- 示例 1：

```python
输入：n = 4
输出：[2,1,4,3]
```

- 示例 2：

```python
输入：n = 5
输出：[3,1,2,5,4]
```

## 解题思路

### 思路 1：分治算法

根据题目要求，我们可以得到以下信息：

1. 题目要求 $2 \times nums[k] == nums[i] + nums[j], (0 \le i < k < j < n)$ 不能成立，可知：等式左侧必为偶数，只要右侧和为奇数则等式不成立。
2. 已知：奇数 + 偶数 = 奇数，则令 $nums[i]$ 和 $nums[j]$ 其中一个为奇数，另一个为偶数，即可保证 $nums[i] + nums[j]$ 一定为奇数。这里我们不妨令 $nums[i]$ 为奇数，令 $nums[j]$ 为偶数。
3. 如果数组 $nums$ 是漂亮数组，那么对数组 $nums$ 的每一位元素乘以一个常数或者加上一个常数之后，$nums$ 仍是漂亮数组。
   - 即如果 $[a_1, a_2, ..., a_n]$ 是一个漂亮数组，那么 $[k \times a_1 + b, k \times a_2 + b, ..., k \times a_n + b]$ 也是漂亮数组。

那么，我们可以按照下面的规则构建长度为 $n$ 的漂亮数组。

1. 当 $n = 1$ 时，返回 $[1]$。此时数组 $nums$ 中仅有 $1$ 个元素，并且满足漂亮数组的条件。
2. 当 $n > 1$ 时，我们将 $nums$ 分解为左右两个部分：`left_nums`、`right_nums`。如果左右两个部分满足：
   1. 数组 `left_nums` 中元素全为奇数（可以通过 `nums[i] * 2 - 1` 将 `left_nums` 中元素全部映射为奇数）。
   2. 数组 `right_nums` 中元素全为偶数（可以通过 `nums[i] * 2` 将 `right_nums` 中元素全部映射为偶数）。
   3. `left_nums` 和 `right_nums` 都是漂亮数组。
3. 那么 `left_nums + right_nums` 构成的数组一定也是漂亮数组，即 $nums$ 为漂亮数组，将 $nums$ 返回即可。

### 思路 1：代码

```python
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        nums = [0 for _ in range(n)]
        left_cnt = (n + 1) // 2
        right_cnt = n - left_cnt
        left_nums = self.beautifulArray(left_cnt)
        right_nums = self.beautifulArray(right_cnt)

        for i in range(left_cnt):
            nums[i] = 2 * left_nums[i] - 1
        
        for i in range(right_cnt):
            nums[left_cnt + i] = 2 * right_nums[i]
        
        return nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(n \times \log n)$。
