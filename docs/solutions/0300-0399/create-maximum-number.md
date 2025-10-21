# [0321. 拼接最大数](https://leetcode.cn/problems/create-maximum-number/)

- 标签：栈、贪心、数组、双指针、单调栈
- 难度：困难

## 题目链接

- [0321. 拼接最大数 - 力扣](https://leetcode.cn/problems/create-maximum-number/)

## 题目大意

**描述**：

给定两个整数数组 $nums1$ 和 $nums2$，它们的长度分别为 $m$ 和 $n$。数组 $nums1$ 和 $nums2$ 分别代表两个数各位上的数字。同时你也会得到一个整数 $k$。

**要求**：

请你利用这两个数组中的数字创建一个长度为 $k \le m + n$ 的最大数。同一数组中数字的相对顺序必须保持不变。

返回代表答案的长度为 $k$ 的数组。

**说明**：

- $m == nums1.length$。
- $n == nums2.length$。
- $1 \le m, n \le 500$。
- $0 \le nums1[i], nums2[i] \le 9$。
- $1 \le k \le m + n$。
- $nums1$ 和 $nums2$ 没有前导 $0$。

**示例**：

- 示例 1：

```python
输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
输出：[9,8,6,5,3]
```

- 示例 2：

```python
输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
输出：[6,7,6,0,4]
```

## 解题思路

### 思路 1：贪心 + 单调栈

这道题的核心思想是：对于长度为 $k$ 的最大数，我们需要从两个数组中选择数字，使得最终结果最大。

解题步骤：

1. **枚举所有可能的分割方式**：假设从 $nums1$ 中选择 $i$ 个数字，从 $nums2$ 中选择 $k-i$ 个数字，其中 $0 \le i \le \min(len(nums1), k)$ 且 $0 \le k-i \le len(nums2)$。
2. **从单个数组中选择最大子序列**：使用单调栈的思想，从 $nums1$ 中选择 $i$ 个数字组成最大子序列，从 $nums2$ 中选择 $k-i$ 个数字组成最大子序列。
3. **合并两个子序列**：将两个子序列合并成一个长度为 $k$ 的最大序列。
4. **比较所有可能的结果**：返回所有可能结果中的最大值。

关键算法：

- 使用单调栈从数组中选择 $k$ 个数字组成最大子序列。
- 使用双指针合并两个子序列，每次选择较大的数字。

### 思路 1：代码

```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxSubsequence(nums, k):
            """从数组中选择k个数字组成最大子序列"""
            stack = []
            # 需要删除的数字个数
            drop = len(nums) - k
            
            for num in nums:
                # 如果栈不为空，且当前数字大于栈顶数字，且还有数字可以删除
                while stack and num > stack[-1] and drop > 0:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            
            # 如果还有数字需要删除，从末尾删除
            return stack[:k]
        
        def merge(nums1, nums2):
            """合并两个数组，保持相对顺序，使结果最大"""
            result = []
            i = j = 0
            
            while i < len(nums1) and j < len(nums2):
                # 比较从当前位置开始的子序列，选择字典序更大的
                if nums1[i:] > nums2[j:]:
                    result.append(nums1[i])
                    i += 1
                else:
                    result.append(nums2[j])
                    j += 1
            
            # 添加剩余元素
            result.extend(nums1[i:])
            result.extend(nums2[j:])
            
            return result
        
        max_result = []
        
        # 枚举所有可能的分割方式
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            j = k - i
            
            # 从两个数组中选择最大子序列
            sub1 = getMaxSubsequence(nums1, i)
            sub2 = getMaxSubsequence(nums2, j)
            
            # 合并两个子序列
            merged = merge(sub1, sub2)
            
            # 更新最大结果
            if merged > max_result:
                max_result = merged
        
        return max_result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k \times (m + n) \times k)$，其中 $m$ 和 $n$ 分别是两个数组的长度。需要枚举 $O(k)$ 种分割方式，每种方式需要 $O(m + n)$ 时间选择子序列，$O(k)$ 时间合并。
- **空间复杂度**：$O(k)$，用于存储临时结果和栈。
