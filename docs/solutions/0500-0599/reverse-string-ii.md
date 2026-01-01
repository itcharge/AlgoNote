# [0541. 反转字符串 II](https://leetcode.cn/problems/reverse-string-ii/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0541. 反转字符串 II - 力扣](https://leetcode.cn/problems/reverse-string-ii/)

## 题目大意

**描述**：

给定一个字符串 $s$ 和一个整数 $k$。

**要求**：

从字符串开头算起，每计数至 $2 \times k$ 个字符，就反转这 $2 \times k$ 字符中的前 $k$ 个字符。
- 如果剩余字符少于 $k$ 个，则将剩余字符全部反转。
- 如果剩余字符小于 $2 \times k$ 但大于或等于 $k$ 个，则反转前 $k$ 个字符，其余字符保持原样。

**说明**：

- $1 \le s.length \le 10^{4}$。
- $s$ 仅由小写英文组成。
- $1 \le k \le 10^{4}$。

**示例**：

- 示例 1：

```python
输入：s = "abcdefg", k = 2
输出："bacdfeg"
```

- 示例 2：

```python
输入：s = "abcd", k = 2
输出："bacd"
```

## 解题思路

### 思路 1：分段反转

按照题目要求，每 $2 \times k$ 个字符为一组进行处理：

- 对于每组的前 $k$ 个字符进行反转
- 后 $k$ 个字符保持原样

具体实现：

1. 遍历字符串，每次步进 $2 \times k$ 个字符
2. 对于每个区间 $[i, i + 2 \times k)$：
   - 如果剩余字符 $\ge k$，反转前 $k$ 个字符（即 $[i, i + k)$）
   - 如果剩余字符 $< k$，反转所有剩余字符

### 思路 1：代码

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        n = len(s_list)
        
        # 每次处理 2k 个字符
        for i in range(0, n, 2 * k):
            # 确定反转的右边界：取 min(i + k, n)
            left = i
            right = min(i + k - 1, n - 1)
            
            # 反转 [left, right] 区间
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度，需要遍历字符串一次。
- **空间复杂度**：$O(n)$，需要将字符串转换为列表进行操作。
