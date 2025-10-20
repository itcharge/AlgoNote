# [0248. 中心对称数 III](https://leetcode.cn/problems/strobogrammatic-number-iii/)

- 标签：递归、数组、字符串
- 难度：困难

## 题目链接

- [0248. 中心对称数 III - 力扣](https://leetcode.cn/problems/strobogrammatic-number-iii/)

## 题目大意

**描述**：

给定两个字符串 $low$ 和 $high$ 表示两个整数 $low$ 和 $high$，其中 $low \le high$。

**要求**：

返回范围 $[low, high]$ 内的「中心对称数」总数。

**说明**：

- 中心对称数：指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
- $1 \le low.length, high.length \le 15$。
- low 和 high 只包含数字。
- $low \le high$。
- $low$ 和 $high$ 不包含任何前导零，除了零本身。

**示例**：

- 示例 1：

```python
输入: low = "50", high = "100"
输出: 3
```

- 示例 2：

```python
输入: low = "0", high = "0"
输出: 1
```

## 解题思路

### 思路 1：递归生成 + 计数

中心对称数只能由数字 $\{0, 1, 6, 8, 9\}$ 组成，其中：

- $0$ 旋转后还是 $0$。
- $1$ 旋转后还是 $1$。
- $6$ 旋转后变成 $9$。
- $8$ 旋转后还是 $8$。
- $9$ 旋转后变成 $6$。

对于长度为 $n$ 的中心对称数，我们可以递归生成：

- 当 $n = 0$ 时：返回空字符串
- 当 $n = 1$ 时：只能是 $\{0, 1, 8\}$
- 当 $n > 1$ 时：
  - 外层可以是 $\{0, 1, 6, 8, 9\}$，但最外层不能是 $0$（避免前导零）
  - 内层递归生成长度为 $n-2$ 的中心对称数

算法步骤：

1. 生成所有长度在 $[\text{len}(low), \text{len}(high)]$ 范围内的中心对称数
2. 过滤出在 $[low, high]$ 范围内的数字
3. 返回符合条件的数字个数

关键点：

- 最外层不能是 $0$，避免生成前导零。
- 内层可以是 $0$，如 `"1001"` 是有效的中心对称数。
- 对于数字字符串的比较，需要先比较长度，再比较字典序。

### 思路 1：代码

```python
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        # 定义中心对称数字的映射关系
        strobogrammatic_map = {
            '0': '0',
            '1': '1', 
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        def generate_strobogrammatic(n, length):
            """递归生成长度为 n 的中心对称数，length 表示目标长度"""
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            
            # 递归生成长度为 n-2 的中心对称数
            shorter = generate_strobogrammatic(n - 2, length)
            result = []
            
            for s in shorter:
                # 对于中间的数字，可以是 0, 1, 6, 8, 9
                for outer in ['0', '1', '6', '8', '9']:
                    # 如果是最外层且长度 > 1，外层不能是 0（避免前导零）
                    if n != length or outer != '0':
                        result.append(outer + s + strobogrammatic_map[outer])
            
            return result
        
        def is_in_range(num_str, low, high):
            """判断数字是否在指定范围内"""
            # 先比较长度，再比较字符串内容
            if len(num_str) < len(low) or len(num_str) > len(high):
                return False
            
            # 如果长度在中间，肯定在范围内
            if len(num_str) > len(low) and len(num_str) < len(high):
                return True
            
            # 长度相等时，直接比较字符串
            if len(num_str) == len(low) and len(num_str) == len(high):
                return low <= num_str <= high
            elif len(num_str) == len(low):
                return num_str >= low
            elif len(num_str) == len(high):
                return num_str <= high
            
            return False
        
        count = 0
        low_len, high_len = len(low), len(high)
        
        # 生成所有长度在 [low_len, high_len] 范围内的中心对称数
        for length in range(low_len, high_len + 1):
            strobogrammatic_nums = generate_strobogrammatic(length, length)
            
            for num in strobogrammatic_nums:
                if is_in_range(num, low, high):
                    count += 1
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(5^{n/2} \times n)$，其中 $n$ 是最大长度。递归生成所有可能的中心对称数，每个数字需要 $O(n)$ 时间进行范围检查。
- **空间复杂度**：$O(5^{n/2} \times n)$，存储所有生成的中心对称数。

具体分析：
- 对于长度为 $k$ 的中心对称数，有 $5^{k/2}$ 个（外层 4 种选择，内层 5 种选择）。
- 总共有 $\sum_{k=\text{len}(low)}^{\text{len}(high)} 5^{k/2}$ 个中心对称数。
- 每个数字的字符串比较需要 $O(k)$ 时间。
