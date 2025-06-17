# [0345. 反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0345. 反转字符串中的元音字母 - 力扣](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：将字符串中的元音字母进行反转。

**说明**：

- 元音字母包括 `'a'`、`'e'`、`'i'`、`'o'`、`'u'`，且可能以大小写两种形式出现不止一次。
- $1 \le s.length \le 3 \times 10^5$。
- $s$ 由可打印的 ASCII 字符组成。

**示例**：

- 示例 1：

```python
输入：s = "hello"
输出："holle"
```

- 示例 2：

```python
输入：s = "leetcode"
输出："leotcede"
```

## 解题思路

### 思路 1：对撞指针

1. 因为 Python 的字符串是不可变的，所以我们先将字符串转为数组。
2. 使用两个指针 $left$，$right$。$left$ 指向字符串开始位置，$right$ 指向字符串结束位置。
3. 然后 $left$ 依次从左到右移动查找元音字母，$right$ 依次从右到左查找元音字母。
4. 如果都找到了元音字母，则交换字符，然后继续进行查找。
5. 如果遇到 $left == right$ 时停止。
6. 最后返回对应的字符串即可。

### 思路 1：代码

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s)-1
        s_list = list(s)
        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            if s_list[right] not in vowels:
                right -= 1
                continue
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(1)$。