# [0344. 反转字符串](https://leetcode.cn/problems/reverse-string/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0344. 反转字符串 - 力扣](https://leetcode.cn/problems/reverse-string/)

## 题目大意

**描述**：给定一个字符数组 $s$。

**要求**：将其反转。

**说明**：

- 不能使用额外的数组空间，必须原地修改输入数组、使用 $O(1)$ 的额外空间解决问题。
- $1 \le s.length \le 10^5$。
- $s[i]$ 都是 ASCII 码表中的可打印字符。

**示例**：

- 示例 1：

```python
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```

- 示例 2：

```python
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```

## 解题思路

### 思路 1：对撞指针

1. 使用两个指针 $left$，$right$。$left$ 指向字符数组开始位置，$right$ 指向字符数组结束位置。
2. 交换 $s[left]$ 和 $s[right]$，将 $left$ 右移、$right$ 左移。
3. 如果遇到 $left == right$，跳出循环。

### 思路 1：代码

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
