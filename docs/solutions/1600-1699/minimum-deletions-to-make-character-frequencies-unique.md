# [1647. 字符频次唯一的最小删除次数](https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/)

- 标签：贪心、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [1647. 字符频次唯一的最小删除次数 - 力扣](https://leetcode.cn/problems/minimum-deletions-to-make-character-frequencies-unique/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：返回使 $s$ 成为优质字符串需要删除的最小字符数。

**说明**：

- **频次**：指的是该字符在字符串中的出现次数。例如，在字符串 `"aab"` 中，`'a'` 的频次是 $2$，而 `'b'` 的频次是 $1$。
- **优质字符串**：如果字符串 $s$ 中不存在两个不同字符频次相同的情况，就称 $s$ 是优质字符串。
- $1 \le s.length \le 10^5$。
- $s$ 仅含小写英文字母。

**示例**：

- 示例 1：

```python
输入：s = "aab"
输出：0
解释：s 已经是优质字符串。
```

- 示例 2：

```python
输入：s = "aaabbbcc"
输出：2
解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc"。
```

## 解题思路

### 思路 1：贪心算法 + 哈希表

1. 使用哈希表 $cnts$ 统计每字符串中每个字符出现次数。
2. 然后使用集合 $s\underline{\hspace{0.5em}}set$ 保存不同的出现次数。
3. 遍历哈希表中所偶出现次数：
   1. 如果当前出现次数不在集合 $s\underline{\hspace{0.5em}}set$ 中，则将该次数添加到集合 $s\underline{\hspace{0.5em}}set$ 中。
   2. 如果当前出现次数在集合 $s\underline{\hspace{0.5em}}set$ 中，则不断减少该次数，直到该次数不在集合 $s\underline{\hspace{0.5em}}set$ 中停止，将次数添加到集合 $s\underline{\hspace{0.5em}}set$ 中，同时将减少次数累加到答案 $ans$ 中。
4. 遍历完哈希表后返回答案 $ans$。

### 思路 1：代码

```Python
class Solution:
    def minDeletions(self, s: str) -> int:
        cnts = Counter(s)
        s_set = set()

        ans = 0
        for key, value in cnts.items():
            while value > 0 and value in s_set:
                value -= 1
                ans += 1
            s_set.add(value)
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

