# [0996. 平方数组的数目](https://leetcode.cn/problems/number-of-squareful-arrays/)

- 标签：位运算、数组、哈希表、数学、动态规划、回溯、状态压缩
- 难度：困难

## 题目链接

- [0996. 平方数组的数目 - 力扣](https://leetcode.cn/problems/number-of-squareful-arrays/)

## 题目大意

**描述**：

如果一个数组的任意两个相邻元素之和都是「完全平方数」，则该数组称为「平方数组」。

给定一个整数数组 $nums$。

**要求**：

返回所有属于「平方数组」的 $nums$ 的排列数量。

**说明**：

- 如果存在某个索引 $i$ 使得 $perm1[i] \ne perm2[i]$，则认为两个排列 $perm1$ 和 $perm2$ 不同。
- $1 \le nums.length \le 12$。
- $0 \le nums[i] \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入：nums = [1,17,8]
输出：2
解释：[1,8,17] 和 [17,8,1] 是有效的排列。
```

- 示例 2：

```python
输入：nums = [2,2,2]
输出：1
```

## 解题思路

### 思路 1：回溯 + 剪枝

这道题需要找到所有满足条件的排列，可以使用回溯算法。

1. **判断完全平方数**：首先实现一个函数判断两个数之和是否为完全平方数。
2. **回溯搜索**：
   - 使用回溯算法生成所有排列
   - 在添加新元素时，检查与前一个元素的和是否为完全平方数
   - 使用访问标记避免重复使用元素
3. **剪枝优化**：
   - 对数组进行排序，方便去重
   - 如果当前元素与前一个元素相同且前一个元素未被使用，跳过（避免重复排列）
   - 预先计算哪些数字对可以相邻，构建图结构

### 思路 1：代码

```python
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        import math
        
        def is_square(n):
            """判断是否为完全平方数"""
            root = int(math.sqrt(n))
            return root * root == n
        
        nums.sort()
        n = len(nums)
        visited = [False] * n
        self.count = 0
        
        def backtrack(path):
            if len(path) == n:
                self.count += 1
                return
            
            for i in range(n):
                # 跳过已使用的元素
                if visited[i]:
                    continue
                
                # 去重：如果当前元素与前一个元素相同，且前一个元素未被使用，跳过
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                # 检查是否满足平方数条件
                if path and not is_square(path[-1] + nums[i]):
                    continue
                
                # 选择当前元素
                visited[i] = True
                path.append(nums[i])
                backtrack(path)
                # 撤销选择
                path.pop()
                visited[i] = False
        
        backtrack([])
        return self.count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n! \times n)$，其中 $n$ 是数组长度。最坏情况下需要遍历所有排列，每次检查需要 $O(n)$ 时间。
- **空间复杂度**：$O(n)$，递归栈和访问标记数组的空间。
