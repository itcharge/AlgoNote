# [0247. 中心对称数 II](https://leetcode.cn/problems/strobogrammatic-number-ii/)

- 标签：递归、数组、字符串
- 难度：中等

## 题目链接

- [0247. 中心对称数 II - 力扣](https://leetcode.cn/problems/strobogrammatic-number-ii/)

## 题目大意

**描述**：

给定一个整数 $n$。

**要求**：

返回所有长度为 $n$ 的「中心对称数」。你可以以任何顺序返回答案。

**说明**：

- 中心对称数：指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
- $1 \le n \le 14$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出：["11","69","88","96"]
```

- 示例 2：

```python
输入：n = 1
输出：["0","1","8"]
```

## 解题思路

### 思路 1：递归构建

中心对称数是指旋转 180 度后看起来相同的数字。只有特定的数字可以构成中心对称数：

- $0$ 旋转后还是 $0$。
- $1$ 旋转后还是 $1$。
- $6$ 旋转后变成 $9$。
- $8$ 旋转后还是 $8$。
- $9$ 旋转后变成 $6$。

使用递归方法从外向内构建中心对称数：

- 对于长度为 $n$ 的中心对称数，我们从两端开始构建。
- 每次选择一对可以相互旋转的数字 $(a, b)$，其中 $a$ 旋转后变成 $b$。
- 递归处理中间部分，直到构建完成。
- 特殊情况：当 $n$ 为奇数时，中间位置只能放置 $0, 1, 8$；当 $n$ 为偶数时，从空字符串开始构建。
- 注意：不能以 $0$ 开头（除非 $n = 1$）。

### 思路 1：代码

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # 定义中心对称数字的映射关系
        strobogrammatic_pairs = [
            ('0', '0'), ('1', '1'), ('6', '9'), 
            ('8', '8'), ('9', '6')
        ]
        
        def build_strobogrammatic(m):
            # 递归构建长度为 m 的中心对称数
            if m == 0:
                return [""]  # 空字符串
            if m == 1:
                return ["0", "1", "8"]  # 单个数字的情况
            
            # 递归构建中间部分
            inner = build_strobogrammatic(m - 2)
            result = []
            
            for pair in strobogrammatic_pairs:
                left, right = pair
                for inner_str in inner:
                    # 构建完整的中心对称数
                    result.append(left + inner_str + right)
            
            return result
        
        # 获取所有可能的中心对称数
        candidates = build_strobogrammatic(n)
        
        # 过滤掉以 0 开头的数字（除非 n = 1）
        if n == 1:
            return candidates
        else:
            return [num for num in candidates if not num.startswith('0')]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(5^{n/2} \times n)$，其中 $n$ 是目标长度。每次递归有 5 种选择，递归深度为 $n/2$，每个结果字符串长度为 $n$。
- **空间复杂度**：$O(5^{n/2} \times n)$，存储所有可能的中心对称数结果。
