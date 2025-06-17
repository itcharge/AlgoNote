# [0821. 字符的最短距离](https://leetcode.cn/problems/shortest-distance-to-a-character/)

- 标签：数组、双指针、字符串
- 难度：简单

## 题目链接

- [0821. 字符的最短距离 - 力扣](https://leetcode.cn/problems/shortest-distance-to-a-character/)

## 题目大意

**描述**：给定一个字符串 $s$ 和一个字符 $c$，并且 $c$ 是字符串 $s$ 中出现过的字符。

**要求**：返回一个长度与字符串 $s$ 想通的整数数组 $answer$，其中 $answer[i]$ 是字符串 $s$ 中从下标 $i$ 到离下标 $i$ 最近的字符 $c$ 的距离。

**说明**：

- 两个下标 $i$ 和 $j$ 之间的 **距离** 为 $abs(i - j)$ ，其中 $abs$ 是绝对值函数。
- $1 \le s.length \le 10^4$。
- $s[i]$ 和 $c$ 均为小写英文字母
- 题目数据保证 $c$ 在 $s$ 中至少出现一次。

**示例**：

- 示例 1：

```python
输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3，所以距离为 abs(0 - 3) = 3。
距下标 1 最近的 'e' 出现在下标 3，所以距离为 abs(1 - 3) = 2。
对于下标 4，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1。
距下标 8 最近的 'e' 出现在下标 6，所以距离为 abs(8 - 6) = 2。
```

- 示例 2：

```python
输入：s = "aaab", c = "b"
输出：[3,2,1,0]
```

## 解题思路

### 思路 1：两次遍历

第一次从左到右遍历，记录每个 $i$ 左边最近的 $c$ 的位置，并将其距离记录到 $answer[i]$ 中。

第二次从右到左遍历，记录每个 $i$ 右侧最近的 $c$ 的位置，并将其与第一次遍历左侧最近的 $c$ 的位置相比较，并将较小的距离记录到 $answer[i]$ 中。

### 思路 1：代码

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        size = len(s)
        ans = [size + 1 for _ in range(size)]

        pos = -1
        for i in range(size):
            if s[i] == c:
                pos = i
            if pos != -1:
                ans[i] = i - pos
        
        pos = -1
        for i in range(size - 1, -1, -1):
            if s[i] == c:
                pos = i
            if pos != -1:
                ans[i] = min(ans[i], pos - i)

        return ans

```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

