# [0440. 字典序的第K小数字](https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/)

- 标签：字典树
- 难度：困难

## 题目链接

- [0440. 字典序的第K小数字 - 力扣](https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/)

## 题目大意

**描述**：

给定整数 $n$ 和 $k$。

**要求**：

返回 $[1, n]$ 中字典序第 $k$ 小的数字。

**说明**：

- $1 \le k \le n \le 10^{9}$。

**示例**：

- 示例 1：

```python
输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
```

- 示例 2：

```python
输入: n = 1, k = 1
输出: 1
```

## 解题思路

### 思路 1：前缀计数法

这道题可以利用字典树（十叉树）的思想来解决。我们可以将 $[1, n]$ 中的数字看作一棵字典树的节点，每个节点最多有 $10$ 个子节点（$0-9$）。

核心思路是：**通过前缀计数的方式，逐步确定第 $k$ 小数字的每一位**。

算法步骤：
1. **初始化**：从 $prefix = 1$ 开始，$k = k$（还需要找到的数字数量）。
2. **前缀搜索**：对于当前前缀 $prefix$，计算以它为前缀且不超过 $n$ 的数字个数 $count$。
3. **判断**：
   - 如果 $count < k$，说明第 $k$ 小的数字不在以 $prefix$ 为前缀的子树中，跳过这些数字，更新 $k = k - count$，并尝试下一个前缀 $prefix + 1$。
   - 如果 $count \ge k$，说明第 $k$ 小的数字在以 $prefix$ 为前缀的子树中，将 $prefix$ 作为当前位的结果，继续深入下一层，即 $prefix = prefix \times 10$，$k = k - 1$（因为 $prefix$ 本身也是一个数字）。
4. **重复**直到 $k = 0$，此时 $prefix$ 就是所求的第 $k$ 小数字。

对于**计算前缀数量**的辅助函数 $countPrefix(prefix, n)$：
- 从 $prefix$ 开始，统计所有以 $prefix$ 为前缀且在 $[1, n]$ 范围内的数字。
- 使用层次遍历的方式：下一层的数字为 $prefix \times 10$ 到 $prefix \times 10 + 9$。
- 例如 $countPrefix(1, 13) = 7$（包含 $1, 10, 11, 12, 13$），$countPrefix(2, 13) = 1$（只包含 $2$）。

### 思路 1：代码

```python
class Solution:
    def countPrefix(self, prefix: int, n: int) -> int:
        """计算以 prefix 为前缀且在 [1, n] 范围内的数字个数"""
        count = 0
        # 当前层的数字范围
        first = prefix  # 当前层第一个数字
        next_prefix = prefix + 1  # 下一层前缀
        
        while first <= n:
            # 计算当前层有多少个数字（不超过 n）
            count += min(next_prefix, n + 1) - first
            # 移动到下一层（扩大10倍）
            first *= 10
            next_prefix *= 10
        
        return count
    
    def findKthNumber(self, n: int, k: int) -> int:
        # 初始化：从前缀 1 开始
        prefix = 1
        k = k  # 还需要找到的数字数量
        
        while k > 1:
            # 计算以当前 prefix 为前缀且不超过 n 的数字个数
            count = self.countPrefix(prefix, n)
            
            if count < k:
                # 如果数量少于 k，说明第 k 小的数字不在这个前缀下
                # 跳过这些数字，尝试下一个前缀
                k -= count
                prefix += 1
            else:
                # 如果数量大于等于 k，说明第 k 小的数字在这个前缀下
                # 继续深入这一层，prefix 作为当前位的结果
                k -= 1
                prefix *= 10
        
        return prefix
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log^2 n)$，其中 $n$ 是给定的数字范围。外层循环最多执行 $O(\log n)$ 次（每层确定一位数字），内层 $countPrefix$ 函数的时间复杂度也为 $O(\log n)$（因为需要逐层计算，层数不超过 $\log_{10} n$）。总体时间复杂度为 $O(\log^2 n)$。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
