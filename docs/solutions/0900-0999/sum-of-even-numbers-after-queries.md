# [0985. 查询后的偶数和](https://leetcode.cn/problems/sum-of-even-numbers-after-queries/)

- 标签：数组、模拟
- 难度：中等

## 题目链接

- [0985. 查询后的偶数和 - 力扣](https://leetcode.cn/problems/sum-of-even-numbers-after-queries/)

## 题目大意

**描述**：

给定一个整数数组 A 和一个查询数组 $queries$。

对于第 $i$ 次查询，有 $val = queries[i][0]$, $index = queries[i][1]$，我们会把 $val$ 加到 $A[index]$ 上。然后，第 $i$ 次查询的答案是 A 中偶数值的和。
（此处给定的 $index = queries[i][1]$ 是从 0 开始的索引，每次查询都会永久修改数组 A。）

**要求**：

返回所有查询的答案。你的答案应当以数组 $answer$ 给出，$answer[i]$ 为第 $i$ 次查询的答案。

**说明**：

- $1 \le A.length \le 10^{000}$。
- $-10^{000} \le A[i] \le 10^{000}$。
- $1 \le queries.length \le 10^{000}$。
- $-10^{000} \le queries[i][0] \le 10^{000}$。
- $0 \le queries[i][1] \lt A.length$。

**示例**：

- 示例 1：

```python
输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
输出：[8,6,2,4]
解释：
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
```

## 解题思路

### 思路 1：模拟

先计算初始的偶数和，然后对每次查询进行模拟。

1. 先遍历数组 $nums$，计算初始的偶数和 $even\_sum$。
2. 对于每次查询 $[val, index]$：
   - 如果 $nums[index]$ 是偶数，从 $even\_sum$ 中减去它。
   - 更新 $nums[index] = nums[index] + val$。
   - 如果更新后的 $nums[index]$ 是偶数，将它加到 $even\_sum$ 中。
   - 将当前的 $even\_sum$ 加入结果数组。
3. 返回结果数组。

### 思路 1：代码

```python
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 计算初始偶数和
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []
        
        for val, index in queries:
            # 如果原来是偶数，先从和中减去
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            # 更新值
            nums[index] += val
            
            # 如果更新后是偶数，加到和中
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            result.append(even_sum)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + q)$，其中 $n$ 是数组 $nums$ 的长度，$q$ 是查询数组 $queries$ 的长度。
- **空间复杂度**：$O(1)$，不考虑结果数组的空间。
