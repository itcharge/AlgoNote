# [0744. 寻找比目标字母大的最小字母](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/)

- 标签：数组、二分查找
- 难度：简单

## 题目链接

- [0744. 寻找比目标字母大的最小字母 - 力扣](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/)

## 题目大意

**描述**：给你一个字符数组 $letters$，该数组按非递减顺序排序，以及一个字符 $target$。$letters$ 里至少有两个不同的字符。

**要求**：找出 $letters$ 中大于 $target$ 的最小的字符。如果不存在这样的字符，则返回 $letters$ 的第一个字符。

**说明**：

- $2 \le letters.length \le 10^4$。
- $letters[i]$$ 是一个小写字母。
- $letters$ 按非递减顺序排序。
- $letters$ 最少包含两个不同的字母。
- $target$ 是一个小写字母。

**示例**：

- 示例 1：

```python
输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"
解释：letters 中字典上比 'a' 大的最小字符是 'c'。
```

- 示例 2：

```python
输入: letters = ["c","f","j"], target = "c"
输出: "f"
解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
```

## 解题思路

### 思路 1：二分查找

利用二分查找，找到比 $target$ 大的字母。注意 $target$ 可能大于 $letters$ 的所有字符，此时应返回 $letters$ 的第一个字母。

我们可以假定 $target$ 的取值范围为 $[0, len(letters)]$。当 $target$ 取到 $len(letters)$ 时，说明 $target$ 大于 $letters$ 的所有字符，对 $len(letters)$ 取余即可得到 $letters[0]$。

### 思路 1：代码

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % n]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为字符数组 $letters$ 的长度。
- **空间复杂度**：$O(1)$。

