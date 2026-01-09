# [0917. 仅仅反转字母](https://leetcode.cn/problems/reverse-only-letters/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0917. 仅仅反转字母 - 力扣](https://leetcode.cn/problems/reverse-only-letters/)

## 题目大意

**描述**：

给定一个字符串 $s$ ，根据下述规则反转字符串：

- 所有非英文字母保留在原有位置。
- 所有英文字母（小写或大写）位置反转。

**要求**：

返回反转后的 $s$。

**说明**：

- $1 \le s.length \le 100$
- $s$ 仅由 ASCII 值在范围 $[33, 122]$ 的字符组成
- $s$ 不含 `'\"'` 或 `'\\'`

**示例**：

- 示例 1：

```python
输入：s = "ab-cd"
输出："dc-ba"
```

- 示例 2：

```python
输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
```

## 解题思路

### 思路 1：双指针

使用双指针分别从字符串的两端向中间移动，只交换英文字母，跳过非英文字母。

1. **初始化**：将字符串转换为列表（Python 字符串不可变），使用左右指针 $left$ 和 $right$。
2. **双指针移动**：
   - 如果 $s[left]$ 不是字母，$left$ 右移
   - 如果 $s[right]$ 不是字母，$right$ 左移
   - 如果两者都是字母，交换它们，然后同时移动
3. **返回结果**：将列表转换回字符串。

### 思路 1：代码

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # 左指针找到字母
            if not s[left].isalpha():
                left += 1
            # 右指针找到字母
            elif not s[right].isalpha():
                right -= 1
            # 交换两个字母
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度，每个字符最多访问一次。
- **空间复杂度**：$O(n)$，需要将字符串转换为列表。
