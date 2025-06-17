# [0925. 长按键入](https://leetcode.cn/problems/long-pressed-name/)

- 标签：双指针、字符串
- 难度：简单

## 题目链接

- [0925. 长按键入 - 力扣](https://leetcode.cn/problems/long-pressed-name/)

## 题目大意

**描述**：你的朋友正在使用键盘输入他的名字 $name$。偶尔，在键入字符时，按键可能会被长按，而字符可能被输入 $1$ 次或多次。

现在给定代表名字的字符串 $name$，以及实际输入的字符串 $typed$。

**要求**：检查键盘输入的字符 $typed$。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），就返回 `True`。否则返回 `False`。

**说明**：

- $1 \le name.length, typed.length \le 1000$。
- $name$ 和 $typed$ 的字符都是小写字母。

**示例**：

- 示例 1：

```python
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
```

- 示例 2：

```python
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
```

## 解题思路

### 思路 1：分离双指针

这道题目的意思是在 $typed$ 里边匹配 $name$，同时要考虑字符重复问题，以及不匹配的情况。可以使用分离双指针来做。具体做法如下：

1. 使用两个指针 $left\underline{\hspace{0.5em}}1$、$left\underline{\hspace{0.5em}}2$，$left\underline{\hspace{0.5em}}1$ 指向字符串 $name$ 开始位置，$left\underline{\hspace{0.5em}}2$ 指向字符串 $type$ 开始位置。
2. 如果 $name[left\underline{\hspace{0.5em}}1] == name[left\underline{\hspace{0.5em}}2]$，则将 $left\underline{\hspace{0.5em}}1$、$left\underline{\hspace{0.5em}}2$ 同时右移。
3. 如果 $nmae[left\underline{\hspace{0.5em}}1] \ne name[left\underline{\hspace{0.5em}}2]$，则：
   1. 如果 $typed[left\underline{\hspace{0.5em}}2]$ 和前一个位置元素 $typed[left\underline{\hspace{0.5em}}2 - 1]$ 相等，则说明出现了重复元素，将 $left\underline{\hspace{0.5em}}2$ 右移，过滤重复元素。
   2. 如果 $typed[left\underline{\hspace{0.5em}}2]$ 和前一个位置元素 $typed[left\underline{\hspace{0.5em}}2 - 1]$ 不等，则说明出现了多余元素，不匹配。直接返回 `False` 即可。

4. 当 $left\underline{\hspace{0.5em}}1 == len(name)$ 或者 $left\underline{\hspace{0.5em}}2 == len(typed)$ 时跳出循环。然后过滤掉 $typed$ 末尾的重复元素。
5. 最后判断，如果 $left\underline{\hspace{0.5em}}1 == len(name)$ 并且 $left\underline{\hspace{0.5em}}2 == len(typed)$，则说明匹配，返回 `True`，否则返回 `False`。

### 思路 1：代码

```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left_1, left_2 = 0, 0

        while left_1 < len(name) and left_2 < len(typed):
            if name[left_1] == typed[left_2]:
                left_1 += 1
                left_2 += 1
            elif left_2 > 0 and typed[left_2 - 1] == typed[left_2]:
                left_2 += 1
            else:
                return False
        while 0 < left_2 < len(typed) and typed[left_2] == typed[left_2 - 1]:
            left_2 += 1

        if left_1 == len(name) and left_2 == len(typed):
            return True
        else:
            return False
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$。其中 $n$、$m$ 分别为字符串 $name$、$typed$ 的长度。
- **空间复杂度**：$O(1)$。

