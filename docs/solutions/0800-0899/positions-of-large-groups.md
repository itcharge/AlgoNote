# [0830. 较大分组的位置](https://leetcode.cn/problems/positions-of-large-groups/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0830. 较大分组的位置 - 力扣](https://leetcode.cn/problems/positions-of-large-groups/)

## 题目大意

**描述**：给定由小写字母构成的字符串 $s$。字符串 $s$ 包含一些连续的相同字符所构成的分组。

**要求**：找到每一个较大分组的区间，按起始位置下标递增顺序排序后，返回结果。

**说明**：

- **较大分组**：我们称所有包含大于或等于三个连续字符的分组为较大分组。

**示例**：

- 示例 1：

```python
输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
```

- 示例 2：

```python
输入：s = "abc"
输出：[]
解释："a","b" 和 "c" 均不是符合要求的较大分组。
```

## 解题思路

### 思路 1：简单模拟

遍历字符串 $s$，统计出所有大于等于 $3$ 个连续字符的子字符串的开始位置与结束位置。具体步骤如下：

1. 令 $cnt = 1$，然后从下标 $1$ 位置开始遍历字符串 $s$。
	1. 如果 $s[i - 1] == s[i]$，则令 $cnt$ 加 $1$。
	2. 如果 $s[i - 1] \ne s[i]$，说明出现了不同字符，则判断之前连续字符个数 $cnt$ 是否大于等于 $3$。
	3. 如果 $cnt \ge 3$，则将对应包含 $cnt$ 个连续字符的子字符串的开始位置与结束位置存入答案数组中。
	4. 令 $cnt = 1$，重新开始记录连续字符个数。
2. 遍历完字符串 $s$，输出答案数组。

### 思路 1：代码

```python
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        cnt = 1
        size = len(s)
        for i in range(1, size):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                if cnt >= 3:
                    res.append([i - cnt, i - 1])
                cnt = 1
        if cnt >= 3:
            res.append([size - cnt, size - 1])
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
